import pandas as pd
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt

def most_frequent_words(subset):
    all_words = []
    for sentence in subset['Sentence']:
        sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
        words = word_tokenize(sentence)
        words = [word for word in words if word not in stop_words]
        all_words.extend(words)

    word_counter = Counter(all_words)
    most_common_words = word_counter.most_common(30)

    return most_common_words

if __name__ == '__main__':
    df = pd.read_csv('../Analysis/Spike.csv', encoding='unicode_escape')

    filtered_df = df[df['Sentiment'] != 0]

    nltk.download('punkt')
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    positive_subset = filtered_df[filtered_df['Sentiment'] == 1]
    negative_subset = filtered_df[filtered_df['Sentiment'] == -1]

    most_common_positive_words = most_frequent_words(positive_subset)
    most_common_negative_words = most_frequent_words(negative_subset)

    positive_words, positive_counts = zip(*most_common_positive_words)
    negative_words, negative_counts = zip(*most_common_negative_words)

    plt.figure(figsize=(12, 6))
    plt.bar(positive_words, positive_counts, color='green', alpha=0.7)
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Most Common Positive Words (Excluding Stopwords)')
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.bar(negative_words, negative_counts, color='red', alpha=0.7)
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Most Common Negative Words (Excluding Stopwords)')
    plt.xticks(rotation=45, fontsize=10)
    plt.tight_layout()
    plt.show()


    sentence_lengths = [len(word_tokenize(sentence.lower())) for sentence in df['Sentence']]
    plt.hist(sentence_lengths, bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Sentence Lengths')
    plt.xlabel('Sentence Length')
    plt.ylabel('Frequency')
    plt.grid(False)
    plt.show()


    grouped = df.groupby(['Pattern', 'Sentiment']).size().unstack(fill_value=0)
    pattern_counts = grouped.sum(axis=1)
    sorted_patterns = pattern_counts.sort_values(ascending=False).index
    colors = sns.color_palette("husl", n_colors=2)
    plot_data = grouped.reset_index()
    plot_data = pd.melt(plot_data, id_vars=['Pattern'], value_vars=[-1, 1], var_name='Sentiment', value_name='Count')

    plt.figure(figsize=(12, 6))
    sns.set(style='whitegrid')
    ax = sns.barplot(
        data=plot_data,
        x='Pattern',
        y='Count',
        hue='Sentiment',
        palette=colors,
        order=sorted_patterns
    )
    plt.xlabel('Pattern')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution for Different Patterns')
    plt.xticks(rotation=90)
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles=handles, labels=['-1', '1'], title='Sentiment', loc='upper right')
    plt.show()

    filtered_df = df[df['Sentiment'].isin([-1, 1])]
    grouped = filtered_df.groupby(['Pattern', 'Sentiment']).size().unstack(fill_value=0)
    pattern_counts = grouped.sum(axis=1)
    sorted_patterns = pattern_counts.sort_values(ascending=False).index
    plot_data = grouped.reset_index()
    plot_data = pd.melt(plot_data, id_vars=['Pattern'], value_vars=[-1, 1], var_name='Sentiment', value_name='Count')
    plt.figure(figsize=(12, 6))
    sns.set(style='whitegrid')
    sns.barplot(data=plot_data, x='Pattern', y='Count', hue='Sentiment', palette=['red', 'blue'], order=sorted_patterns)
    plt.xlabel('Pattern')
    plt.ylabel('Count')
    plt.title('Sentiment Distribution for Different Patterns')
    plt.xticks(rotation=90)
    plt.legend(title='Sentiment', loc='upper right', labels=['-1', '1'])
    plt.show()

