FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "crop_streamlit.py","--server.port=8501", "--server.address=0.0.0.0"]