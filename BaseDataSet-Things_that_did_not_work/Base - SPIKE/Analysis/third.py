import pandas as pd
from sklearn.metrics import cohen_kappa_score

if __name__ == '__main__':

    df = pd.read_csv('0.9.csv')

    filtered_df = df[(df['manual - gili'].isin([-1, 1, 0])) & (df['manual - liron'].isin([-1, 1, 0]))]

    cohen_kappa = cohen_kappa_score(filtered_df['manual - liron'], filtered_df['manual - gili'])

    num_rows = len(filtered_df)
    print(f"Number of rows in the filtered DataFrame: {num_rows}")

    print(f"Cohen's Kappa for 'manual-liron' and 'manual-gili': {cohen_kappa:.2f}")
