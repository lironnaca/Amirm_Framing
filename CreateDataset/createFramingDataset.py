import sys

import pandas as pd
from openai import Client

PROMPTS = [
     "Here is an example of a base sentence with a negative sentiment:"
     "I failed my math test today."
     "Here is the same sentence, after adding a positive framing:"
     "I failed my math test today, however I see it as an opportunity to learn and improve in the future."
     "Here is a negative sentence: <sentence>"
     "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.",

    "Here is an example of a base sentence with a negative sentiment:"
    "I failed my math test today."
    "Here is the same sentence, after adding a negative framing:"
    "I failed my math test today and I feel like a failure."
    "Here is a negative sentence: <sentence>."
    "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.",

    "Here is an example of a base sentence with a positive sentiment:"
    "I got an A on my math test."
    "Here is the same sentence, after adding a positive framing:"
    "I got an A on my math test. I feel like I earned it, as I worked very hard to get it."
    "Here is a positive sentence: <sentence>."
    "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.",

    "Here is an example of a base sentence with a positive sentiment:"
    "I got an A on my math test."
    "Here is the same sentence, after adding a negative framing:"
    "I got an A on my math test. I think I spent too much time learning to it though."
    "Here is a positive sentence: <sentence>."
    "Like the example, add a negative suffix or prefix to it. Don't change the original sentence."
]


def makeFraming(client, prompt):
    dic = [{"role": "user", "content": prompt}]
    chat = client.chat.completions.create(model="gpt-4-0613", messages=dic)
    return chat.choices[0].message.content.split("\n")


def makeFramingForPositiveSentnece(client, df, sentence):
    #positive framing
    prompt = PROMPTS[2].replace("<sentence>", sentence)
    df.loc[df['sentence_text'] == sentence, 'positive_framing'] = makeFraming(client, prompt)
    df.to_csv('combinedData.csv', index=False)


   # negative framing
    prompt = PROMPTS[3].replace("<sentence>", sentence)
    df.loc[df['sentence_text'] == sentence, 'negative_framing'] = makeFraming(client, prompt)
    df.to_csv('combinedData.csv', index=False)


def makeFramingForNegativeSentnece(client, df, sentence):
    # positive framing
    prompt = PROMPTS[0].replace("<sentence>", sentence)
    df.loc[df['sentence_text'] == sentence, 'positive_framing'] = makeFraming(client, prompt)
    df.to_csv('combinedData.csv', index=False)


    # negative framing
    prompt = PROMPTS[1].replace("<sentence>", sentence)
    df.loc[df['sentence_text'] == sentence, 'negative_framing'] = makeFraming(client, prompt)
    df.to_csv('combinedData.csv', index=False)



if __name__ == '__main__':
    client = Client(api_key= sys.argv[1])
    data = pd.read_csv('combinedData.csv')

    for index, row in data.iterrows():
        if (index < 2142):
            continue
        print(index)
        if row['answer'] == 'positive':
            makeFramingForPositiveSentnece(client, data, row['sentence_text'])
        elif row['answer'] == 'negative':
            makeFramingForNegativeSentnece(client, data, row['sentence_text'])


