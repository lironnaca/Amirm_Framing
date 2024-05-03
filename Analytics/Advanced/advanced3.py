import pandas as pd
import matplotlib.pyplot as plt
import ast
import numpy as np

def convert_to_list(s):
    return ast.literal_eval(s)

def add_jitter(values, jitter_amount=0.01):
    return values + np.random.normal(0, jitter_amount, size=len(values))


if __name__ == '__main__':
    df = pd.read_csv('combinedData_GPT_result_preprocessed.csv')

    df['Base Sentence Score'] = df['Base Sentence Score'].apply(convert_to_list)
    df['After Positive Framing Sentence Score'] = df['After Positive Framing Sentence Score'].apply(convert_to_list)
    df['After Negative Framing Sentence Score'] = df['After Negative Framing Sentence Score'].apply(convert_to_list)

    fig, ax = plt.subplots(figsize=(12, 6))

    x_values_pos = add_jitter([float(score[0]) for score in df['Base Sentence Score']])
    y_values_pos = add_jitter([float(score[0]) for score in df['After Positive Framing Sentence Score']])
    ax.scatter(x_values_pos, y_values_pos, alpha=0.5, color='green', label='Positive Scores')

    x_values_neg = add_jitter([float(score[1]) for score in df['Base Sentence Score']])
    y_values_neg = add_jitter([float(score[1]) for score in df['After Negative Framing Sentence Score']])
    ax.scatter(x_values_neg, y_values_neg, alpha=0.5, color='red', label='Negative Scores')

    combined_x_values = np.concatenate([x_values_pos, x_values_neg])
    ax.plot([min(combined_x_values), max(combined_x_values)], [min(combined_x_values), max(combined_x_values)], 'b--')

    ax.set_xlabel('Base SA Score')
    ax.set_ylabel('After Framing Score')
    ax.legend()

    plt.tight_layout()
    plt.savefig("../Figures/diff2")
    plt.show()