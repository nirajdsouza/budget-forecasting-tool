# forecasting.py
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from config import HISTORICAL_REVENUE, HISTORICAL_COSTS, HISTORICAL_OPERATING_EXPENSES, FORECAST_PERIOD

def forecast_revenue():
    model = ExponentialSmoothing(HISTORICAL_REVENUE, trend='add', seasonal=None, damped_trend=True)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=FORECAST_PERIOD)
    return forecast

def forecast_costs():
    model = ExponentialSmoothing(HISTORICAL_COSTS, trend='add', seasonal=None, damped_trend=True)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=FORECAST_PERIOD)
    return forecast

def forecast_operating_expenses():
    model = ExponentialSmoothing(HISTORICAL_OPERATING_EXPENSES, trend='add', seasonal=None, damped_trend=True)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=FORECAST_PERIOD)
    return forecast

def forecast_net_income(forecasted_revenue, forecasted_costs, forecasted_operating_expenses):
    forecasted_net_income = forecasted_revenue - forecasted_costs - forecasted_operating_expenses
    return forecasted_net_income
