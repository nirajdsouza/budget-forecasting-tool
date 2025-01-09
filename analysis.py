# analysis.py
import numpy as np

def calculate_growth_rate(values):
    """
    Calculate the growth rate for a series of values (e.g., Revenue, Costs).
    """
    growth_rate = [(values[i] - values[i - 1]) / values[i - 1] * 100 for i in range(1, len(values))]
    return growth_rate

def calculate_profit_margin(revenue, costs):
    """
    Calculate the profit margin given revenue and costs.
    """
    profit_margin = (revenue - costs) / revenue * 100
    return profit_margin
