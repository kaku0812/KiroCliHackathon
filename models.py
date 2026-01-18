from sqlalchemy import Table, Column, Integer, Float, Boolean, BigInteger, DateTime
from database import metadata
from datetime import datetime

snapshots = Table(
    "snapshots",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("local_id", Integer, nullable=False),
    Column("timestamp", DateTime, nullable=False),
    Column("battery", Integer, nullable=False),
    Column("network", Boolean, nullable=False),
    Column("lat", Float, nullable=False),
    Column("lng", Float, nullable=False)
)