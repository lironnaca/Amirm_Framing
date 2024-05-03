import pandas as pd
import matplotlib.pyplot as plt
import ast
import seaborn as sns

if __name__ == '__main__':
    # [0] positive [1] negative
    df = pd.read_csv('combinedData_Mistral_preproccessed.csv')

    df['After Positive Framing Sentence Score'] = df['After Positive Framing Sentence Score'].apply(ast.literal_eval)
    df['After Negative Framing Sentence Score'] = df['After Negative Framing Sentence Score'].apply(ast.literal_eval)
    df['Base Sentence Score'] = df['Base Sentence Score'].apply(ast.literal_eval)


    negative_base_positive_framing_positive_result = df[(df['Base SA'] == 'negative') & (df['After Positive Framing SA'] == 'positive')]

    negative_base_positive_framing_positive_result['After Positive Framing Sentence Score'] = \
    negative_base_positive_framing_positive_result['After Positive Framing Sentence Score'].apply(lambda x: x[0])

    negative_base_positive_framing_positive_result['Base Sentence Score'] = \
    negative_base_positive_framing_positive_result['Base Sentence Score'].apply(lambda x: x[0])

    negative_base_positive_framing_positive_result['Score Difference'] = abs((negative_base_positive_framing_positive_result[
                                                                         'Base Sentence Score'].astype(float) -
                                                                              negative_base_positive_framing_positive_result[
                                                                         'After Positive Framing Sentence Score'].astype(float)))

    positive_base_negative_framing_negative_result = df[(df['Base SA'] == 'positive') & (df['After Negative Framing SA'] == 'negative')]

    positive_base_negative_framing_negative_result['After Negative Framing Sentence Score'] = \
positive_base_negative_framing_negative_result['After Negative Framing Sentence Score'].apply(lambda x: x[1])

    positive_base_negative_framing_negative_result['Base Sentence Score'] = \
        positive_base_negative_framing_negative_result['Base Sentence Score'].apply(lambda x: x[1])

    positive_base_negative_framing_negative_result['Score Difference'] = abs(
        (positive_base_negative_framing_negative_result[
             'Base Sentence Score'].astype(float) -
         positive_base_negative_framing_negative_result[
             'After Negative Framing Sentence Score'].astype(float)))

    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    sns.histplot(negative_base_positive_framing_positive_result['Score Difference'], color='skyblue', bins=10, alpha=0.6)
    plt.title('Difference in Positive Score\n(Negative Base SA & Positive Framing & LLM Tagged as Positive)')
    plt.xlabel('Score Difference')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.subplot(2, 1, 2)
    sns.histplot(positive_base_negative_framing_negative_result['Score Difference'], color='skyblue', bins=10, alpha=0.6)
    plt.title('Difference in Negative Score\n(Positive Base SA & Negative Framing & LLM Tagged as Negative)')
    plt.xlabel('Score Difference')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('../Figures/Difference Opposite Framing')
    plt.show()

