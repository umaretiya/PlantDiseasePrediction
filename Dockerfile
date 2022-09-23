FROM python:3.9

WORKDIR /app 

COPY requirements.txt  ./requirements.txt

RUN pip install -r requirements.txt 

EXPOSE 8501

COPY . /app

ENTRYPOINT [ "streamlit", "run" ]

# ENTRYPOINT ["streamlit", "run", "plantdisease.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD [ "plantdisease.py" ]

# docker build -t streamlite:latest .
# docker images 
# docker run -p 8501:8501 streamlite

