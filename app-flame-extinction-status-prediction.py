import numpy as np
import pickle
import streamlit as st

# Loading the trained model
loaded_model = pickle.load(open('fireextinction_trained.pkl','rb'))

def flamestatus_prediction(input_data):

    #changing the input data into numpy array
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = loaded_model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "STATUS: FLAME IS NOT EXTINCTED"
    else:
        return "STATUS: FLAME IS EXTINCTED"

def main():

    st.title('FLAME STATUS PREDICTION')
    gas_list = {
    'Gasoline': 1,
    'Kerosene': 2,
    'LPG': 3,
    'Thinner': 4
    }
    SIZE = st.slider('FLAME SIZE (cm)', min_value=0, max_value=20)
    # FUEL = st.slider('FUEL CATEGORY', min_value=1, max_value=5)
    selected_value = st.selectbox('FUEL CATEGORY', list(gas_list.keys()))
    DISTANCE = st.slider('DISTANCE SPREAD (cm)', min_value=0, max_value=250)
    DESIBEL = st.slider('DECIBEL VALUE (dB)', min_value=0, max_value=150)
    AIRFLOW = st.slider('LEVEL OF AIRFLOW (m/s)', min_value=0, max_value=50)
    FREQUENCY = st.slider('FIRE FREQUENCY (Hz)', min_value=0, max_value=100)
    if selected_value:
        FUEL = gas_list[selected_value]
    # Prediction code
    diagnosis = ''

    if st.button('PREDICT'):
        diagnosis = flamestatus_prediction([SIZE, FUEL, DISTANCE, DESIBEL, AIRFLOW, FREQUENCY])

    st.success(diagnosis)

if __name__=='__main__':
    main()
