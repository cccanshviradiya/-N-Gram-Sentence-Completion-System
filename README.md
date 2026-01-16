# 🧠 N-Gram Sentence Completion System

A simple **N-gram based sentence completion system** built from scratch using **Python** and deployed with **Streamlit**.  
This project demonstrates how statistical language models work without using any machine learning libraries.

---

## 📌 Project Overview

This application predicts the next words of a sentence based on previously seen word sequences from a training text file.  
It uses a **4-gram language model** with **backoff strategy** and **temperature-based sampling**.

Users can:
- Upload a custom training text file
- Enter a seed sentence
- Generate sentence completions interactively

---

## 🎯 Objectives

- Implement an N-gram language model from scratch
- Understand statistical text generation
- Apply backoff and sampling strategies
- Build a simple NLP web application using Streamlit

---

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Regular Expressions (`re`)
- `collections.defaultdict`
- Random Sampling

---

## 📂 Project Structure






---

## 📄 Dataset

- Input data is a plain text (`.txt`) file
- Default dataset: `test_text.txt`
- Users can upload their own text file through the UI

### Preprocessing Steps:
1. Convert text to lowercase
2. Split into sentences
3. Remove special characters
4. Add `<s>` (start) and `</s>` (end) tokens

---

## 🧩 Model Details

- **Model Type:** Statistical Language Model
- **N-Gram Size:** 4 (4-gram)
- **Context Length:** Previous 3 words
- **Vocabulary:** Extracted from training corpus
- **Prediction Method:** Backoff + sampling

---

## 🔄 Backoff Strategy

If a 4-gram context is not found:
- Fall back to 3-gram
- Then 2-gram
- Then 1-gram
- Stop generation if no match is found

---

## 🎛️ Temperature Sampling

Temperature controls randomness in word selection:

| Temperature | Effect |
|------------|-------|
| Low (0.3) | More deterministic |
| Medium (0.7) | Balanced |
| High (1.2+) | More creative/random |

---

## 🌐 Streamlit Interface

### Features:
- File upload (`.txt`)
- Seed sentence input
- Temperature control
- Maximum word limit
- Vocabulary size display

---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install streamlit


