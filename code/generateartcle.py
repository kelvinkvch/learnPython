from urllib.request import urlopen
from random import randint


def wordlistsum(wordlist):
    sum = 0
    for word, value in wordlist.items():
        sum += value
    return sum


def retrieverandomword(wordlist):
    randindex = randint(1, wordlistsum(wordlist))
    for word, value in wordlist.items():
        randindex -= value
        if randindex <= 0:
            return word


def buildworddict(text):
    #剔除换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('"', '')
    #保证每个标点符号都和前面的单词在一起
    #这样不会被剔除,保留在马尔可夫链中
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' '+symbol+' ')
    words = text.split(' ')
    #过滤空单词
    words = [word for word in words if word != '']
    worddict = {}
    for i in range(1, len(words)):
        if words[i-1] not in worddict:
            #为单词新建一个词典
            worddict[words[i-1]] = {}
        if words[i] not in worddict[words[i-1]]:
            worddict[words[i-1]][words[i]]=0
        worddict[words[i-1]][words[i]] = worddict[words[i-1]][words[i]]+1
    return worddict


text = str(urlopen(
    'http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf8')
worddict = buildworddict(text)
length = 80
chain = ''
currentword = 'I'
for i in range(0, length):
    chain += currentword+' '
    currentword = retrieverandomword(worddict[currentword])
print(chain+'.')
