from flask import Flask, render_template, request
from models import generate_recommendations 
import pandas as pd

app = Flask(__name__)

# Home page route with the "Health Wealth Optimizer" button
@app.route('/')
def home():
    return render_template('home.html')

# Route for the input form page
@app.route('/input')
def input_page():
    return render_template('input.html')




@app.route('/result', methods=['GET' , 'POST'])
def result_page():
    if request.method == 'POST':
    # Collect user inputs from the form
        age = int(request.form['age'])
        income = float(request.form['income'])
        health_expenses = float(request.form['health_expenses'])
        savings_goal = float(request.form['savings_goal'])
        current_investment = float(request.form['current_investment'])

        data = pd.read_csv('templates/data/sample_data.csv')
    
    # Call AI model to generate recommendations
        recommendations = generate_recommendations(age, income, health_expenses, savings_goal, current_investment,data)
    
    # Render the result.html page with the recommendations
        return render_template('result.html', recommendations=recommendations)
    else:
        # Handle GET request (optional)
        return "You are not supposed to access this page directly."
    

if __name__ == "__main__":
    app.run(debug=True)

