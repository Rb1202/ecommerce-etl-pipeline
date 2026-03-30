from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data
from scripts.logger import setup_logger
import logging

# Initialize logging once
setup_logger()

def run_pipeline():
    logging.info(" Starting ETL Pipeline")

    try:
        raw_data = extract_data()
        logging.info(" Extraction completed")

        clean_data = transform_data(raw_data)
        logging.info(" Transformation completed")

        load_data(clean_data)
        logging.info(" Data loaded into database")

        logging.info(" ETL Pipeline finished successfully")

    except Exception as e:
        logging.error(f" Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()