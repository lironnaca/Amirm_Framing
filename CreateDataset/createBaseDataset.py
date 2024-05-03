import pandas as pd
import random
if __name__ == '__main__':
    csv_files = ['../TaggingApps/BaseSentencesTaggingApp/Sentences/TempleteOneWithNegativeVerbs.csv',
                 '../TaggingApps/BaseSentencesTaggingApp/Sentences/TempleteOneWithPositiveVerbs.csv',
                 '../TaggingApps/BaseSentencesTaggingApp/Sentences/TempleteTwoWithNegativeAdjectives.csv',
                 '../TaggingApps/BaseSentencesTaggingApp/Sentences/TempleteTwoWithPositiveAdjectives.csv']

    dfs = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df = combined_df[combined_df['answer'].isin(['positive', 'negative'])]

    combined_df = combined_df[['sentence_text', 'answer']]
    combined_df = combined_df.drop_duplicates(subset=['sentence_text'])

    combined_df.to_csv('combinedData_before_framing.csv', index=False)
