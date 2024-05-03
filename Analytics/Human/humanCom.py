import csv


def get_tag(base_sentiment, id, tag_dict):
    if base_sentiment == 'negative':
        return tag_dict[id]['After Positive Framing SA']
    elif base_sentiment == 'positive':
        return tag_dict[id]['After Negative Framing SA']
    else:
        return ''


if __name__ == '__main__':
    first_batch_results_csv = '../MechanicalTurk//Framing//first//first_processed_batch_results.csv'
    allen_csv = 'Advanced/combinedData_allenNLP_result_preprocessed.csv'
    gpt_csv = 'Advanced/combinedData_GPT_result_preprocessed.csv'
    llama2_csv = 'Advanced/combinedData_LLAMA2_result_preproccessed.csv'
    mistral_csv = 'Advanced/combinedData_Mistral_preproccessed.csv'
    output_csv = 'firstBatchComparison.csv'

    tag_dicts = {}
    for csv_file in [allen_csv, gpt_csv, mistral_csv, llama2_csv]:
        tag_dict = {}
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tag_dict[row['ID']] = row
        tag_dicts[csv_file] = tag_dict

    with open(first_batch_results_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['ID', 'human tag', allen_csv, gpt_csv, llama2_csv, mistral_csv]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            id = row['Input.id']
            base_sentiment = row['Base_Sentiment']

            output_row = {'ID': id, 'human tag': row['Majority_Sentiment']}

            for csv_file, tag_dict in tag_dicts.items():
                output_row[csv_file] = get_tag(base_sentiment, id, tag_dict)

            writer.writerow(output_row)

