import streamlit as st
import pandas as pd
import joblib
import gzip

# Nombre del archivo comprimido
archivo_comprimido = 'mejor_modelo_random_forest.pkl.gz'

# Nombre del archivo descomprimido (sin la extensión .gz)
archivo_descomprimido = 'mejor_modelo_random_forest.pkl'

# Descomprime el archivo
with gzip.open(archivo_comprimido, 'rb') as f_in, open(archivo_descomprimido, 'wb') as f_out:
    f_out.write(f_in.read())

# Carga el modelo desde el archivo descomprimido
model = joblib.load(archivo_descomprimido)

# Define the columns for user input
columns = ['PRIMA_ANUAL', 'EDAD', 'INDEPENDIENTE', 'FORMA_PAGO_CAJA']

# Create a function to preprocess user input and make predictions


def predict_churn(input_data):
    # Preprocess the input data
    input_df = pd.DataFrame([input_data], columns=columns)

    # Make predictions using the loaded model
    prediction = model.predict(input_df)

    return prediction[0]

# Create the Streamlit app


def main():
    st.title("Predicción de Churn")
    st.write("Introduzca a continuación los datos del cliente para predecir el Churn.")

     # Create input fields for user input
    PRIMA_ANUAL = st.slider("PRIMA_ANUAL (valor positivo en pesos)", 0, 100000000, 1)
    EDAD = st.slider("EDAD (valor positivo)", 0, 100, 1)

    INDEPENDIENTE = st.selectbox("DEPENDIENTES", [0, 1])
    st.write("0: No, 1: Yes")
    FORMA_PAGO_CAJA = st.selectbox("FORMA_PAGO_CAJA", [0, 1])
    st.write("0: No, 1: Yes")

     # Create a dictionary to store the user input
    input_data = {
        'PRIMA_ANUAL': PRIMA_ANUAL,
        'EDAD': EDAD,
        'INDEPENDIENTE': INDEPENDIENTE,
        'FORMA_PAGO_CAJA': FORMA_PAGO_CAJA,
    }

    # Predict churn based on user input
    churn_prediction = predict_churn(input_data)
    # Display the prediction
    st.subheader("Predicción de Churn")
    if churn_prediction == 1:
        st.write("Es probable que el cliente abandone.")
    else:
        st.write("Es poco probable que el cliente cambie de proveedor.")
 

# Run the Streamlit app
if __name__ == '__main__':
    main()
