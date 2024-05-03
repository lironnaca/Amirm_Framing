from datasets import load_dataset
import random
from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging

if __name__ == '__main__':
    data = load_dataset("cc_news")

    predictor = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/stanford-sentiment-treebank-roberta.2021-03-11.tar.gz")
    dataset = []
    for sample in data["train"]:
        sentences = (sample["text"].replace('\n', "")).split(".")
        for sentence in sentences:
            if len(sentence) < 5:
                continue
            result = predictor.predict(sentence)
            if result['probs'][0] > 0.7 and result['probs'][1] > 0.1 or result['probs'][0] > 0.1 and result['probs'][
                1] > 0.7:
                print(f"sentence is: {sentence}, label: {result['label']}, probs: {result['probs']}")
                dataset.append([sentence, result['label'], result['probs']])


