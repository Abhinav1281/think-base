import importlib

from .Database.db_services import log_run

accessories = importlib.import_module(".accessories", package="Accessories")
logger = accessories.logger


def ingest_message(data):
    logger.info(f"Ingesting data: {data}")
    log_run(
        "DOCUMENT INGESTION",
        {"status": "ingested"},
        {"source": data.get("doc_id", "unknown")},
        0,
    )
    logger.info("Ingestion complete")
