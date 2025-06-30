**# Customer Store Analysis 🛍️**

**Demo Website:** 🔗 \(https://customer-store-analysi1.onrender.com/)

---

## 🎯 Project Overview

A data-driven web application that helps businesses analyze customer purchasing patterns and visualize insights through interactive dashboards and a user-friendly website.

---

## 📂 File Structure

```
Customer_Store_Analysis/
├── data/                   # Raw and processed datasets
│   ├── raw/                # Original CSV and Excel files
│   └── processed/          # Cleaned and merged data
├── notebooks/              # Jupyter notebooks for exploration & modeling
│   ├── EDA_Customer.ipynb  # Exploratory Data Analysis on customer demographics
│   ├── Sales_Trend.ipynb   # Time-series analysis of sales trends
│   └── Clustering.ipynb    # Customer segmentation using clustering
├── backend/                # (Optional) Backend API code
├── frontend/               # React app for the web interface
│   ├── public/             # Static assets
│   └── src/                # Components & pages
├── requirements.txt        # Python dependencies
├── package.json            # Node.js dependencies
└── README.md               # This documentation
```

---

## 📝 Notebooks Explained

Below is a detailed walkthrough of each analysis notebook, describing objectives, methodologies, datasets, and key deliverables.

**1. Segmentation.ipynb** 🔍

In this notebook, we perform customer segmentation to uncover distinct groups based on purchasing behavior and demographics:

* **Data Loading & Preparation:**

  * Dataset: `segmentation_data.csv` (customer attributes) with definitions in `segmentation_data_legend.xlsx`.
  * Handle missing values, outliers, and ensure consistent data types.

* **Correlation Analysis & Standardization:**

  * Compute a correlation matrix to identify relationships between numerical features.
  * Apply Z‑score standardization to normalize features before clustering.

* **Dimensionality Reduction (PCA):**

  * Use Principal Component Analysis to reduce feature space while retaining > 90% variance.
  * Visualize principal components to confirm separation potential.

* **Clustering Techniques:**

  * **Hierarchical Clustering:** Build dendrograms to infer a natural cluster count.
  * **K‑Means Clustering:** Experiment with K values (using the elbow and silhouette methods) and assign final cluster labels.

* **Visualization & Interpretation:**

  * Heatmaps of standardized feature clusters.
  * Dendrogram plot to illustrate hierarchical structure.
  * Scatter plots of the first two principal components, colored by cluster.

* **Outcome:** A segmentation model saved as `segmentation_model.pkl`, cluster summaries detailing average feature values per group.

---

**2. Purchase\_Analytics\_Descriptive\_Analysis.ipynb** 🛒

This notebook leverages the segmentation results to explore shopping habits and revenue patterns:

* **Data Loading:**

  * Dataset: `purchase_data.csv` (daily transactions for a two‑year period focusing on chocolate candy bars).
  * Column definitions in `purchase_data_legend.xlsx`.

* **Assigning Segments:**

  * Load `segmentation_model.pkl` and map each customer in the purchase data to their segment.

* **Exploratory Data Analysis (EDA):**

  * **Shopping Frequency:** Calculate average store visits per month by segment.
  * **Spending Patterns:** Assess total and per‑visit spend distributions.
  * **Product Purchase Frequency:** Compute purchase rate per item relative to store visits.

* **Brand Preferences & Revenue:**

  * Create dummy variables for top brands and examine brand affinity by segment.
  * Analyze segment‑wise revenue contribution and identify high‑value customer groups.

* **Visualizations:**

  * Bar charts of visit frequency and spend by segment.
  * Box plots of per‑visit expenditure.
  * Stacked area charts showing revenue trends over time.

* **Outcome:** Insight report summarizing key segment behaviors and recommendations for targeted marketing.

---

**3. Customer\_Analytics\_Predictive\_Analysis.ipynb** 🤖

In this notebook, we build predictive models to forecast purchase likelihood and quantity:

* **Feature Engineering:**

  * Generate features such as recency, frequency, and monetary value (RFM) metrics.
  * Encode segment labels and promotional flags.

* **Modeling Approach:**

  * **Classification Model:** Predict purchase occurrence using Logistic Regression and Random Forest classifiers.
  * **Regression Model:** Predict purchase quantity via Linear Regression and Gradient Boosting.

* **Training & Evaluation:**

  * Split data into training/test sets (80/20).
  * Evaluate classification accuracy, precision, recall, and ROC‑AUC.
  * Assess regression performance with RMSE and R² metrics.

* **Scenario Analysis:**

  * Compare model outputs under promotion vs. non‑promotion scenarios.
  * Feature importance plots to highlight key drivers of purchase behavior.

* **Visualizations:**

  * ROC curves and confusion matrices for classifiers.
  * Scatter plots of actual vs. predicted quantities.

* **Outcome:** Saved models (`purchase_classifier.pkl`, `quantity_regressor.pkl`) with documented performance metrics and a summary of actionable insights for pricing and promotions.

---

## 💻 Website Functionality

* **Home Page:** Overview of the application and quick stats
* **Dashboard:** Interactive charts built with Plotly/D3 showing:

  * Customer demographics
  * Sales trends over time
  * Cluster segments and profiles
* **User Management:** Signup, login, and role-based access
* **Data Upload:** Admins can upload new CSVs to refresh data
* **Responsive Design:** Mobile-friendly layout using React & Tailwind CSS


## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/royder789/Customer_Store_Analysis.git
   cd Customer_Store_Analysis
   ```
2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Install Node.js dependencies**

   ```bash
   cd frontend
   npm install
   ```
4. **Run Notebooks**

   ```bash
   jupyter notebook
   ```
5. **Start Frontend**

   ```bash
   npm start
   ```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.
