import pandas as pd
import matplotlib.pyplot as plt


def classify_change(row):
    base = row['Base_Sentiment'].lower()
    majority = row['Majority_Sentiment'].lower()
    if base == majority:
        return 'No Change'
    elif (base == 'positive' and majority == 'negative') or (base == 'negative' and majority == 'positive'):
        return 'Flipped Sentiment'
    else:
        return 'Became Neutral'

if __name__ == '__main__':
    df = pd.read_csv('../../MechanicalTurk//Framing//first//first_processed_batch_results.csv')
    df['Change_Type'] = df.apply(classify_change, axis=1)

    pivot_table = pd.pivot_table(df, index='Base_Sentiment', columns='Change_Type', aggfunc='size', fill_value=0)
    pivot_table_percentage = pivot_table.div(pivot_table.sum(axis=1), axis=0) * 100

    colors = {'Became Neutral': '#AFEEEE', 'Flipped Sentiment': '#F08080', 'No Change': '#D3D3D3'}
    plt.figure(figsize=(10, 6))
    pivot_table_percentage.plot(kind='bar', stacked=True, color=[colors[x] for x in pivot_table_percentage.columns], width=0.8)
    plt.legend(title='Type of Change', bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=3)
    plt.xlabel('Base Sentiment')
    plt.ylabel('Percentage')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for p in plt.gca().patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        if height > 0:
            plt.gca().annotate('{:.1f}%'.format(height), (x + width / 2, y + height / 2), ha='center', va='center', fontsize=8)

    plt.tight_layout()
    plt.savefig('../Figures/humanDist2')
    plt.show()
