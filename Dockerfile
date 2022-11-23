FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501

CMD ["streamlit", "run", "crop_streamlit.py"]