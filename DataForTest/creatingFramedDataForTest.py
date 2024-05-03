
import pandas as pd
import openai
import sys
# from langchain.chains import LLMChain
# from langchain.llms.openai import OpenAI

PROMPTS = [
    ["Here is a sentence: <sentence>.\n"
     "You are not allowed to change this sentence. Add a positive suffix.",

     "Here is a sentence: <sentence>.\n"
     "You are not allowed to change this sentence. Add a positive prefix.",

     "The framing effect is a cognitive bias in which people decide between options based on whether the options are "
     "presented with positive or negative connotations.\n "
     "Here is a sentence: <sentence>.\n"
     "You are not allowed to change this sentence. Add a positive framing.",

     "Here is an example of a base sentence with a positive sentiment:\n"
     "I got an A on my math test.\n"
     "Here is the same sentence, after adding a positive framing:\n"
     "I got an A on my math test. I feel like I earned it, as I worked very hard to get it.\n"
     "Here is a positive sentence: <sentence>.\n"
     "Like the example, add a positive suffix or prefix to it. Don't change the original sentence."
     ],
    ["Here is a sentence: <sentence>.\n"
     "You are not allowed to change this sentence. Add a negative suffix.",

     "Here is a sentence: <sentence>.\n"
     "You are not allowed to change this sentence. Add a negative prefix.",

     "The framing effect is a cognitive bias in which people decide between options based on whether the options are "
     "presented with positive or negative connotations\n. "
     "Here is a sentence: <sentence>.\n"
     "You are not allowed to change this sentence. Add a negative framing.",

     "Here is an example of a base sentence with a positive sentiment:\n"
     "I got an A on my math test.\n"
     "Here is the same sentence, after adding a negative framing:\n"
     "I got an A on my math test. I think I spent too much time learning to it though.\n"
     "Here is a positive sentence: <sentence>.\n"
     "Like the example, add a negative suffix or prefix to it. Don't change the original sentence."
     ],
    [
        "Here is a sentence: <sentence>.\n"
        "You are not allowed to change this sentence. Add a positive suffix.",

        "Here is a sentence: <sentence>.\n"
        "You are not allowed to change this sentence. Add a positive prefix.",

        "The framing effect is a cognitive bias in which people decide between options based on whether the options are "
        "presented with positive or negative connotations.\n "
        "Here is a sentence: <sentence>.\n"
        "You are not allowed to change this sentence. Add a positive framing.",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I failed my math test today, however I see it as an opportunity to learn and improve in the future.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.\n"
    ],
    [
        "Here is a sentence: <sentence>.\n"
        "You are not allowed to change this sentence. Add a negative suffix.",

        "Here is a sentence: <sentence>.\n"
        "You are not allowed to change this sentence. Add a negative prefix.",

        "The framing effect is a cognitive bias in which people decide between options based on whether the options are "
        "presented with positive or negative connotations\n. "
        "Here is a sentence: <sentence>.\n"
        "You are not allowed to change this sentence. Add a negative framing.",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I failed my math test today and I feel like a failure.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.\n"
    ],
]

PROMPTS_FOR_SECOND_TEST = [
    [
        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I'm so happy! I got an A on my math test.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.",

        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I got an A on my math test. I'm proud of myself.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.",

        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I got an A on my math test. I feel like I earned it, as I worked very hard to get it.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.",

        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Let's add a positive framing to this sentence:\n"
        "First, we will start with the original sentence:\n"
        "I got an A on my math test.\n"
        "Now, we will chose words with positive sentiment, and create a sentence, that when"
        "we put it after the original sentence, will make the original sentence even more positive:\n"
        "I feel like I earned it, as I worked very hard to get it."
        "Combine the two sentences together and receive:\n"
        "I got an A on my math test. I feel like I earned it, as I worked very hard to get it.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence."
    ],
    [
        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I got an A on my math test. However, I think that I can do better.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.",

        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I'm disappointed in myself. I got an A on my math test. I wanted A+.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.",

        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I got an A on my math test. I think I spent too much time learning to it though.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.",

        "Here is an example of a base sentence with a positive sentiment:\n"
        "I got an A on my math test.\n"
        "Let's add a negative framing to the sentence.\n"
        "First, we will start with the original sentence:\n"
        "I got an A on my math test.\n"
        "Now, we will chose words with negative sentiment, and create a sentence, that when"
        "we put it after the original sentence, will make the original sentence negative:\n"
        "I think I spent too much time learning to it though.\n"
        "Combine the two sentences together and receive:\n"
        "I got an A on my math test. I think I spent too much time learning to it though.\n"
        "Here is a positive sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence."
    ],
    [
        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I won't give up, even though I failed my math test today.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.\n",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I failed my math test today, but got an amazing job offer.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.\n",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a positive framing:\n"
        "I failed my math test today, however I see it as an opportunity to learn and improve in the future.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.\n",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Let's add a positive framing to this sentence.\n"
        "First, we will start with the original sentence:\n"
        "I failed my math test today.\n"
        "Now, we will choose words with positive sentiment, and create a sentence, that when"
        "we put it after the original sentence, we will make the sentence positive:\n"
        "I see it as an opportunity to learn and improve in the future.\n"
        "Combine the two sentences together and receive:\n"
        "I failed my math test today, however I see it as an opportunity to learn and improve in the future.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a positive suffix or prefix to it. Don't change the original sentence.\n"
    ],
    [
        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I feel like a failure, I failed my math test today.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.\n",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I have put so much effort and time, but still I failed my math test today.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.\n",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Here is the same sentence, after adding a negative framing:\n"
        "I failed my math test today and I feel like a failure.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.\n",

        "Here is an example of a base sentence with a negative sentiment:\n"
        "I failed my math test today.\n"
        "Let's add a negative framing to the sentence.\n"
        "First, we will start with the original sentence:\n"
        "I failed my math test today.\n"
        "Now, we will choose words with negative sentiment, and create a sentence, that when"
        "we put in after the original sentence, will make the original sentence even more negative:\n"
        "I feel like a failure.\n"
        "Combine the two sentences together and receive:\n"
        "I failed my math test today and I feel like a failure.\n"
        "Here is a negative sentence: <sentence>.\n"
        "Like the example, add a negative suffix or prefix to it. Don't change the original sentence.\n"
    ],
]


def makeFraming(client, sentence, prompt):
    prompt = prompt.replace("<sentence>", sentence)
    dic = [{"role": "user", "content": prompt}]
    chat = client.chat.completions.create(model="gpt-4", messages=dic)
    return chat.choices[0].message.content.split("\n")
    # llm_chain = LLMChain(llm=client)
    # llm_chain.run(prompt)


def makeTestData(client, final_df, sentiment, i):
    sentences = []
    first_results = []
    second_results = []
    third_results = []
    fourth_results = []
    is_first_best = [None]
    is_second_best = [None]
    is_third_best = [None]
    is_forth_best = [None]

    for sentence in final_df[final_df['label'] == sentiment]['sentence']:
        sentences.append(sentence)
        for index, prompt in enumerate(PROMPTS_FOR_THIRD_TEST[i]):
            print("prompt is: " + prompt)
            result_str = makeFraming(client, sentence, prompt)
            if index == 0:
                first_results.append(result_str)
            elif index == 1:
                second_results.append(result_str)
            elif index == 2:
                third_results.append(result_str)
            elif index == 3:
                fourth_results.append(result_str)
        print("done with sentence:" + sentence)

    combined_result_df = pd.DataFrame({
        'Sentence': sentences,
        'First': first_results,
        'Second': second_results,
        'Third': third_results,
        'Fourth': fourth_results,
        "isFirst": is_first_best * len(sentences),
        "isSecond": is_second_best * len(sentences),
        "isThird": is_third_best * len(sentences),
        "isForth": is_forth_best * len(sentences)
    })

    combined_result_df.to_csv(sentiment + str(i) + '.csv', index=False)


if __name__ == '__main__':
    final_df = pd.read_csv('testData.csv')
    client = openai.Client(api_key=sys.argv[1])
    # client = OpenAI(model_name="gpt-4")

    makeTestData(client, final_df, "positive", 0)
    # makeTestData(client, final_df, "positive", 1)
    # makeTestData(client, final_df, "negative", 2)
    # makeTestData(client, final_df, "negative", 3)


