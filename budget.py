# budget.py
from config import BUDGET

def create_budget():
    """
    Creates the budget for each category (Revenue, COGS, Operating Expenses, Net Income).
    """
    budget = BUDGET
    return budget

def compare_actual_vs_forecast(actual, forecast):
    """
    Compares actual vs forecasted values for the given budget categories.
    """
    comparison = {}
    for key in actual:
        comparison[key] = {
            'Actual': actual[key],
            'Forecast': forecast[key],
            'Difference': [actual_value - forecast_value for actual_value, forecast_value in zip(actual[key], forecast[key])]
        }
    return comparison

def print_budget_report(budget, comparison):
    """
    Prints a simple report of the budget and comparison with actual values.
    """
    print("Monthly Budget and Comparison Report:\n")
    print("Category".ljust(20), "Budget".ljust(10), "Actual".ljust(10), "Difference")
    for category in budget:
        print(f"{category.ljust(20)}", end="")
        print(f"{sum(budget[category]):<10}", end="")
        print(f"{sum(comparison[category]['Actual']):<10}", end="")
        print(f"{sum(comparison[category]['Difference']):<10}")
    print("\n")
