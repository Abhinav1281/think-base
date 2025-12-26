from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import json
import os
from datetime import datetime, timezone

import importlib

accessories = importlib.import_module(".accessories", package="Accessories")
logger = accessories.logger


# Read from environment or config
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_NAME = os.getenv("DB_NAME", "reasoningdb")

# Create connection string
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    return SessionLocal()


def log_run(query: str, response: dict, citations: dict, latency_ms: int):
    """
    Logs a run into the runs table
    """
    sql = """
    INSERT INTO runs (query, response, citations, latency_ms, created_at)
    VALUES (:query, :response, :citations, :latency_ms, :created_at)
    """

    created_at = datetime.now(timezone.utc)

    # Use session
    session = get_session()
    try:
        session.execute(
            text(sql),
            {
                "query": query,
                "response": json.dumps(response),
                "citations": json.dumps(citations),
                "latency_ms": latency_ms,
                "created_at": created_at,
            },
        )
        session.commit()
    except Exception as e:
        session.rollback()
        logger.info(f"Error logging run: {e}")
    finally:
        session.close()
