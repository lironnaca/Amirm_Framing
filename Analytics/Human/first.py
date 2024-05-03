import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../../MechanicalTurk//Framing//first//first_processed_batch_results.csv')

    df_positive = df[df['Base_Sentiment'] == 'positive']
    df_negative = df[df['Base_Sentiment'] == 'negative']

    pivot_table_positive = pd.pivot_table(df_positive, index='Base_Sentiment', columns='Majority_Sentiment',
                                          aggfunc='size', fill_value=0)
    pivot_table_negative = pd.pivot_table(df_negative, index='Base_Sentiment', columns='Majority_Sentiment',
                                          aggfunc='size', fill_value=0)

    print(pivot_table_positive)
    print(pivot_table_negative)

    pivot_table_percentage_positive = pivot_table_positive.div(pivot_table_positive.sum(axis=1), axis=0) * 100
    pivot_table_percentage_negative = pivot_table_negative.div(pivot_table_negative.sum(axis=1), axis=0) * 100

    combined_data = pd.concat([pivot_table_percentage_positive, pivot_table_percentage_negative])

    colors = ['#2ca02c', '#ff7f0e', '#1f77b4']
    plt.figure(figsize=(10, 6))
    combined_data.plot(kind='bar', stacked=True, color=colors, width=0.8)
    plt.title('Distribution of Human Tag After Opposite Framing`')
    plt.xlabel('Base Sentiment')
    plt.ylabel('Percentage')
    plt.xticks(rotation=0)
    plt.legend(title='Majority Sentiment')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for p in plt.gca().patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        plt.gca().annotate('{:.1f}%'.format(height), (x + width / 2, y + height / 2), ha='center', va='center',
                           fontsize=8)

    plt.gca().yaxis.set_visible(False)

    plt.tight_layout()
    plt.savefig('../Figures/human dist.png')
    plt.show()