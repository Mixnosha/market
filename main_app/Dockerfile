FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/market

COPY ./requirements /usr/src/requirements

RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements

COPY . /usr/src/market