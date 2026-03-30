# 🛒 E-commerce ETL Pipeline (Data Engineering Project)

## 📌 Overview

This project implements a **production-style ETL (Extract, Transform, Load) pipeline** using real-world e-commerce data.
The pipeline automates data ingestion, transformation, storage, and logging to simulate real-world data engineering workflows.

---

## 🚀 Key Features

* 🔄 Automated data extraction using KaggleHub
* 🧹 Data cleaning and transformation using Pandas
* 🗄️ Structured data storage in PostgreSQL
* 📁 Separation of raw and processed data
* 🧾 Timestamp-based logging for each pipeline run
* ⚙️ Modular and scalable architecture

---

## 🧰 Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* KaggleHub

---

## 📂 Project Structure

```
ecommerce-etl-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── db.py
│   ├── logger.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Pipeline Architecture

Kaggle Dataset → Extract → Transform → Save Processed Data → Load to PostgreSQL → Logging

---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure database in `config.py`

3. Run pipeline:

```bash
python -m scripts.main
```

---

## 📊 Sample SQL Queries

```sql
-- Top customers by orders
SELECT customer_id, COUNT(*) 
FROM orders
GROUP BY customer_id
ORDER BY COUNT(*) DESC
LIMIT 5;

-- Monthly order trends
SELECT DATE_TRUNC('month', order_purchase_timestamp), COUNT(*)
FROM orders
GROUP BY 1;
```

---

## 🧠 Key Learnings

* Built scalable ETL pipelines
* Worked with real-world datasets
* Handled database integration and debugging
* Implemented structured logging and error handling
* Managed data pipelines with modular design

---

## 🔮 Future Enhancements

* Integrate Apache Airflow for orchestration
* Add real-time data ingestion
* Build dashboard using Power BI / Streamlit

---

## 👨‍💻 Author

Rushi Bedmutha
