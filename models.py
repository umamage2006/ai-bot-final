import numpy as np
from sklearn.linear_model import LinearRegression

def generate_recommendations(age, income, health_expenses, savings_goal, current_investment,data):
   
    future_health_expenses = health_expenses * (1 + 0.03 * (age / 100)) + income * 0.01
  
   
    
    # Simple rule-based recommendations
    if future_health_expenses > health_expenses:
        health_plan = "Consider upgrading your health insurance plan."
    else:
        health_plan = "Your current health insurance seems adequate."
    
    # Investment advice
    future_investment = current_investment * 1.05  # Example of simple growth
    
    if savings_goal > future_investment:
        investment_plan = "Increase your monthly savings by 10% to meet your future goals."
    else:
        investment_plan = "Your investment strategy is on track."
    
    return {
        'health_plan': health_plan,
        'investment_plan': investment_plan,
        'predicted_health_expenses': future_health_expenses,
        'future_investment': future_investment
    }
