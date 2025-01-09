# main.py
from budget import create_budget, compare_actual_vs_forecast, print_budget_report
from forecasting import forecast_revenue, forecast_costs, forecast_operating_expenses, forecast_net_income
from analysis import calculate_growth_rate, calculate_profit_margin
from visualization import plot_budget_vs_actual, plot_forecast
from config import BUDGET, HISTORICAL_REVENUE, HISTORICAL_COSTS, HISTORICAL_OPERATING_EXPENSES, FORECAST_PERIOD

def main():
    # Step 1: Create the budget (use the historical data to calculate actual values)
    actual = {
        'Revenue': HISTORICAL_REVENUE,
        'Cost_of_Goods_Sold': HISTORICAL_COSTS,
        'Operating_Expenses': HISTORICAL_OPERATING_EXPENSES,
        'Net_Income': [rev - cgs - oe for rev, cgs, oe in zip(HISTORICAL_REVENUE, HISTORICAL_COSTS, HISTORICAL_OPERATING_EXPENSES)]
    }

    # Step 2: Forecast future values based on historical data
    forecasted_revenue = forecast_revenue()
    forecasted_costs = forecast_costs()
    forecasted_operating_expenses = forecast_operating_expenses()
    forecasted_net_income = forecast_net_income(forecasted_revenue, forecasted_costs, forecasted_operating_expenses)

    # Step 3: Prepare the forecast dictionary
    forecast = {
        'Revenue': forecasted_revenue,
        'Cost_of_Goods_Sold': forecasted_costs,
        'Operating_Expenses': forecasted_operating_expenses,
        'Net_Income': forecasted_net_income
    }

    # Step 4: Compare actual vs forecasted values
    comparison = compare_actual_vs_forecast(actual, forecast)
    
    # Step 5: Print budget report
    print_budget_report(actual, comparison)
    
    # Step 6: Perform analysis on growth rates and profit margin
    revenue_growth_rate = calculate_growth_rate(HISTORICAL_REVENUE)
    cost_growth_rate = calculate_growth_rate(HISTORICAL_COSTS)
    operating_expenses_growth_rate = calculate_growth_rate(HISTORICAL_OPERATING_EXPENSES)
    profit_margin = calculate_profit_margin(sum(HISTORICAL_REVENUE), sum(HISTORICAL_COSTS))

    print("\nRevenue Growth Rate: ", revenue_growth_rate)
    print("Cost Growth Rate: ", cost_growth_rate)
    print("Operating Expenses Growth Rate: ", operating_expenses_growth_rate)
    print("Profit Margin: {:.2f}%".format(profit_margin))
    
    # Step 7: Visualize budget vs actual
    plot_budget_vs_actual(actual, forecast, 'Revenue')
    plot_budget_vs_actual(actual, forecast, 'Cost_of_Goods_Sold')
    plot_budget_vs_actual(actual, forecast, 'Operating_Expenses')

    # Step 8: Visualize forecast
    plot_forecast(forecasted_revenue, 'Revenue')
    plot_forecast(forecasted_costs, 'Costs')
    plot_forecast(forecasted_operating_expenses, 'Operating Expenses')
    plot_forecast(forecasted_net_income, 'Net Income')

if __name__ == "__main__":
    main()
