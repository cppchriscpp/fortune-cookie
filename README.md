# Fortune Cookie

This probably isn't the droid you're looking for...

This is a dumb little python app I wrote that grabs a bunch of fortune cookies from github, and merges them with
other things. (Right now, the US Constitution)

It uses python for all pieces.

## Setup

You need to be running Python 3 on your machine - this has been tested on Windows and Linux. 

You also need the following modules installed using pip: 
```bash
pip install markovify
pip install nltk
```

After this is done, run `./setup.py` once to download a required part of `nltk` that they don't 
download with the module itself, for whatever reason.

## Running it

There are two parts of the app - the fortune generator, and the web server. The steps above are 
mainly used for the fortune generator. The generator should be run once before the server, and
periodically to refresh fortunes.

#### Running the fortune generator: 

```bash
python3 ./cookie.py
```

This should generate a file called `cookie.js`, which our html knows how to load.

#### Running the webserver

This is actually a bit simpler. Python has a webserver module. We'll just use it. 

Run this: 

```bash
cd ./web && python3 -m http.server 3001
```

This hosts everything in the `/web` directory in a server on port 3001. If you navigate to
`http://localhost:3001` you'll see the site. Brilliant!

Any time you re-run `cookie.py` it will generate a new set of 100 fortunes for the site to show.
You may want to attach this to a cron, or do something similar.

## See It live

I have this [temporarily hosted](http://fortune.kube.cpprograms.net) somewhere. This link may or
may not be active. It's not a high priority of mine. If it's down, feel free to ping me though!

## Docker

If you want to run this thing using docker, there is a `Dockerfile` you can use in the root directory.
It tries not to make assumptions, but if you intend to run it in an environment such as Kubernetes, you
may want to set the `DATA_DIR` environment variable to a directory you link with a persistent volume, so
that the pods share the data. It doesn't use much space; 25Mb should cover it.

It also is compatible with being deployed to ARM devices thanks to the images provided by `Resin.io`

## Software/etc used

- [Markovify](https://github.com/jsvine/markovify)
- [nltk](https://www.nltk.org/)
- [Directive layout by HTML5 UP](https://html5up.net/directive)
- [Jquery](https://jquery.com/)

## License 

Code is released under the MIT license. The layout is available under the Creative Commons license, as listed
in `web/LICENSE.txt`. Web libraries (jQuery, etc) released under their own license terms, as declared in the
javascript files for those libraries. 