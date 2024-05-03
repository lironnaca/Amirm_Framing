import pandas as pd
import matplotlib.pyplot as plt


def classify_change(row, base, after):
    if row[base].lower() == 'negative':
        afterFraming = row[after].lower()
        if afterFraming == 'negative':
            return 'No Change'
        elif afterFraming == 'positive':
            return 'Flipped Sentiment'
        else:
            return 'Became Neutral'
    else:
        afterFraming = row[after].lower()
        if afterFraming == 'positive':
            return 'No Change'
        elif afterFraming == 'negative':
            return 'Flipped Sentiment'
        else:
            return 'Became Neutral'

if __name__ == '__main__':
    df = pd.read_csv('../Advanced/combinedData_Mistral_preproccessed.csv')

    base_neg_df = df[(df['Base SA'].str.lower().str.contains('negative'))]
    base_pos_df = df[(df['Base SA'].str.lower().str.contains('positive'))]

    base_neg_df['Change_Type'] = base_neg_df.apply(
        lambda row: classify_change(row, 'Base SA', 'After Positive Framing SA'), axis=1)
    base_pos_df['Change_Type'] = base_pos_df.apply(
        lambda row: classify_change(row, 'Base SA', 'After Negative Framing SA'), axis=1)

    pivot_neg = pd.pivot_table(base_neg_df, index='Base SA', columns='Change_Type', aggfunc='size', fill_value=0)
    pivot_pos = pd.pivot_table(base_pos_df, index='Base SA', columns='Change_Type', aggfunc='size', fill_value=0)

    pivot_percentage_neg = pivot_neg.div(pivot_neg.sum(axis=1), axis=0) * 100
    pivot_percentage_pos = pivot_pos.div(pivot_pos.sum(axis=1), axis=0) * 100

    colors = {'Became Neutral': '#AFEEEE', 'Flipped Sentiment': '#F08080', 'No Change': '#D3D3D3'}
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 6), sharey=True)

    pivot_percentage_neg.plot(kind='bar', stacked=True, color=[colors[x] for x in pivot_percentage_neg.columns],
                              width=0.8, ax=axes[0])
    axes[0].set_title('Negative Base Sentiment Changes')
    axes[0].set_xlabel('Base Sentiment')
    axes[0].set_ylabel('Percentage')
    axes[0].tick_params(axis='x', rotation=0)
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)

    pivot_percentage_pos.plot(kind='bar', stacked=True, color=[colors[x] for x in pivot_percentage_pos.columns],
                              width=0.8, ax=axes[1])
    axes[1].set_title('Positive Base Sentiment Changes')
    axes[1].set_xlabel('Base Sentiment')
    axes[1].tick_params(axis='x', rotation=0)
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)

    for ax in axes:
        for p in ax.patches:
            width, height = p.get_width(), p.get_height()
            x, y = p.get_xy()
            if height > 0:
                ax.annotate(f'{height:.1f}%', (x + width / 2, y + height / 2), ha='center', va='center', fontsize=10)

    fig.legend([x for x in colors.keys()], title='Type of Change', loc='lower center', bbox_to_anchor=(0.5, -0.05),
               ncol=3)

    plt.tight_layout(rect=[0, 0.1, 1, 1])
    plt.savefig('../Figures/CombinedSentimentChanges.png')
    plt.show()