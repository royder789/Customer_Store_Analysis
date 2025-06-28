In this machine learning project, I employ a variety of techniques to analyze customer data, focusing on segmentation, purchase analytics, and predictive modeling.

**Customer Segmentation**:
In **Segmentation.ipynb**, I perform a comprehensive analysis using correlation estimates and data standardization. I apply segmentation methods such as hierarchical clustering, k-means clustering, and Principal Component Analysis (PCA). The process involves extensive visualizations including heatmaps, clusters, dendrograms, and scatter plots to segment and understand customer behavior. The dataset used for this analysis is **segmentation data.csv**.

**Purchase Analytics Descriptive Analysis**:
In **Purchase Analytics Descriptive Analysis.ipynb**, I leverage the segmentation model to divide customers into segments and extract insights about their shopping habits. This notebook involves thorough exploratory data analysis (EDA), addressing questions like shopping frequency, spending patterns, and product purchase frequency relative to store visits. I create dummy variables for essential features and analyze preferences, such as which brands are favored by different segments and the reasons behind their choices. The analysis also includes an examination of revenue across various segments. The data for this analysis is contained in **purchase data.csv**.I have conducted a detailed analysis to answer several key questions related to customer shopping behavior. These questions include:

1. Shopping Frequency: How often do customers go shopping?
2. Spending Patterns: How much money do customers spend during their visits?
3. Product Purchase Frequency: How often do customers buy a particular product relative to their store visits?

**Customer Analytics Predictive Analysis**:
In **Customer Analytics Predictive Analysis.ipynb**, I delve into the calculation of price elasticity for purchase probability and quantity. This analysis includes evaluating purchase probabilities by segments, with and without promotions, as well as determining own and cross-price elasticities by segment. The analysis helps in understanding brand choices made by different customer segments.

In my analysis of price elasticity, I explored how changes in price affect customer shopping behavior. Price elasticity measures the responsiveness of an output variable to a 1% change in an input variable. If the absolute value of 'price elasticity' is less than 1, the demand is considered 'inelastic.' This means a 1% change in price results in less than a 1% change in purchase probability, indicating that an increase in price will not significantly decrease purchase probability. For inelastic products, we can increase the price, whereas for elastic products, we need to decrease the price to boost purchases.

I conducted a detailed analysis to answer several key questions related to customer shopping behavior in response to price changes:

1. Own Brand-Price Elasticity: How does the purchase probability of a customer for a brand change with variations in the price of that brand?
2. Cross-Price Elasticity: How does the purchase probability of a customer for a brand change with fluctuations in the price of other brands?
3. Price Elasticity of Purchase Probability: How does the purchase probability change with and without promotion?
4. Price Elasticity of Purchase Quantity: How does the purchase quantity change with and without promotion?

The dataset **segmentation data.csv** is utilized to build the segmentation model in the **Segmentation.ipynb** notebook. Accompanying this dataset, the **segmentation data legend.xlsx** file provides a detailed explanation of what each column represents within the segmentation data.

For the descriptive analysis conducted in the **Purchase Analytics Descriptive Analysis.ipynb** notebook, I used the **purchase data.csv** dataset. This dataset includes purchase data from a convenience store, recorded on a daily basis over a period of two years. In this project, I focused specifically on the purchase of chocolate candy bars. The **purchase data legend.xlsx** file contains the legends, explaining what each column in the **purchase data.csv** file signifies.
