import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)

    # Convert failure types into binary 'maintenance_needed' column (1 if any failure occurs, else 0)
    df['maintenance_needed'] = df[['Failure Type']].apply(lambda x: 0 if x['Failure Type'] == 'No Failure' else 1, axis=1)

    # Drop redundant columns
    df.drop(columns=['UDI', 'Product ID', 'Failure Type'], inplace=True)

    return df

if __name__ == '__main__':
    df = load_data('data/predictive_maintenance.csv')
    print(df.head())
