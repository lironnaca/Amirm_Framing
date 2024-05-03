from allennlp.predictors.predictor import Predictor
import pandas as pd

def doSAallenNLP(baseSentence, firstSentnece, secondSentence, predictor):
    result = predictor.predict(baseSentence)
    if result['probs'][1] > result['probs'][0]:
        baseReply = 'Negative'
    else:
        baseReply = 'Positive'

    result = predictor.predict(firstSentnece)
    if result['probs'][1] > result['probs'][0]:
        firstReply = 'Negative'
    else:
        firstReply = 'Positive'

    result = predictor.predict(secondSentence)
    if result['probs'][1] > result['probs'][0]:
        secondReply = 'Negative'
    else:
        secondReply = 'Positive'

    return baseReply, firstReply, secondReply


def makeTest(data):
    predictor = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/stanford-sentiment-treebank-roberta.2021-03-11.tar.gz")

    for index, row in data.iterrows():
        print(index)
        processed_sentence = doSAallenNLP(row['sentence_text'], row['positive_framing'], row['negative_framing'],
                                          predictor)
        data.at[index, 'Base SA'] = processed_sentence[0][0]
        data.at[index, 'After Positive Framing SA'] = processed_sentence[1][0]
        data.at[index, 'After Negative Framing SA'] = processed_sentence[2][0]

        data.to_csv('combinedData_allenNLP_result.csv', index=False)


if __name__ == '__main__':
    data = pd.read_csv('combinedData_allenNLP_result.csv')
    data['Base SA'] = data['Base SA'].astype(str)
    data['After Positive Framing SA'] = data['After Positive Framing SA'].astype(str)
    data['After Negative Framing SA'] = data['After Negative Framing SA'].astype(str)
    makeTest(data)
