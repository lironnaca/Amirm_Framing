import openai
import time
from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
import random
import sys

if __name__ == '__main__':
    chapterList = ["1.1.txt"]
    # , "1.2.txt",
    #                "2.1.txt","2.2.txt",
    #                "3.1.txt", "3.2.txt",
    #                "4.1.txt", "4.2.txt", "4.3.txt",
    #                "5.1.txt", "5.2.txt", "5.3.txt", "5.4.txt",
    #                "6.1.txt", "6.2.txt",
    #                "7.1.txt", "7.2.txt",
    #                "8.1.txt", "8.2.txt",
    #                "9.1.txt",
    #                "10.1.txt", "10.2.txt", "10.3.txt",
    #                "11.1.txt", "11.2.txt", "11.3.txt",
    #                "12.1.txt", "12.2.txt", "12.3.txt", "12.4.txt",
    #                "13.1.txt", "13.2.txt",
    #                "14.1.txt", "14.2.txt",
    #                "15.1.txt",
    #                "16.1.txt",
    #                "17.1.txt",
    #                "18.1.txt",
    #                "19.1.txt",
    #                "20.1.txt",
    #                "21.1.txt",
    #                "22.1.txt", "22.2.txt",
    #                "23.1.txt", "23.2.txt",
    #                "24.1.txt",
    #                "25.1.txt", "25.2.txt"]
    openai.api_key = sys.argv[1]
    positive = []
    negative = []
    for chapter in chapterList:
        time.sleep(21)
        text = open(chapter, "r").read()
        message = "Here's a chapter from a book. Give me all the sentences with a negative sentiment:" + text
        dic = [{"role": "user", "content": message}]
        chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=dic)
        reply = chat.choices[0].message.content.split("\n")
        negative += reply



    predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/stanford-sentiment-treebank-roberta.2021-03-11.tar.gz")

    text = open("1.1.txt", "r").read()
    sentences = text.split(".")
    randomIndices = []
    while len(randomIndices) < 100:
      x = random.randint(0, len(sentences)-1)
      if x not in randomIndices:
        randomIndices.append(x)

    for i in randomIndices:
      print(sentences[i])
      print("\n")