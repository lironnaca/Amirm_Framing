import pandas as pd

def classify_sentiment(text):
    if pd.isnull(text):
        return "neutral"
    elif 'N' in str(text).upper():
        return "negative"
    elif 'P' in str(text).upper():
        return "positive"
    else:
        return "neutral"

if __name__ == '__main__':
    original_df = pd.read_csv("../combinedData_allenNLP_result.csv")

    original_df["Base SA"] = original_df["Base SA"].apply(classify_sentiment)
    original_df["After Positive Framing SA"] = original_df["After Positive Framing SA"].apply(classify_sentiment)
    original_df["After Negative Framing SA"] = original_df["After Negative Framing SA"].apply(classify_sentiment)

    original_df.to_csv("combinedData_allenNLP_result_preprocessed.csv", index=False)
