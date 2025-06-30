from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load pre-trained models
scaler = pickle.load(open('scaler.pickle', 'rb'))
pca = pickle.load(open('pca.pickle', 'rb'))
kmeans_pca = pickle.load(open('kmeans_pca.pickle', 'rb'))
purchase_model = pickle.load(open('purchase_model.pickle', 'rb'))

# Segment labels
segment_labels = {0: 'Fewer-Opportunities', 1: 'Standard', 2: 'Career-Focused', 3: 'Well-Off'}

# Top brands per segment with real brand names and Font Awesome icons
top_brands = {
    0: {  # Fewer-Opportunities
        'Cars': {'icon': 'fa-car', 'brands': ['Budget Rent a Car', 'Used Car Dealerships']},
        'Clothes': {'icon': 'fa-tshirt', 'brands': ['Walmart', 'Target']},
        'Houses': {'icon': 'fa-home', 'brands': ['Affordable Housing', 'Rental Apartments']}
    },
    1: {  # Standard
        'Cars': {'icon': 'fa-car', 'brands': ['Toyota', 'Honda']},
        'Clothes': {'icon': 'fa-tshirt', 'brands': ['Gap', 'Old Navy']},
        'Houses': {'icon': 'fa-home', 'brands': ['Suburban Homes', 'Townhouses']}
    },
    2: {  # Career-Focused
        'Cars': {'icon': 'fa-car', 'brands': ['BMW', 'Mercedes']},
        'Clothes': {'icon': 'fa-tshirt', 'brands': ['Banana Republic', 'J.Crew']},
        'Houses': {'icon': 'fa-home', 'brands': ['Urban Apartments', 'Condos']}
    },
    3: {  # Well-Off
        'Cars': {'icon': 'fa-car', 'brands': ['Tesla', 'Porsche']},
        'Clothes': {'icon': 'fa-tshirt', 'brands': ['Gucci', 'Prada']},
        'Houses': {'icon': 'fa-home', 'brands': ['Luxury Villas', 'Penthouses']}
    }
}
@app.route('/', methods=['GET', 'POST'])
def index():
    probability = None
    if request.method == 'POST':
        # Get form data
        mean_price = float(request.form['mean_price'])
        promotion = int(request.form['promotion'])
        
        # Prepare data for prediction
        X = pd.DataFrame({'Mean_Price': [mean_price], 'Promotion': [promotion]})
        
        # Predict purchase probability (assuming purchase_model is a classifier)
        probability = purchase_model.predict_proba(X)[:, 1][0] * 100  # Convert to percentage
    
    # Render the template, passing the probability if it exists
    return render_template('index.html', probability=probability)

@app.route('/segmentation', methods=['GET', 'POST'])
def segmentation():
    prediction = None
    brands = None
    income_increase = None
    next_segment = None
    next_brands = None
    if request.method == 'POST':
        sex = int(request.form['sex'])
        marital_status = int(request.form['marital_status'])
        age = int(request.form['age'])
        education = int(request.form['education'])
        income = float(request.form['income'])
        occupation = int(request.form['occupation'])
        settlement_size = int(request.form['settlement_size'])

        input_data = np.array([[sex, marital_status, age, education, income, occupation, settlement_size]])
        input_std = scaler.transform(input_data)
        input_pca = pca.transform(input_std)
        segment = kmeans_pca.predict(input_pca)[0]
        prediction = segment_labels[segment]
        brands = top_brands[segment]

        # Calculate income increase to reach next segment
        if segment < 3:  # Not already in the highest segment
            step = 1000
            temp_income = income
            while temp_income <= income * 2:  # Cap at double the income
                temp_data = np.array([[sex, marital_status, age, education, temp_income, occupation, settlement_size]])
                temp_std = scaler.transform(temp_data)
                temp_pca = pca.transform(temp_std)
                temp_segment = kmeans_pca.predict(temp_pca)[0]
                if temp_segment > segment:
                    income_increase = temp_income - income
                    next_segment = segment_labels[temp_segment]
                    next_brands = top_brands[temp_segment]
                    break
                temp_income += step

    return render_template('segmentation.html', prediction=prediction, brands=brands,
                           income_increase=income_increase, next_segment=next_segment, next_brands=next_brands)

@app.route('/descriptive')
def descriptive():
    return render_template('descriptive.html')

@app.route('/predict_segment_ajax', methods=['POST'])
def predict_segment_ajax():
    data = request.json
    sex = int(data['sex'])
    marital_status = int(data['marital_status'])
    age = int(data['age'])
    education = int(data['education'])
    income = float(data['income'])
    occupation = int(data['occupation'])
    settlement_size = int(data['settlement_size'])

    input_data = np.array([[sex, marital_status, age, education, income, occupation, settlement_size]])
    input_std = scaler.transform(input_data)
    input_pca = pca.transform(input_std)
    segment = kmeans_pca.predict(input_pca)[0]
    prediction = segment_labels[segment]
    brands = top_brands[segment]

    return jsonify({'prediction': prediction, 'brands': brands})

if __name__ == '__main__':
    app.run(debug=True)