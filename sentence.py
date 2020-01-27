import random

VOWELS = ["a", "e", "i", "o", "u"]
DETERMINERS = ["the", "this", "that", "my", "your", "his", "her", "its", "our", "their", "one", "each", "every", "another"] 
C_CONJ = ["and", "but", "for", "or", "so", "yet"]

with open("grammar/verbs.txt") as verbfile:
    VERBS = [line.strip() for line in verbfile]

with open("grammar/nouns.txt") as nounfile:
    NOUNS = [line.strip() for line in nounfile]

with open("grammar/adverbs.txt") as adverbfile:
    ADVERBS = [line.strip() for line in adverbfile]

with open("grammar/adjectives.txt") as adjectivefile:
    ADJECTIVES = [line.strip() for line in adjectivefile]

"""

WORDS START

"""
def Noun():
    return random.choice(NOUNS)
def Verbs():
    return random.choice(VERBS)
def Adverbs():
    return random.choice(ADVERBS)
def Adjectives():
    return random.choice(ADJECTIVES)

"""

WORDS END

"""


"""

PHRASE START

"""

def getAdj(num_adj):
    li = [Adjectives() for i in range(num_adj)]
    return li

def getAdv(num_adv):
    li = [Adverbs() for i in range(num_adv)]
    return li    

def getDet():
    return [random.choice(DETERMINERS)]

def nounPhrase():
    NP = [Noun()]
    num_adj = random.randrange(0,3)
    num_adv = random.randrange(0,2) if num_adj else 0
    NP = getAdj(num_adj) + NP
    NP = getAdv(num_adv) + NP
    if random.random() < 0.5:
        NP = getDet() + NP
    return NP

def verbPhrase():
    VP = [Verbs()]
    num_adv = random.randrange(0,2)
    
    if random.random() < 0.5:
        VP += nounPhrase()
    VP += getAdv(num_adv)
    return VP

"""

PHRASE END

"""

def Sentence():
    NP = nounPhrase()
    VP = verbPhrase()
    s = NP + VP
    if random.random() < 0.30 :
        s2 = Sentence()
        conjunction = random.choice(C_CONJ)
        s += [conjunction]
        s += s2
    return s

if __name__ == '__main__':
    content = Sentence()
    content = " ".join(content) + "."
    print(content)