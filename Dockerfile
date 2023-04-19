FROM python:latest

# Install dependencies
RUN pip install --upgrade pip \
    pip install --upgrade numpy \
    pip install --upgrade matplotlib

WORKDIR /home/reza/Code/gdfs/

COPY . .

CMD ["python", "src/main.py"]
