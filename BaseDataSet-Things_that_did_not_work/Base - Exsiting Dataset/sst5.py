from datasets import load_dataset
if __name__ == '__main__':
    dataset = load_dataset("SetFit/sst5")["train"].select(range(4000))
    wordsCount = {}  # negative and then positive
    for sample in dataset:
        wordsInSample = sample["text"].split()
        if sample["label"] == 0: #very negative
            for word in wordsInSample:
                if word not in wordsCount:
                    wordsCount[word] = [0, 1]
                else:
                    wordsCount[word][1] += 1
        if sample["label"] == 4: #very positive
            for word in wordsInSample:
                if word not in wordsCount:
                    wordsCount[word] = [0, 1]
                else:
                    wordsCount[word][0] += 1

    probabilityDict = {}
    wordsThatTendsNegative = {}
    wordsThatTendsPositive = {}
    for word, counts in wordsCount.items():
        negativeCount, positiveCount = counts[0], counts[1]
        negativeProb = negativeCount/(negativeCount + positiveCount)
        positiveProb = positiveCount/(negativeCount + positiveCount)
        probabilityDict[word] = (negativeProb, positiveProb)
        if negativeProb > 0.9:
            wordsThatTendsNegative[word] = negativeProb
        if positiveProb > 0.9:
            wordsThatTendsPositive[word] = positiveProb

    # print("Words that tend to relate to negative sentiment:\n")
    # for word, prob in wordsThatTendsNegative.items():
    #     print(f"{word} -> {prob}")
    #
    # print("Words that tend to relate to positive sentiment:\n")
    # for word, prob in wordsThatTendsPositive.items():
    #     print(f"{word} -> {prob}")

    newDataSet = {'text': [], 'label': []}
    for sample in dataset:
        if sample['label'] != 0 and sample['label'] != 4:
            continue
        # newSample = []
        wordsInSample = sample["text"].split()
        shouldAddFlag = 1
        for word in wordsInSample:
            if word in wordsThatTendsNegative or word in wordsThatTendsPositive:
                shouldAddFlag = 0
                continue
        if shouldAddFlag:
            newDataSet['text'].append(sample['text'])
            newDataSet['label'].append(sample['label'])

    for i, sentence in enumerate(newDataSet['text']):
        print(f"The sentence is: {sentence}")
        print(f"The label is: {newDataSet['label'][i]}")

    print(len(newDataSet["label"]))
    # compareDataSet = {}
    # for i in range(len(dataset["text"])):
    #     compareDataSet[i] = (dataset["text"][i], newDataSet["text"][i])
    #
    # for i, values in compareDataSet.items():
    #     print(f"This is the {i}th sample:")
    #     print(f"old: {values[0]}")
    #     print(f"new: {values[1]}")





