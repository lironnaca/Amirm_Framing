import pandas as pd

if __name__ == '__main__':
    input_filename = "claim_stance_dataset_v1.csv"
    output_filename = "processed_dataset.csv"

    data = pd.read_csv(input_filename)

    new_data = data[['claims.claimCorrectedText', 'claims.stance', 'texttopic']]
    new_data.columns = ['sentence', 'sentiment', 'original topic']

    new_data['sentiment_order'] = new_data['sentiment'].apply(lambda x: 1 if x == 'Pro' else 2)
    new_data.sort_values(by=['original topic', 'sentiment_order'], inplace=True)

    new_data.drop(columns=['sentiment_order'], inplace=True)

    new_data.to_csv(output_filename, index=False)

    ###############################
    data = pd.read_csv("processed_dataset.csv")
    rows_to_keep = []

    for index, row in data.iterrows():
        sentence = row['sentence'].lower()
        main_words = row['main'].lower().split()

        if any(word in sentence for word in main_words):
            rows_to_keep.append(index)

    filtered_data = data.iloc[rows_to_keep]
    filtered_data.to_csv("OrFilter.csv", index=False)