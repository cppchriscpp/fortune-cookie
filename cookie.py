import markovify
import re
import nltk
import os
import urllib.request

from shutil import copyfile

# TODO: Should this be somewhere else?
nltk.download('averaged_perceptron_tagger')

class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

with open("./fortune-cookies-galore/fortunes.txt") as f:
    text = f.read()

response = urllib.request.urlopen("https://www.usconstitution.net/const.txt")
data = response.read()
tswext = data.decode('utf-8')

tooxt = text.split("\n")
tswooxt = tswext.split("\n")

def excluded(string):
    if string.startswith("Q:"):
        return False
    if "\"" in string:
        return False
    if "--" in string:
        return False
    return True

def exwifted(string):
    if "[" in string:
        return False
    return True

# There's some non-fortunes in our fortune source.. let's strip those
tooxt[:] = [x for x in tooxt if excluded(x)]
tswooxt[:] = [x for x in tswooxt if exwifted(x)]

text_model = POSifiedText("\n".join(tooxt))
tswext_model = POSifiedText("\n".join(tswooxt))

moodel = markovify.combine([text_model, tswext_model])

print("Long:")
for i in range(5):
    print(moodel.make_sentence(tries=25))

print("")

print("tweeter:")
for i in range(5):
    print(moodel.make_short_sentence(140, tresi=25))

if not os.path.exists('./temp'):
    os.mkdir('./temp')

with open("./temp/cookie.js", "w+") as file:
    file.write("window.fortuneCookies=[\n")
    for i in range(100):
        file.write("\"" + moodel.make_sentence(tries=25) + "\",\n")
    file.write("];")

copyfile("./temp/cookie.js", "/data/cookie.js")
