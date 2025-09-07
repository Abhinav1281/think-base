from .Database.db import log_run

def ingest_message(data):
    print(f"Ingesting data: {data}", flush=True)
    log_run("DOCUMENT INGESTION", {"status": "ingested"}, {"source": data.get("doc_id", "unknown")}, 0)
    print(f"Ingestion complete", flush=True)
    
    