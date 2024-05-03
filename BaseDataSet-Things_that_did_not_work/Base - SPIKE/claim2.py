from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
import csv
import pandas as pd
def filter_row(row):
    sentiment = row['sentiment']
    predictions = row['predictions']
    if predictions["probs"][0] > 0.7 or predictions["probs"][1] > 0.7:
        return True
    else:
        return False

if __name__ == '__main__':
    predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/stanford-sentiment-treebank-roberta.2021-03-11.tar.gz")
    input_filename = "processed_dataset.csv"
    output_filename = "SAFilter.csv"

    data = pd.read_csv(input_filename)

    data['predictions'] = data['sentence'].apply(predictor.predict)
    data.to_csv("data_with_pred.csv", index=False)

    #############################
    filtered_data = data[data.apply(filter_row, axis=1)]
    filtered_data.drop(columns=['predictions'], inplace=True)
    filtered_data.to_csv("0.7.csv", index=False)

    ###############################

    with open('claim_stance_dataset_v1.csv', newline='') as csvfile:
        all = []
        reader = csv.DictReader(csvfile)
        for row in reader:
          if row['topicText'] not in all and row['topicSentiment'] == '-1':
              all.append(row['topicText'])
