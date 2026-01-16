
import re
import random
from collections import defaultdict


with open("test_text.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

sentences = re.split(r"[.!?]", text)

corpus = []
for s in sentences:
    s = re.sub(r"[^a-z0-9\s]", "", s).strip()
    if not s:
        continue
    corpus.extend(["<s>", "<s>"] + s.split() + ["</s>"])


N = 4
ngram_counts = defaultdict(lambda: defaultdict(int))

for i in range(len(corpus) - N + 1):
    context = tuple(corpus[i:i+N-1])
    target = corpus[i+N-1]
    ngram_counts[context][target] += 1

def retrain_model_from_text(raw_text):
    global ngram_counts

    text = raw_text.lower()
    sentences = re.split(r"[.!?]", text)

    corpus = []
    for s in sentences:
        s = re.sub(r"[^a-z0-9\s]", "", s).strip()
        if not s:
            continue
        corpus.extend(["<s>", "<s>"] + s.split() + ["</s>"])

    ngram_counts = defaultdict(lambda: defaultdict(int))

    for i in range(len(corpus) - N + 1):
        context = tuple(corpus[i:i + N - 1])
        target = corpus[i + N - 1]
        ngram_counts[context][target] += 1



def sample(probs, temperature=0.7):
    words, weights = zip(*probs.items())
    weights = [w ** (1 / temperature) for w in weights]
    total = sum(weights)
    weights = [w / total for w in weights]
    return random.choices(words, weights)[0]


def predict_next(tokens, temperature=0.7):
    for n in range(N, 0, -1):
        if len(tokens) >= n - 1:
            context = tuple(tokens[-(n-1):])
            if context in ngram_counts:
                return sample(ngram_counts[context], temperature)

    return "</s>"


def complete_sentence(seed, max_words=20, temperature=0.7):
    tokens = ["<s>", "<s>"] + seed.lower().split()

    for _ in range(max_words):
        word = predict_next(tokens, temperature)
        if word == "</s>":
            break
        tokens.append(word)

    return " ".join(tokens[2:])

# print(complete_sentence("the system is ", temperature=0.3))
# print(complete_sentence("the system is ", temperature=0.7))
# print(complete_sentence("the system is ", temperature=1.0))

