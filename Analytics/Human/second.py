import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('firstBatchComparison.csv')
    df['human tag'] = df['human tag'].str.lower()
    total_rows = len(df)

    matching_rows_AllenNlp = len(df[df['human tag'] == df['AllenNLP']]) / total_rows * 100
    matching_rows_GPT4 = len(df[df['human tag'] == df['GPT4']]) / total_rows * 100
    matching_rows_Llama2 = len(df[df['human tag'] == df['LLAMA2']]) / total_rows * 100
    matching_rows_Mistral = len(df[df['human tag'] == df['Mistral']]) / total_rows * 100

    labels = ['AllenNLP', 'GPT4', 'Llama2', 'Mistral']
    counts = [matching_rows_AllenNlp, matching_rows_GPT4, matching_rows_Llama2, matching_rows_Mistral]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, counts, color=['#aec7e8', '#ffbb78', '#98df8a', '#ff9896'])
    plt.title('Agreement of Human Tags with LLM Tags')
    plt.xlabel('Model')
    plt.xticks(rotation=45)
    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
    plt.tight_layout()

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}%', ha='center', va='bottom')

    plt.savefig('../Figures/human and llm.png')
    plt.show()
