# Financial Forecasting and Budgeting Tool

This project is a learning tool developed to demonstrate the process of financial forecasting, budgeting, and analysis. It uses historical financial data to create budgets, forecast future values, compare actual vs. forecasted results, and perform financial analysis such as calculating growth rates and profit margins. Visualizations of the budget vs actual values and forecast data are also provided.

## Features

-   **Budget Creation**: Use historical data to create a budget for categories like Revenue, Cost of Goods Sold, Operating Expenses, and Net Income.
-   **Forecasting**: Generate forecasts for future values based on historical data using Exponential Smoothing.
-   **Comparison**: Compare actual values with forecasted values and calculate the differences.
-   **Analysis**: Perform analysis on growth rates for revenue, costs, and operating expenses, and calculate the profit margin.
-   **Visualization**: Visualize budget vs actual data and forecast values through line charts.

## Requirements

-   Python 3.x
-   `numpy`
-   `statsmodels`
-   `matplotlib`

## Usage

1.  Configure your financial data in `config.py`.
    
2.  Run the main program:
    
	   ```bash
	python main.py
	```
    

This will:

-   Create a budget based on the historical data.
-   Forecast future values for revenue, costs, and operating expenses.
-   Compare actual vs forecasted values.
-   Perform growth rate analysis and calculate profit margin.
-   Generate visualizations of the budget vs actual and forecast data.

## Notes

-   This tool is designed as a learning project to explore financial modeling, forecasting, and data analysis techniques.
-   The models used for forecasting are based on simple Exponential Smoothing.

## License

[MIT](LICENSE) License