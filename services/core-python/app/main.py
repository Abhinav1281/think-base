from Accessories.accessories import logger
from services.Database.db_services import get_session
from sqlalchemy import text

from services import rabbitmq


def __run_consumer():
    rabbitmq.start_consumer()


def __startup_event():
    session = get_session()
    try:
        result = session.execute(text("SELECT NOW()")).fetchone()
        logger.info(f"[DB Check] Postgres connection successful! Time: {result[0]}")
        # Run consumer in the main thread so the process stays alive
        # Daemon threads won't keep the interpreter running after main exits,
        # which caused the consumer to be killed immediately.
        __run_consumer()
    except Exception as e:
        logger.info(f"[DB Check] Connection failed: {e}")
        # Optionally, raise exception to stop the app
        raise e
    finally:
        session.close()


if __name__ == "__main__":
    __startup_event()
