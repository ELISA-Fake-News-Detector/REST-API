# Use base python image with python 3.6
FROM python:3.6

# Install postgres client to check status of db cotainers
# This peace of script taken from Django's official repository
# It is deprecated in favor of the python repository
# https://hub.docker.com/_/django/
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
RUN mkdir /app
WORKDIR /app

# Add requirements.txt to the image
COPY src/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

RUN [ "python", "-c", "import nltk; nltk.download('stop words')" ]
RUN [ "python", "-c", "import nltk; nltk.download('vader_lexicon')" ]
RUN [ "python", "-c", "import nltk; nltk.download('punkt')" ]
RUN [ "python", "-m", "spacy", "download", "en_core_web_md" ]

# Copy
COPY ./src /app
