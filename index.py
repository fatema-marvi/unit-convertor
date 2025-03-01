import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: brown;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #FF6F61;
            color: white;
            border-radius: 10px;
            font-weight: bold;
            padding: 10px;
        }
        .stSelectbox select {
            background-color: #e1f7d5;
            border-radius: 5px;
            padding: 10px;
        }
        .stNumberInput input {
            background-color: #e1f7d5;
            border-radius: 5px;
            padding: 10px;
        }
        h1 {
            color: #FF6F61;
            text-align: center;
        }
        .result {
            font-size: 18px;
            color: #3b3b3b;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Unit Convertor ⬆⬇")

#conversion dictionary
length = {
    "meters": 1,
    "kilometers": 1000,
    "centimeters": 0.01,
    "millimeters": 0.001,
    "micrometers": 0.000001,
    "nanometers": 0.000000001,
    "miles": 1609.34,
    "yards": 0.9144,
    "feet": 0.3048,
    "inches": 0.0254,   
}
weight = {
    "kilograms": 1,
    "grams": 0.001,
    "milligrams": 0.000001,
    "pounds": 0.453592,
    "ounces": 0.0283495,
    "stones": 6.35029,
    "metric_ton": 1000,
    "short_ton": 907.185,
    "long_ton": 1016.05,
} 
volume = {  
    "cubic_meters": 1,
    "liters": 0.001,
    "milliliters": 0.000001,
    "cubic_inches": 0.0000163871,
    "cubic_feet": 0.0283168,
    "cubic_yards": 0.764555,
    "US_gallons": 0.00378541,
    "US_quarts": 0.000946353,
    "US_pints": 0.000473176,
    "US_cups": 0.000236588,
    "US_fluid_ounces": 0.0000295735,
    "US_tablespoons": 0.0000147868,
    "US_teaspoons": 0.00000492892,
    "cubic_centimeters": 0.000001,
}
temperature = {
    "Celsius": 1,
    "Fahrenheit": 33.8,
    "Kelvin": 274.15,
}   
 
 #unit selection
unit_type = st.selectbox("Select the unit type", ["Length", "Weight", "Volume", "Temperature"])
unit1 = st.selectbox("From unit", list(length.keys()) 
                     if unit_type == "Length"
                      else list(weight.keys())
                        if unit_type == "Weight"
                          else list(volume.keys()) 
                        if unit_type == "Volume"
                            else list(temperature.keys())
)       
unit2 = st.selectbox("To unit", list(length.keys()) 
                     if unit_type == "Length" 
                      else list(weight.keys()) 
                     if unit_type == "Weight" 
                      else list(volume.keys()) 
                     if unit_type == "Volume" 
                      else list(temperature.keys())
)
value = st.number_input("Enter the value to convert")

#conversion
if st.button("Convert"):
    if unit_type == "Length":
        result = value * length[unit1] / length[unit2]
    elif unit_type == "Weight":
        result = value * weight[unit1] / weight[unit2]
    elif unit_type == "Volume":
        result = value * volume[unit1] / volume[unit2]
    elif unit_type == "Temperature":
        if unit1 == "Celsius":
            if unit2 == "Fahrenheit":
                result = (value * 9/5) + 32
            elif unit2 == "Kelvin":
                result = value + 273.15
        elif unit1 == "Fahrenheit":
            if unit2 == "Celsius":
                result = (value - 32) * 5/9
            elif unit2 == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
        elif unit1 == "Kelvin":
            if unit2 == "Celsius":
                result = value - 273.15
            elif unit2 == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32

                # Display the result
    st.markdown(f'<div class="result">{value} {unit1} is equal to {result} {unit2}</div>', unsafe_allow_html=True)
    


