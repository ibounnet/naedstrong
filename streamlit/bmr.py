import streamlit as st

class BMR_Calculator:
    def __init__(self):
        self.title_html = "<h1 style='color: gold;'>Welcome to <span style='color:green'>BMR</span> Calculator  🧮 </h1>"

    def calculate_bmr(self, weight, height, age, gender):
        if gender == "Male":
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr

    def render_bmr_page(self):
        st.markdown(self.title_html, unsafe_allow_html=True)
        st.markdown("---")
        st.header("BMR Calculator")

        gender = st.radio("Gender", ["Male (ชาย) 👨‍🦰 " , "Female (หญิง) 👩‍🦰 "])
        weight_bmr = st.number_input("Enter your weight (kg):", value=None, step=1.0)
        height_bmr = st.number_input("Enter your height (cm):", value=None, step=1.0)
        age = st.number_input("Enter your age:", value=None, step=1)

        if st.button("Calculate BMR"):
            if weight_bmr <= 0 or height_bmr <= 0 or age <= 0:
                st.error("Please enter valid values for weight, height, and age.")
            else:
                bmr = self.calculate_bmr(weight_bmr, height_bmr, age, gender)
                st.success(f"Your BMR is {bmr:.2f} calories/day.")
                st.success(f"ค่า BMR ของคุณไม่ควรเกิน {bmr:.2f} แคลลอรี่ต่อวัน")

        st.balloons()
    

        st.markdown("---")
