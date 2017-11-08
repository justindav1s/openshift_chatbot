import csv
import pickle
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import operator

ignore_words = ['?']
nn_width = 20

def saveToCSV(list, filename):
    with open(filename, 'w') as file:
        wr = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in list:
            wr.writerow([row])

def loadFromCSV(filename):
    data = []
    with open(filename, 'r') as file:
        rdr = csv.reader(file, quoting=csv.QUOTE_MINIMAL)
        for row in rdr:
            data.append(str(row).strip())
    return data

def loadFromFile(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    return data

def convertToBag(text):
    words = []
    w = nltk.word_tokenize(text)
    words.extend(w)
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    lex = loadFromFile('chatbot/words.csv')
    bag = zeroList(len(lex))
    for word in words:
        if word in lex:
            #print(word, ' : ', lex.index(word))
            bag[lex.index(word)] = 1
    return bag

def zeroList(length):
    zeros = []
    for i in range(length):
        zeros.append(0)
    return zeros

def predictThis(model, sentence):
    classes = loadFromFile('chatbot/classes.csv')
    bag = convertToBag(sentence)
    bags = []
    bags.append(bag)
    preds = model.predict(bags)
    for i in range(len(preds)):
        index, value = max(enumerate(preds[i]), key=operator.itemgetter(1))
        print(sentence, ' : ', classes[index] , ' : ', (value*100), '%')

    return classes[index], int(value)
