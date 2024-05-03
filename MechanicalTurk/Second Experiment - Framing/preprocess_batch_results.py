import pandas as pd
from collections import Counter

def majority_sentiment(labels):
    counts = Counter(labels)
    max_count = max(counts.values())
    if max_count > 1:
        return max((label for label, count in counts.items() if count == max_count))
    else:
        return 'Neutral'

if __name__ == '__main__':
    input_file = "FirstBatch//first_batch_results.csv"
    output_file = "FirstBatch//first_processed_batch_results.csv"
    df = pd.read_csv(input_file)

    grouped = df.groupby('HITId').agg({
        'WorkerId': lambda x: len(set(x)),
        'Answer.sentiment.label': majority_sentiment,
        'Input.base_sentiment': 'first',
        'Input.id': 'first'
    }).reset_index()

    grouped.columns = ['HITid', 'Num_WorkerIDs', 'Majority_Sentiment', 'Base_Sentiment', 'Input.id']
    grouped = grouped.sort_values(by='Input.id')
    grouped.to_csv(output_file, index=False)
