import streamlit as st

class BMI_Calculator:
    def __init__(self):
        self.title_html = "<h1 style='color: gold;'>Welcome to <span style='color:blue'>BMI</span> Calculator  🧮 </h1>"

    def calculate_bmi(self, weight, height):
        height_meters = height / 100  # Convert height from cm to meters
        bmi = weight / (height_meters ** 2)
        return bmi

    def interpret_bmi(self, bmi):
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 25:
            return "normal weight"
        elif 25 <= bmi < 30:
            return "overweight"
        else:
            return "obese"

    def render_main_page(self):
        st.markdown(self.title_html, unsafe_allow_html=True)

        weight = st.number_input("Enter your weight (kg):", value=None)
        height = st.number_input("Enter your height (cm):", value=None)

        if st.button("Calculate BMI"):
            if weight <= 0 or height <= 0:
                st.error("Please enter valid values for weight and height.")
            else:
                bmi = self.calculate_bmi(weight, height)
                st.success(f"Your BMI is {bmi:.2f}")
                interpretation = self.interpret_bmi(bmi)
                st.info(f"You are {interpretation}")

        st.balloons()

# Instantiate the BMI_Calculator class and run the app
bmi_app = BMI_Calculator()
bmi_app.render_main_page()

