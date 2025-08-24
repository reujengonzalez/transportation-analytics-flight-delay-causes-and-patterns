# Flight Delay Causes & Patterns (Transportation Analytics) [Python, MySQL, Tableau]

## 📌 Overview

This project explores **flight delays** across U.S. airports, analyzing causes, time-based trends, and geographic patterns. Using **Python** for preprocessing, **MySQL** for structured querying, and **Tableau** for dashboard visualization, the analysis highlights which airlines and airports experience the most delays and uncovers the factors driving these disruptions.

---

## 🎯 Objectives

* Identify the **most common causes** of flight delays (weather, carrier, late aircraft, etc.).
* Compare delay performance across **airlines and airports**.
* Detect **seasonal and time-of-day patterns** in flight delays.
* Provide interactive dashboards for travelers, airlines, and policymakers to understand delay reliability.

---

## 📂 Dataset Description

* **Source**: Flight Delay and Causes dataset [Kaggle](https://www.kaggle.com/datasets/undersc0re/flight-delay-and-causes?utm_source=chatgpt.com)
* **Size**: Millions of flight records across multiple years (\~5M+ rows)
- **Main Features:**
  * `Flight Date`, `Carrier`, `Origin Airport`, `Destination Airport`
  * `Arrival Delay`, `Departure Delay`, `Delay Cause` (Weather, Carrier, NAS, Security, Late Aircraft)
* **Preprocessing (Python)**:
  * Cleaned missing and inconsistent values
  * Normalized airport and airline codes
  * Created derived metrics: `% Delayed Flights`, `Average Delay Minutes`
  * Exported structured data into MySQL for querying and visualization

---

## 🛠 Tools & Techniques

* **Python (Pandas, NumPy, Matplotlib)**
  * Data wrangling and feature engineering
  * Initial exploratory data analysis (delay distributions, histograms)
* **SQL (MySQL)**
  * Aggregation by airline, airport, and month
  * Filtering based on delay causes
* **Tableau**
  * Heatmaps of delay rates by airport
  * Trendlines of delays by month/season
  * Comparative dashboards for airline reliability
  * Geographic visualization of delay hotspots

---

## 🔑 Key Insights

* **Weather-related delays** peaked during winter months, especially in northern airports.
* **Late Aircraft** was the leading cause of delays overall, indicating systemic scheduling issues.
* **Hub airports (e.g., ATL, ORD, DFW)** showed higher delay frequencies but also managed higher traffic volumes.
* **Low-cost carriers** experienced more frequent delays compared to legacy airlines.
* Geographic heatmaps revealed **regional clusters of delays**, with the Northeast corridor being most affected.

👉 [View Tableau Dashboard](https://public.tableau.com/app/profile/reujen.gonzalez/viz/FlightDelayAnalysisDashboard_17546768445230/Dashboard1)

---

## ⚡ Challenges & Solutions

* **Data volume**: Handling millions of records → Used Python for chunked data cleaning and MySQL indexing for faster queries.
* **Inconsistent airport codes**: Standardized using FAA reference tables.
* **Complex delay categories**: Grouped causes into broader categories for clearer visualization.
* **Dashboard readability**: Initially cluttered → Streamlined with interactive filters (airline, airport, time range).

---

## 🔍 How to Explore

1. **Dashboard** – Explore the interactive Tableau dashboard [here](https://public.tableau.com/app/profile/reujen.gonzalez/viz/FlightDelayAnalysisDashboard_17546768445230/Dashboard1)
2. **Scripts** – Check the `scripts/` folder for scripts used in Python.  
3. **Case Study** – Read the full write-up in `transportation-analytics-case-study.docx`.  

---

## 🚀 Next Steps

* Build **predictive models (ML)** to forecast flight delays using historical data.
* Integrate **real-time flight status APIs** for live dashboards.
* Include **weather API integration** to correlate conditions with real-time delays.
* Explore **passenger experience metrics** (missed connections, satisfaction scores).

---

📌 **Author:** Reujen Gonzalez 

🔗 **Portfolio Website:** [Link](https://reujengonzalez.github.io/) | **LinkedIn:** [Link](https://www.linkedin.com/in/reujen-river-gonzalez-878356350/) | **GitHub:** [Link](https://github.com/reujengonzalez)
