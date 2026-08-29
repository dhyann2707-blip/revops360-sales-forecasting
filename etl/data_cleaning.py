import pandas as pd

def run_etl():
    raw_data = {
        'opp_id': ['OPP101', 'OPP102', 'OPP103', 'OPP104', 'OPP105', 'OPP106'],
        'region': ['North America', 'North America', 'APAC', 'North America', 'North America', 'EMEA'],
        'stage': ['Closed Won', 'Proposal', 'Closed Lost', 'Negotiation', 'Qualification', 'Closed Won'],
        'deal_amount': [120000, 85000, 45000, 210000, 60000, 175000]
    }
    df = pd.DataFrame(raw_data)
    probabilities = {
        'Qualification': 0.25, 
        'Proposal': 0.50, 
        'Negotiation': 0.75, 
        'Closed Won': 1.00, 
        'Closed Lost': 0.00
    }
    df['win_probability'] = df['stage'].map(probabilities)
    df['weighted_forecast'] = df['deal_amount'] * df['win_probability']
    return df

if __name__ == '__main__':
    print("ETL Data Pipeline initialized successfully.")
