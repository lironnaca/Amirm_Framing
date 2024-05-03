import pandas as pd
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter

def word_probabilities(positive_subset, negative_subset):
    positive_text = ' '.join(positive_subset['sentence']).lower()
    negative_text = ' '.join(negative_subset['sentence']).lower()

    positive_words = set(positive_text.split())
    negative_words = set(negative_text.split())

    word_probabilities = {}
    all_words = positive_words.union(negative_words)

    for word in all_words:
        positive_count = positive_text.split().count(word)
        negative_count = negative_text.split().count(word)

        total_count = positive_count + negative_count
        if total_count > 0:
            prob_positive = positive_count / total_count
            prob_negative = negative_count / total_count
            word_probabilities[word] = {'positive': prob_positive, 'negative': prob_negative}

    return word_probabilities


if __name__ == '__main__':
    df = pd.read_csv('0.9.csv')
    filtered_df = df[df['manual - liron'] != 0]
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    positive_subset = filtered_df[filtered_df['manual - liron'] == 1]
    negative_subset = filtered_df[filtered_df['manual - liron'] == -1]

    word_probabilities_dict = word_probabilities(positive_subset, negative_subset)

    positive_subset['sentiment'] = positive_subset['sentence'].apply(
        lambda x: calculate_sentence_sentiment(x, word_probabilities_dict))
    negative_subset['sentiment'] = negative_subset['sentence'].apply(
        lambda x: calculate_sentence_sentiment(x, word_probabilities_dict))

    positive_and_manual_1 = filtered_df[filtered_df['manual - liron'] == 1]
    positive_and_manual_1['sentiment'] = positive_and_manual_1['sentence'].apply(
        lambda x: calculate_sentence_sentiment(x, word_probabilities_dict))

    count_positive_and_manual_1 = len(positive_and_manual_1)

    print(f"Number of sentences with Positive Sentiment and '1' in manual-liron: {count_positive_and_manual_1}")

    filtered_df = df[df['manual - liron'].isin([-1, 1])]

    grouped = filtered_df.groupby(['main', 'manual - liron']).size().unstack(fill_value=0)

    plt.figure(figsize=(12, 6))
    sns.set(style='whitegrid')
    sns.barplot(data=grouped.reset_index(), x='main', y=-1, color='red', label='-1')
    sns.barplot(data=grouped.reset_index(), x='main', y=1, color='blue', label='1')
    plt.xlabel('Original Topic')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution for Different Topics')
    plt.xticks(rotation=90)
    plt.legend(title='Sentiment', loc='upper right')
    plt.show()