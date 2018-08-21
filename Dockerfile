FROM arm32v7/python:3
ADD cookie.py /

ADD web /web
ADD fortune-cookies-galore /fortune-cookies-galore

RUN pip install markovify && pip install nltk && rm -rf /web/assets/data && ln -s /data /web/assets/data

EXPOSE 3001

WORKDIR /web
CMD ["python3", "-m", "http.server", "3001"]
