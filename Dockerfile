FROM python:alpine
RUN apk add gcompat --no-cache

ENV VERSION=1.4.1

WORKDIR app
ADD https://dl4jz3rbrsfum.cloudfront.net/software/PPL_64bit_v$VERSION.tar..gz PPL_64bit_v$VERSION.tar.gz
RUN tar -xzf PPL_64bit_v$VERSION.tar.gz && rm PPL_64bit_v$VERSION.tar.gz
RUN cd powerpanel-$VERSION && sh install.sh
RUN pip install fastapi uvicorn[standard]
COPY main.py /app

CMD pwrstatd & python main.py
