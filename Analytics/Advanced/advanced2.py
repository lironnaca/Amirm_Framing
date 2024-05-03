import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ast

if __name__ == '__main__':
    df = pd.read_csv('combinedData_LLAMA2_result_preproccessed.csv')

    df['After Positive Framing Sentence Score'] = df['After Positive Framing Sentence Score'].apply(ast.literal_eval)
    df['After Negative Framing Sentence Score'] = df['After Negative Framing Sentence Score'].apply(ast.literal_eval)
    df['Base Sentence Score'] = df['Base Sentence Score'].apply(ast.literal_eval)

    df['Positive Difference After Positive'] = df.apply(
        lambda row: float(row['After Positive Framing Sentence Score'][0]) - float(row['Base Sentence Score'][0]),
        axis=1)

    df['Negative Difference After Negative'] = df.apply(
        lambda row: float(row['After Negative Framing Sentence Score'][1]) - float(row['Base Sentence Score'][1]),
        axis=1)

    bin_ranges = np.linspace(max(0, df['Positive Difference After Positive'].min()),
                             df['Positive Difference After Positive'].max(), 20)
    df['Binned Differences'] = pd.cut(df['Positive Difference After Positive'], bins=bin_ranges, include_lowest=True)

    avg_base_scores = df.groupby('Binned Differences')['Base Sentence Score'].apply(
        lambda scores: np.mean([float(score[0]) for score in scores])).reset_index()
    avg_base_scores['mid'] = avg_base_scores['Binned Differences'].apply(lambda x: x.mid)

    plt.figure(figsize=(12, 6))
    hist = sns.histplot(df['Positive Difference After Positive'], bins=bin_ranges, color='skyblue', alpha=0.6)
    plt.title('Difference in Positive Scores After Positive Framing')
    plt.xlabel('Difference')
    plt.ylabel('Density')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.xlim([0, None])

    for _, row in avg_base_scores.iterrows():
        y_position = hist.patches[int(np.digitize(row['mid'], bin_ranges)) - 1].get_height()
        plt.annotate(f'{row["Base Sentence Score"]:.2f}', xy=(row['mid'], y_position), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontweight='bold', color='black')

    plt.tight_layout()
    plt.savefig('Pos Diff with Avg')



    ######################

    bin_ranges = np.linspace(max(0, df['Negative Difference After Negative'].min()),
                             df['Negative Difference After Negative'].max(), 20)
    df['Binned Differences'] = pd.cut(df['Negative Difference After Negative'], bins=bin_ranges, include_lowest=True)

    avg_base_scores = df.groupby('Binned Differences')['Base Sentence Score'].apply(
        lambda scores: np.mean([float(score[0]) for score in scores])).reset_index()
    avg_base_scores['mid'] = avg_base_scores['Binned Differences'].apply(lambda x: x.mid)

    plt.figure(figsize=(12, 6))
    hist = sns.histplot(df['Negative Difference After Negative'], bins=bin_ranges, color='skyblue', alpha=0.6)
    plt.title('Difference in Negative Scores After Negative Framing')
    plt.xlabel('Difference')
    plt.ylabel('Density')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.xlim([0, None])

    for _, row in avg_base_scores.iterrows():
        y_position = hist.patches[int(np.digitize(row['mid'], bin_ranges)) - 1].get_height()
        plt.annotate(f'{row["Base Sentence Score"]:.2f}', xy=(row['mid'], y_position), xytext=(0, 5),
                     textcoords='offset points', ha='center', fontweight='bold', color='black')

    plt.tight_layout()
    plt.savefig('../Figures/Negative Diff with Avg')






