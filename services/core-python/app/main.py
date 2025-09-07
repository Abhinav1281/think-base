from fastapi import FastAPI
from app.services import rabbitmq
from app.services.Database.db import get_session
import threading
from .services.Database.db import get_session
from sqlalchemy import text

def startup_event(app: FastAPI):
    session = get_session()
    try:
        result = session.execute(text("SELECT NOW()")).fetchone()
        print(f"[DB Check] Postgres connection successful! Time: {result[0]}")
    except Exception as e:
        print(f"[DB Check] Connection failed: {e}")
        # Optionally, raise exception to stop the app
        raise e
    finally:
        session.close()
    threading.Thread(target=run_consumer, daemon=True).start()
    yield
    
app = FastAPI(lifespan=startup_event)

@app.get("/health")
def health_check():
    return {"status": "HEALTHY"}

@app.post("/query")
def query_data(query):
    # Process the query and return results (this is just a placeholder)
    results = {"query": query, "results": ["result1", "result2"]}
    return results

def run_consumer():
    rabbitmq.start_consumer()