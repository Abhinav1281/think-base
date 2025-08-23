from fastapi import FastAPI
from app.services import rabbitmq
import threading

app = FastAPI()

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

threading.Thread(target=run_consumer, daemon=True).start()