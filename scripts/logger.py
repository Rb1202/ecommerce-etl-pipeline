import logging
import datetime
import os

def setup_logger():
    # Create logs folder (optional but recommended)
    os.makedirs("logs", exist_ok=True)

    # Generate unique filename
    filename = f"logs/etl_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename=filename,
        filemode="w"   # new file every run
    )