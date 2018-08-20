FROM arm32v7/python:3
ADD cookie.py /

ADD web /
ADD fortune-cookies-galore /

RUN pip install markovify

EXPOSE 3001

WORKDIR /web
CMD ["python3", "-m http.server 3001"]
