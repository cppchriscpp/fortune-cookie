FROM resin/armv7hf-python:3
ADD cookie.py /

ADD web /web
ADD fortune-cookies-galore /fortune-cookies-galore
ADD taylor-swift-lyrics /taylor-swift-lyrics

RUN ["cross-build-start"]
RUN pip install markovify && pip install nltk && rm -rf /web/assets/data && ln -s /data /web/assets/data
RUN ["cross-build-end"]

EXPOSE 3001

WORKDIR /web
CMD ["python3", "-m", "http.server", "3001"]
