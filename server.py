from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
from contextlib import asynccontextmanager
from database import database, metadata, engine
from models import snapshots
import sqlalchemy

# -------------------- MODELS --------------------

class SnapshotPayload(BaseModel):
    local_id: int
    timestamp: int  # millis
    battery: int
    network: bool
    lat: float
    lng: float

class SyncResponse(BaseModel):
    acked_ids: List[int]

# -------------------- LIFESPAN --------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    metadata.create_all(engine)
    await database.connect()
    print("Database connected and tables created")
    yield
    # Shutdown
    await database.disconnect()
    print("Database disconnected")

# -------------------- APP --------------------

app = FastAPI(
    title="Safety Snapshot Sync API",
    description="Receives device snapshots from Android app",
    version="1.0",
    lifespan=lifespan
)

# -------------------- ROUTES --------------------

@app.post("/sync/snapshots", response_model=SyncResponse)
async def upload_snapshots(payload: List[SnapshotPayload]):
    if not payload:
        raise HTTPException(status_code=400, detail="Empty payload")
    
    acked_ids = []
    
    for snap in payload:
        query = snapshots.insert().values(
            local_id=snap.local_id,
            timestamp=datetime.fromtimestamp(snap.timestamp / 1000),
            battery=snap.battery,
            network=snap.network,
            lat=snap.lat,
            lng=snap.lng
        )
        await database.execute(query)
        acked_ids.append(snap.local_id)
    
    print(f"[{datetime.now()}] Received {len(payload)} snapshots")
    return SyncResponse(acked_ids=acked_ids)

@app.get("/snapshots")
async def get_snapshots():
    query = snapshots.select()
    result = await database.fetch_all(query)
    return [dict(r) for r in result]