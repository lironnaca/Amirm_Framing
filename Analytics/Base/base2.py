import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick



def find_disagreeing_csv_index(sentiment_counts, rows):
    disagreeing_csv_index = None
    for answer, count in sentiment_counts.items():
        if count != 3:
            return rows.index(answer)

def getModel(path):
    if "allen" in path:
        return 'AllenNlp'
    elif "GPT" in path:
        return 'GPT-4'
    elif "Mistral" in path:
        return "Mistral"
    else:
        return "LLAMA2"

def count_sentiment_agreements(file_paths):
    dfs = []
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        dfs.append(df)

    unanimous_count = 0
    three_out_of_four_count = 0
    tie_count = 0

    disagreement_counts = {getModel(file_path): 0 for file_path in file_paths}

    for rows in zip(*[df['Base SA'] for df in dfs]):
        sentiment_counts = Counter(rows)

        if len(sentiment_counts) == 1:
            unanimous_count += 1
        elif max(sentiment_counts.values()) == 3:
            three_out_of_four_count += 1
            disagreeing_csv_index = find_disagreeing_csv_index(sentiment_counts, rows)
            disagreeing_csv = file_paths[disagreeing_csv_index]
            disagreement_counts[getModel(disagreeing_csv)] += 1
        elif len(sentiment_counts) == 2 and max(sentiment_counts.values()) == 2:
            tie_count += 1

    print("Disagreement counts:")
    for file_path, count in disagreement_counts.items():
        print(f"{file_path}: {count} times")

    total_disagreement = sum(disagreement_counts.values())
    disagreement_percentages = {key: (value / total_disagreement) * 100 for key, value in
                                disagreement_counts.items()}
    colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue']
    plt.figure(figsize=(8, 8))
    plt.pie(disagreement_percentages.values(), labels=disagreement_percentages.keys(), autopct='%1.1f%%',
            colors=colors, shadow=True, startangle=140)
    plt.legend(disagreement_percentages.keys(), loc="best")
    plt.title('Disagreement Percentage Distribution', fontsize=14)
    plt.tight_layout()
    plt.savefig('../Figures/Modles agreement2')
    plt.show()

    return unanimous_count, three_out_of_four_count, tie_count

if __name__ == '__main__':
    disagreement_counts = {}
    file_paths = ['Advanced//combinedData_allenNLP_result_preprocessed.csv',
                  'Advanced//combinedData_GPT_result_preprocessed.csv',
                  'Advanced//combinedData_LLAMA2_result_preproccessed.csv',
                  'Advanced//combinedData_Mistral_preproccessed.csv']
    unanimous_count, three_out_of_four_count, tie_count = count_sentiment_agreements(file_paths)

    print("Number of sentences with unanimous sentiment agreement across all CSV files:", unanimous_count)
    print("Number of sentences where 3 out of 4 CSV files agreed:", three_out_of_four_count)
    print("Number of sentences where there was a tie:", tie_count)


    counts = {
        'Unanimous Agreement': unanimous_count,
        '3 out of 4 Agreements': three_out_of_four_count,
        'Ties': tie_count
    }

    colors = ['#66c2a5', '#fc8d62', '#8da0cb']
    plt.figure(figsize=(8, 8))
    explode = (0.1, 0, 0)

    wedges, texts, autotexts = plt.pie(counts.values(), labels=None, autopct='%1.1f%%', colors=colors, shadow=True,
                                       startangle=140, explode=explode)
    plt.title('Sentiment Agreement Distribution', fontsize=16)
    plt.axis('equal')

    legend_handles = [plt.Rectangle((0, 0), 1, 1, fc=color) for color in colors]
    plt.legend(legend_handles, counts.keys(), loc="best", fontsize=12)
    for text in autotexts:
        text.set_fontsize(12)

    plt.savefig('../Figures/Modles agreement1')
    plt.show()


