# visualization.py
import matplotlib.pyplot as plt

def plot_budget_vs_actual(budget, actual, category):
    """
    Plot the budgeted vs actual values for a specific category.
    """
    months = range(1, len(budget[category]) + 1)
    plt.plot(months, budget[category], label='Budgeted', marker='o')
    plt.plot(months, actual[category], label='Actual', marker='o')
    plt.xlabel('Month')
    plt.ylabel(category)
    plt.title(f'{category} - Budget vs Actual')
    plt.legend()
    plt.show()

def plot_forecast(forecasted_values, title):
    """
    Plot the forecasted values for revenue or costs.
    """
    months = range(1, len(forecasted_values) + 1)
    plt.plot(months, forecasted_values, label='Forecasted', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title(f'{title} Forecast')
    plt.legend()
    plt.show()
