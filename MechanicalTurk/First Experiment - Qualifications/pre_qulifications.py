import pandas as pd
if __name__ == '__main__':
    df = pd.read_csv('pre-qualifiactions-results-2.csv')

    sentence_counts = df.groupby('WorkerId').size()

    result = df.groupby('WorkerId').apply(lambda x: ((x['Input.origin_sentiment'] == x['Answer.sentiment.label']).sum() / len(x)) * 100)

    result_df = pd.DataFrame({'WorkerId': result.index, 'Match_percentage': result.values, 'Total_sentences_assigned': sentence_counts})

    result_df.to_csv('result_with_stats-2.csv', index=False)
