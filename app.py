import streamlit as st
import re
import random
from collections import defaultdict


@st.cache_data
def load_corpus_from_text(text):
    text = text.lower()
    sentences = re.split(r"[.!?]", text)

    corpus = []
    for s in sentences:
        s = re.sub(r"[^a-z0-9\s]", "", s).strip()
        if not s:
            continue
        corpus.extend(["<s>", "<s>"] + s.split() + ["</s>"])

    return corpus


@st.cache_data
def load_corpus_from_file():
    with open("test_text.txt", "r", encoding="utf-8") as f:
        return load_corpus_from_text(f.read())



uploaded_file = st.file_uploader("Upload training text (.txt)", type=["txt"])

if uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")
    corpus = load_corpus_from_text(raw_text)
else:
    corpus = load_corpus_from_file()

VOCAB = set(corpus)
V = len(VOCAB)
N = 4  # 4-gram model

st.title("N-gram Sentence Completion")
st.write("Vocabulary size:", V)


def inner_dict():
    return defaultdict(int)

def build_ngram(corpus):
    ngram_counts = defaultdict(inner_dict)

    for i in range(len(corpus) - N + 1):
        context = tuple(corpus[i:i + N - 1])
        target = corpus[i + N - 1]
        ngram_counts[context][target] += 1

    return ngram_counts


ngram_counts = build_ngram(corpus)


def sample(probs, temperature=0.7):
    words, weights = zip(*probs.items())
    weights = [w ** (1 / temperature) for w in weights]
    total = sum(weights)
    weights = [w / total for w in weights]
    return random.choices(words, weights)[0]


def predict_next(tokens, temperature=0.7):
    for n in range(N, 0, -1):
        if len(tokens) >= n - 1:
            context = tuple(tokens[-(n - 1):])
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


seed = st.text_input("Seed text", placeholder="Enter sentence")
temperature = st.slider("Temperature", 0.1, 1.5, 0.7)
max_words = st.slider("Max words", 1, 20, 10)

if st.button("Generate"):
    result = complete_sentence(seed, max_words, temperature)
    st.write(result)


