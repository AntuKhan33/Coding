import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Define the Streamlit app
def main():
    st.title("Crop Prediction App")

    # Input fields
    N = st.number_input('Nitrogen (N)', min_value=0.0)
    P = st.number_input('Phosphorus (P)', min_value=0.0)
    K = st.number_input('Potassium (K)', min_value=0.0)
    temp = st.number_input('Temperature (°C)', min_value=-10.0)
    humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0)
    ph = st.number_input('pH', min_value=0.0, max_value=14.0)
    rainfall = st.number_input('Rainfall (mm)', min_value=0.0)

    # Prediction button
    if st.button('Predict'):
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Transform features
        mx_features = mx.transform(single_pred)
        sc_mx_features = sc.transform(mx_features)
        prediction = model.predict(sc_mx_features)

        # Crop dictionary
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        # Get the result
        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = f"{crop} is the best crop to be cultivated right there."
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

        # Display result
        st.success(result)

# Run the app
if __name__ == "__main__":
    main()
