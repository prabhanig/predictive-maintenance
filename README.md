# AI-Driven Predictive Maintenance for Service Centers

## Overview
This project demonstrates how **machine learning** can be applied to **predictive maintenance in service centers**. By analyzing historical sensor and maintenance data, the model predicts when maintenance is needed, reducing downtime and improving operational efficiency.

## Features
✔ **Data Preprocessing & Feature Engineering** – Cleaning and transforming sensor data for analysis.  
✔ **Exploratory Data Analysis (EDA)** – Visualizing key trends in sensor readings and maintenance logs.  
✔ **Predictive Modeling** – Training machine learning models (Random Forest, XGBoost, Isolation Forest) for maintenance prediction.  
✔ **Anomaly Detection** – Identifying unusual patterns in sensor data using unsupervised learning techniques.  
✔ **Interactive Dashboard with Streamlit** – Visualizing model predictions and maintenance insights.  
✔ **Deployment-ready scripts** – Easy-to-run Python scripts for model training and prediction.

---

## 📂 Project Structure

```plaintext
AI_Predictive_Maintenance/
│── data/
│   ├── sample_data.csv               # Sample dataset for model training
│── notebooks/
│   ├── predictive_maintenance.ipynb   # Jupyter Notebook with step-by-step execution
│── preprocessing.py                   # Data loading and preprocessing script
│── requirements.txt                    # Required Python libraries
│── README.md                           # Project documentation
```

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/AI_Predictive_Maintenance.git
cd AI_Predictive_Maintenance
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run Jupyter Notebook**
Open the `notebooks/predictive_maintenance.ipynb` file in **Jupyter Notebook** to follow the step-by-step execution.

```bash
jupyter notebook notebooks/predictive_maintenance.ipynb
```

### **4️⃣ Run the Streamlit Dashboard**
To visualize model predictions interactively:
```bash
streamlit run app.py
```

---

## 🔍 Data Description

The dataset (`sample_data.csv`) contains sensor readings and maintenance history for service center equipment.

| Column          | Description                              |
|----------------|------------------------------------------|
| id             | Unique identifier for the observation   |
| timestamp      | Date and time of sensor reading        |
| sensor_1       | Sensor reading #1                      |
| sensor_2       | Sensor reading #2                      |
| sensor_3       | Sensor reading #3                      |
| maintenance_needed | 1 = Maintenance required, 0 = No maintenance |

---

## 🛠️ Machine Learning Models Used

- **Random Forest Classifier** – Used for predictive maintenance classification.
- **XGBoost** – Gradient boosting model for improved accuracy.
- **Isolation Forest & Local Outlier Factor (LOF)** – Unsupervised anomaly detection methods.

---

## 📊 Example Visualization

The **EDA section** in the notebook provides insights into sensor readings over time, highlighting patterns that indicate maintenance needs.

---

## 📈 Model Performance

Model accuracy and performance metrics will be displayed in the **notebook output** after model training.

---

## 🤖 Future Enhancements

- Expand dataset with **real-world service center logs**.
- Implement **deep learning models (LSTMs, CNNs)** for time-series forecasting.
- Deploy as a **web API for real-time predictive maintenance insights**.

---

## 📝 License

This project is open-source and available under the **MIT License**.

---

## 📬 Contact

**Author:** Prabhani Hansika Gunasekera  
🔗 LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/prabhanigunasekera/)  
💻 GitHub: [GitHub Profile](https://github.com/prabhanig)  

---
