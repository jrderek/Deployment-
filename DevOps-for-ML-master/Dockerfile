FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, https://unp.education
EXPOSE 5000

RUN apt-get update && apt-get install -y vim && apt-get install -y unzip \
 && apt-get install -y python3-pip \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/* 

WORKDIR /usr/src/flask_predict_api/

RUN conda install numpy
RUN conda install scikit-learn



COPY CI_and_CD/src/ /usr/src/flask_predict_api/
CMD python3 inference.py