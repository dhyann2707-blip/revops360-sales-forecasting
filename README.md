# revops360-sales-forecasting
B2B Sales Pipeline Analytics, KPI Modeling, and Revenue Forecasting Suite
# RevOps360 - Sales Pipeline & Revenue Forecasting Suite

## Executive Summary
RevOps360 is an end-to-end B2B sales pipeline analytics platform built to clean CRM data, calculate conversion KPIs, and construct probability-weighted revenue forecasting models.

## Repository Architecture
- `etl/data_cleaning.py`: Cleans pipeline data, handles stage probabilities, and computes weighted deal values.
- `analytics/forecasting_model.py`: Calculates scenario forecasts (Base, Conservative, Aggressive).
- `docs/KPI_Dictionary.md`: Business definitions for core metrics (Win Rate, Sales Cycle Time, ACV).

## Core KPIs Modeled
- **Win Rate (%)**: `(Closed Won / Total Closed Deals) * 100`
- **Weighted Forecast ($)**: `Sum(Deal Amount * Stage Probability)`
- **Sales Cycle Time**: `Average(Close Date - Created Date)`

