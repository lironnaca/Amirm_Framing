import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('../Advanced/combinedData_Mistral_preproccessed.csv')

    total_sentences = df.shape[0]

    # 1. Negative answer, Negative Base SA
    neg_neg = df[(df['answer'].str.lower().str.contains('negative')) & (
        df['Base SA'].str.lower().str.contains('negative'))].shape[0]
    percent_neg_neg = (neg_neg / total_sentences) * 100

    # 2. Negative answer, Positive Base SA
    neg_pos = df[(df['answer'].str.lower().str.contains('negative')) & (
        df['Base SA'].str.lower().str.contains('positive'))].shape[0]
    percent_neg_pos = (neg_pos / total_sentences) * 100

    # 3. Negative answer, Neutral Base SA
    neg_neutral = \
    df[(df['answer'].str.lower().str.contains('negative')) & (df['Base SA'].str.lower().str.contains('neutral'))].shape[
        0]
    percent_neg_neutral = (neg_neutral / total_sentences) * 100

    # 4. Positive answer, Negative Base SA
    pos_neg = df[(df['answer'].str.lower().str.contains('positive')) & (
        df['Base SA'].str.lower().str.contains('negative'))].shape[0]
    percent_pos_neg = (pos_neg / total_sentences) * 100

    # 5. Positive answer, Positive Base SA
    pos_pos = df[(df['answer'].str.lower().str.contains('positive')) & (
        df['Base SA'].str.lower().str.contains('positive'))].shape[0]
    percent_pos_pos = (pos_pos / total_sentences) * 100

    # 6. Positive answer, Neutral Base SA
    pos_neutral = \
    df[(df['answer'].str.lower().str.contains('positive')) & (df['Base SA'].str.lower().str.contains('neutral'))].shape[
        0]
    percent_pos_neutral = (pos_neutral / total_sentences) * 100



    # 7. Negative Base SA, Negative After Positive Framing SA
    base_neg_neg = df[(df['Base SA'].str.lower().str.contains('negative')) & (
        df['After Positive Framing SA'].str.lower().str.contains('negative'))].shape[0]
    percent_base_neg_neg = (base_neg_neg / total_sentences) * 100

    # 8. Negative Base SA, Positive After Positive Framing SA
    base_neg_pos = df[(df['Base SA'].str.lower().str.contains('negative')) & (
        df['After Positive Framing SA'].str.lower().str.contains('positive'))].shape[0]
    percent_base_neg_pos = (base_neg_pos / total_sentences) * 100

    # 9. Negative Base SA, Neutral After Positive Framing SA
    base_neg_neutral = df[(df['Base SA'].str.lower().str.contains('negative')) & (
        df['After Positive Framing SA'].str.lower().str.contains('neutral'))].shape[0]
    percent_base_neg_neutral = (base_neg_neutral / total_sentences) * 100

    # 10. Positive Base SA, Negative After Positive Framing SA
    base_pos_neg = df[(df['Base SA'].str.lower().str.contains('positive')) & (
        df['After Negative Framing SA'].str.lower().str.contains('negative'))].shape[0]
    percent_base_pos_neg = (base_pos_neg / total_sentences) * 100

    # 11. Positive Base SA, Positive After Positive Framing SA
    base_pos_pos = df[(df['Base SA'].str.lower().str.contains('positive')) & (
        df['After Negative Framing SA'].str.lower().str.contains('positive'))].shape[0]
    percent_base_pos_pos = (base_pos_pos / total_sentences) * 100

    # 12. Positive Base SA, Neutral After Positive Framing SA
    base_pos_neutral = df[(df['Base SA'].str.lower().str.contains('positive')) & (
        df['After Negative Framing SA'].str.lower().str.contains('neutral'))].shape[0]
    percent_base_pos_neutral = (base_pos_neutral / total_sentences) * 100

    print("first table:")
    print("1. Negative answer, Negative Base SA:", neg_neg, "(", round(percent_neg_neg, 2), "%)")
    print("2. Negative answer, Positive Base SA:", neg_pos, "(", round(percent_neg_pos, 2), "%)")
    print("3. Negative answer, Neutral Base SA:", neg_neutral, "(", round(percent_neg_neutral, 2), "%)")
    print("4. Positive answer, Negative Base SA:", pos_neg, "(", round(percent_pos_neg, 2), "%)")
    print("5. Positive answer, Positive Base SA:", pos_pos, "(", round(percent_pos_pos, 2), "%)")
    print("6. Positive answer, Neutral Base SA:", pos_neutral, "(", round(percent_pos_neutral, 2), "%)")

    print("second table:")
    print("7. Negative Base SA, Negative After Positive Framing SA:", base_neg_neg, "(", round(percent_base_neg_neg, 2),
          "%)")
    print("8. Negative Base SA, Positive After Positive Framing SA:", base_neg_pos, "(", round(percent_base_neg_pos, 2),
          "%)")
    print("9. Negative Base SA, Neutral After Positive Framing SA:", base_neg_neutral, "(",
          round(percent_base_neg_neutral, 2), "%)")
    print("10. Positive Base SA, Negative After Positive Framing SA:", base_pos_neg, "(",
          round(percent_base_pos_neg, 2), "%)")
    print("11. Positive Base SA, Positive After Positive Framing SA:", base_pos_pos, "(",
          round(percent_base_pos_pos, 2), "%)")
    print("12. Positive Base SA, Neutral After Positive Framing SA:", base_pos_neutral, "(",
          round(percent_base_pos_neutral, 2), "%)")






