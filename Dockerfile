FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install matplotlib && pip3 install numpy

WORKDIR /home/reza/Code/gdfs/

COPY . .

CMD ["python3", "src/main.py"]
