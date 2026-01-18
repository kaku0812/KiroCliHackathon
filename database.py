from sqlalchemy import create_engine, MetaData
from databases import Database

# SQLite database file
DATABASE_URL = "sqlite:///./snapshots.db"

# Async database
database = Database(DATABASE_URL)

# SQLAlchemy metadata for models
metadata = MetaData()

# Engine for creating tables
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})