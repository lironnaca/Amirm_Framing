import random
if __name__ == '__main__':
  text = open("nyt.txt", "r").read()
  sentences = text.split(".")
  randomIndices = []
  while len(randomIndices) < min(len(sentences),100):
    x = random.randint(0, len(sentences)-1)
    if x not in randomIndices:
      randomIndices.append(x)

  for i in randomIndices:
    print(sentences[i])
    print("\n")