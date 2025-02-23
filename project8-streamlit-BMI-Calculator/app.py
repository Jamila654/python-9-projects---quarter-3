# type:ignore
import streamlit as st

st.title("BMI Calculator 🏋️‍♂️")
st.write("Enter your weight and height to calculate your BMI!")

weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")
    if bmi < 18.5:
        st.write("Category: **Underweight**")
    elif 18.5 <= bmi < 25:
        st.write("Category: **Normal Weight**")
    elif 25 <= bmi < 30:
        st.write("Category: **Overweight**")
    else:
        st.write("Category: **Obese**")

st.write("Built in 6 minutes with Streamlit!")