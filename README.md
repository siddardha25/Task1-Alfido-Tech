# Task1-Alfido-Tech
# 📈 Monthly Revenue Analysis – Data Analytics Internship Task 1

This project is part of my **Data Analytics Internship at [Alfido Tech](https://www.linkedin.com/company/alfidotech/)**.  
It involves reading a transactional dataset from an ecommerce platform and generating a **monthly revenue trend graph** using Python.

---

## 🧠 Objective

To analyze a sales dataset and visualize:
- **Monthly total revenue**
- Revenue **growth trends**
- Insights for business decision-making

---

## 📂 Dataset Overview

| Column Name           | Description                          |
|------------------------|--------------------------------------|
| Customer ID           | Unique ID for each customer          |
| Purchase Date         | Date of transaction                  |
| Product Category      | Category of purchased product        |
| Product Price         | Unit price of the product            |
| Quantity              | Number of items bought               |
| Total Purchase Amount | Total = Price × Quantity             |
| Payment Method        | Mode of payment                      |
| Gender, Age, Churn    | Customer demographic details         |

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas** – Data cleaning & aggregation
- **Matplotlib** – Data visualization
- **Seaborn** – Enhanced styling for plots

---

## 📊 Output

The script:
1. Cleans and prepares the data
2. Extracts month-wise revenue totals
3. Saves the final revenue trend as a **graph image** (`monthly_revenue.png`) in the project folder

<p align="center">
  <img src="monthly_revenue.png" width="600" alt="Monthly Revenue Graph">
</p>

---

## 📁 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/monthly-revenue-analysis.git
   cd monthly-revenue-analysis
Install dependencies

bash
Copy
Edit
pip install pandas matplotlib seaborn
Place your dataset in the same folder (e.g. data.csv)

Run the script

bash
Copy
Edit
python analysis.py
The output graph will be saved as monthly_revenue.png
