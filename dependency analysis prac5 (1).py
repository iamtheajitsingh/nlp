from collections import defaultdict, Counter

corpus = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "AI", "</s>"],
    ["<s>", "NLP", "loves", "me", "</s>"]
]

# Unigram counts
unigrams = Counter(word for sent in corpus for word in sent)
N = sum(unigrams.values())
V = len(unigrams)

# Bigram counts
bigrams = defaultdict(int)
for sent in corpus:
    for i in range(len(sent)-1):
        bigrams[(sent[i], sent[i+1])] += 1

def unigram_prob(word):
    return (unigrams[word] + 1) / (N + V)

def bigram_prob(w1, w2):
    return (bigrams[(w1, w2)] + 1) / (unigrams[w1] + V)

def sentence_prob_unigram(sentence):
    prob = 1.0
    for w in sentence[1:]:  # skip <s>
        prob *= unigram_prob(w)
    return prob

def sentence_prob_bigram(sentence):
    prob = 1.0
    for i in range(len(sentence)-1):
        prob *= bigram_prob(sentence[i], sentence[i+1])
    return prob

sentence = ["<s>", "I", "love", "NLP", "</s>"]

print(sentence_prob_unigram(sentence))
print(sentence_prob_bigram(sentence))