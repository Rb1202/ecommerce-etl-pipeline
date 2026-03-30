import kagglehub
import pandas as pd
import os
import logging

def extract_data():
    logging.info(" Starting data extraction from Kaggle")

    try:
        # Download dataset
        path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
        logging.info(" Dataset downloaded successfully")

        files = {
            "orders": "olist_orders_dataset.csv",
            "customers": "olist_customers_dataset.csv",
            "products": "olist_products_dataset.csv"
        }

        dataframes = {}

        for key, file in files.items():
            file_path = os.path.join(path, file)

            if not os.path.exists(file_path):
                logging.error(f" File not found: {file_path}")
                raise FileNotFoundError(file_path)

            dataframes[key] = pd.read_csv(file_path)
            logging.info(f" Loaded {key} data")

        logging.info(" Extraction completed successfully")
        return dataframes

    except Exception as e:
        logging.error(f" Extraction failed: {e}")
        raise