import pandas as pd
import logging

import os

# Get project root
base_dir = os.path.dirname(os.path.dirname(__file__))

# Create correct path
processed_path = os.path.join(base_dir, "data", "processed")

# Ensure folder exists
os.makedirs(processed_path, exist_ok=True)

# Save files
def transform_data(data):
    logging.info(" Starting data transformation")

    try:
        orders = data["orders"].drop_duplicates()
        customers = data["customers"].drop_duplicates()
        products = data["products"].drop_duplicates()

        logging.info(" Removed duplicates")

        # Handle missing values
        orders.fillna(0, inplace=True)
        customers.fillna("Unknown", inplace=True)
        products.fillna(0, inplace=True)

        logging.info(" Handled missing values")

        # Convert date column
        if "order_purchase_timestamp" in orders.columns:
            orders["order_purchase_timestamp"] = pd.to_datetime(
                orders["order_purchase_timestamp"]
            )
            logging.info(" Converted order_purchase_timestamp to datetime")
        
        orders.to_csv(os.path.join(processed_path, "orders_clean.csv"), index=False)
        customers.to_csv(os.path.join(processed_path, "customers_clean.csv"), index=False)
        products.to_csv(os.path.join(processed_path, "products_clean.csv"), index=False)
        logging.info(" Saved processed data to /data/processed")

        logging.info(" Transformation completed successfully")

        return {
            "orders": orders,
            "customers": customers,
            "products": products
        }

    except Exception as e:
        logging.error(f" Transformation failed: {e}")
        raise

