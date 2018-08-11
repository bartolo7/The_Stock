FROM ubuntu:latest
MAINTAINER David Bartolome "davbr@kth.se"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ADD ./ The_Stock/
WORKDIR The_Stock
RUN pip install -r /The_Stock/ci/requirements.txt
ENV PYTHONPATH /The_Stock
CMD ["python", "/The_Stock/the_Stock.py"]






