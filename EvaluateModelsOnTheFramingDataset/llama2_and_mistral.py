from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd


def doSA(baseSentence, firstSentnece, secondSentence, chain, prompt):
    baseReply = chain.invoke({"sentence": baseSentence})
    firstReply = chain.invoke({"sentence": firstSentnece})
    secondReply = chain.invoke({"sentence": secondSentence})

    return baseReply, firstReply, secondReply


def makeTest(data):
    llm = ChatOllama(model="mistral")
    prompt = ChatPromptTemplate.from_template("Here's a sentence:\n" \
             "{sentence}.\n" \
             "Is the sentence Positive Or Negative? Write the answer as Json: " \
             "['Sentiment' : 'Positive/Negative'].")
    chain = prompt | llm | StrOutputParser()

    for index, row in data.iterrows():
        processed_sentence = doSA(row['sentence_text'], row['positive_framing'], row['negative_framing'], chain, prompt)
        data.at[index, 'Base SA'] = processed_sentence[0]
        data.at[index, 'After Positive Framing SA'] = processed_sentence[1]
        data.at[index, 'After Negative Framing SA'] = processed_sentence[2]

        data.to_csv('combinedData_Mistral.csv', index=False)


if __name__ == '__main__':
    data = pd.read_csv('combinedData_Mistral.csv')
    data['Base SA'] = data['Base SA'].astype(str)
    data['After Positive Framing SA'] = data['After Positive Framing SA'].astype(str)
    data['After Negative Framing SA'] = data['After Negative Framing SA'].astype(str)
    makeTest(data)
