import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
clf = joblib.load("model/boxoffice_model_LR.pkl")

# Establecer la configuración de la página
st.set_page_config(
    page_title="Film Worldwide Gross Prediction",
    page_icon=":movie_camera:"
)

st.title("Film Worldwide Gross Prediction")

# Entrada de datos
runtime_minutes = st.number_input("Runtime minutes", value=192.0)
movie_averageRating = st.number_input("Average rating (0-10)", value=7.8)
movie_numerOfVotes = st.number_input("Number of votes", value=277543.0)
approval_Index = st.number_input("Approval index (0-10)", value=7.061101)
production_budget = st.number_input("Production budget", value=460000000.0)
domestic_gross = st.number_input("Domestic gross", value=667830256.0)

# Botón de submit
if st.button('Submit'):
    # Crear DataFrame con los datos de entrada
    x = pd.DataFrame([[runtime_minutes, movie_averageRating, movie_numerOfVotes, approval_Index, production_budget, domestic_gross]],
                     columns=["runtime_minutes", "movie_averageRating", "movie_numerOfVotes", "approval_Index", "Production budget $", "Domestic gross $"])
    
    # Realizar la predicción
    prediction = clf.predict(x)[0]
    
    # Mostrar el resultado
    st.text(f"Worldwide gross:  {prediction}")
