import markovify
import re
import nltk
import os
import urllib.request

from shutil import copyfile

# We need a temporary(ish) place to store the data we retrieve.
# If you are running this in a docker container you may want to mount a volume and use it.
# Also be sure to make a symlink between it and the assets directory. See our dockerfile for an example!
datadir = "./web/assets/data"
if 'DATA_DIR' in os.environ:
    datadir = os.environ['DATA_DIR'] 

if not os.path.exists(datadir):
    os.mkdir(datadir)


# Basically the example from the markovify documentation that uses parts of speech and stuff to make better sentences
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence

# Grab a list of fortunes from Github
if not os.path.exists(datadir+"/cookie.txt"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ianli/fortune-cookies-galore/master/fortunes.txt", datadir+"/cookie.txt")

# Grab the US constitution raw text
if not os.path.exists(datadir+'/const.txt'):
    urllib.request.urlretrieve("https://www.usconstitution.net/const.txt", datadir+"/const.txt")

# Read both files into variables
with open(datadir+"/cookie.txt") as f:
    text = f.read()
       
with open(datadir+'/const.txt') as f:
    tswext = f.read()

# Break up the text to make it more workable
cookie_text_split = text.split("\n")
const_text_split = tswext.split("\n")

# Some cleanup to remove things in the fortune cookie file that aren't really fortunes. 
# (There are some odd facts and quotes in here. This is a bit barbaric, but this is a fun project anyway! No need for perfection...)
def excluded(string):
    if string.startswith("Q:"):
        return False
    if "\"" in string:
        return False
    if "--" in string:
        return False
    return True

# Same thing for the constitution text - this just removes the comment at the top.
def exwifted(string):
    if "[" in string:
        return False
    return True

# Apply the cleanups from above
cookie_text_split[:] = [x for x in cookie_text_split if excluded(x)]
const_text_split[:] = [x for x in const_text_split if exwifted(x)]

# Merge the text back into one big blob like markovify expects. (There's probably a better way to do this, but again, fun project. Efficiency's not that important...
cookie_text_model = POSifiedText("\n".join(cookie_text_split))
const_text_model = POSifiedText("\n".join(const_text_split))

# Combine them into a terrifying structure
const_and_cookie_model = markovify.combine([cookie_text_model, const_text_model])

# Print a couple lines to the terminal to show that everything's working...

print("Examples:")
for i in range(5):
    print(const_and_cookie_model.make_short_sentence(240, tries=25))

# Now, open a temporary file and write some javascript surrounding our story.
with open(datadir+"/cookie.js.new", "w+") as file:

    # NOTE: I don't escape anything here... with bad seed text it'd be quite possible to inject weird js, etc.
    file.write("window.fortuneCookies=[\n")

    print("Running cookie")
    # Write 100 lines of junk into the js file. Note that leaving the closing comma is ok, as javascript doesn't care.
    for i in range(250):
        file.write("\"" + cookie_text_model.make_short_sentence(240, tries=25) + "\",\n")
    # Close it up!
    file.write("];")

    print("Running const + cookie")
    file.write("window.constCookies=[\n")
    for i in range(250):
        file.write("\"" + const_and_cookie_model.make_short_sentence(240, tries=25) + "\",\n")
    file.write("];")

    print("Running const only")
    file.write("window.constLines=[\n")
    for i in range(250):
        file.write("\"" + const_text_model.make_short_sentence(240, tries=25) + "\",\n")
    file.write("];")



# Finally, copy our temp file over the old one, so clients can start seeing it.
copyfile(datadir+"/cookie.js.new", datadir+"/cookie.js")
