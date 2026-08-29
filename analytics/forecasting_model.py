import pandas as pd

def calculate_scenarios(base_forecast):
    conservative = base_forecast * 0.85
    aggressive = base_forecast * 1.15
    return conservative, aggressive

if __name__ == '__main__':
    base_val = 422500.00
    cons, agg = calculate_scenarios(base_val)
    print(f"Base Forecast: ${base_val:,.2f}")
    print(f"Conservative Target: ${cons:,.2f}")
    print(f"Aggressive Target: ${agg:,.2f}")
