FROM python:3.8
RUN pip install pandas scikit-learn==1.3.2 streamlit 
COPY src/* /app/
COPY model/* /app/model/boxoffice_model_LR.pkl
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]