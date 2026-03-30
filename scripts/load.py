import logging
from scripts.db import get_engine

def load_data(data):
    logging.info(" Starting data loading into PostgreSQL")

    try:
        engine = get_engine()

        data["orders"].to_sql("orders", engine, if_exists="replace", index=False)
        logging.info(" Orders table loaded")

        data["customers"].to_sql("customers", engine, if_exists="replace", index=False)
        logging.info(" Customers table loaded")

        data["products"].to_sql("products", engine, if_exists="replace", index=False)
        logging.info(" Products table loaded")

        logging.info(" All data loaded successfully into PostgreSQL")

    except Exception as e:
        logging.error(f" Loading failed: {e}")
        raise