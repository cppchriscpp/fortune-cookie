import markovify
import re
import nltk
import os

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
tooxt = text.split("\n")

def excluded(string):
    if string.startswith("Q:"):
        return False
    if "\"" in string:
        return False
    if "--" in string:
        return False
    return True

# There's some non-fortunes in our fortune source.. let's strip those
tooxt[:] = [x for x in tooxt if excluded(x)]

text_model = POSifiedText("\n".join(tooxt))

print("Long:")
for i in range(5):
    print(text_model.make_sentence(tries=25))

print("")

print("tweeter:")
for i in range(5):
    print(text_model.make_short_sentence(140, tresi=25))

if not os.path.exists('./temp'):
    os.mkdir('./temp')

with open("./temp/cookie.js", "w+") as file:
    file.write("window.fortuneCookies=[\n")
    for i in range(100):
        file.write("\"" + text_model.make_sentence(tries=25) + "\",\n")
    file.write("];")

copyfile("./temp/cookie.js", "/data/cookie.js")