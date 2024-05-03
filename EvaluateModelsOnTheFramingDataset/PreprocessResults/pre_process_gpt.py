import pandas as pd


def classify_sentiment(text):
    if pd.isnull(text):
        return "neutral"
    elif "negative" in str(text).lower():
        return "negative"
    elif "positive" in str(text).lower():
        return "positive"
    else:
        return "neutral"


if __name__ == '__main__':
    original_df = pd.read_csv("../combinedData_GPT_result.csv")

    original_df["Base SA"] = original_df["Base SA"].apply(classify_sentiment)
    original_df["After Positive Framing SA"] = original_df["After Positive Framing SA"].apply(classify_sentiment)
    original_df["After Negative Framing SA"] = original_df["After Negative Framing SA"].apply(classify_sentiment)

    original_df.to_csv("combinedData_GPT_result_preprocessed.csv", index=False)
