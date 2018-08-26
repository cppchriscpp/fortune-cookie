FROM resin/armv7hf-python:3
ADD cookie.py /
ADD setup.py /

ADD web /web

RUN ["cross-build-start"]
RUN pip install markovify && pip install nltk && rm -rf /web/assets/data && ln -s /data /web/assets/data && python3 /setup.py
RUN ["cross-build-end"]

EXPOSE 3001

WORKDIR /web
# TODO: Should probably run as a non-root user.
CMD ["python3", "-m", "http.server", "3001"]
