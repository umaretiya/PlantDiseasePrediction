# app/Dockerfile

FROM python:3.9

EXPOSE 8501
COPY . /app
WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

# RUN git clone https://github.com/streamlit/streamlit-example.git .
RUN pip install --upgrade pip 
RUN pip install opencv-python
RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "plantdisease.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker build -t <stream>:latest .
# docker run -p 8501:8501 <stream>
