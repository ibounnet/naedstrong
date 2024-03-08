import streamlit as st

# Markdown link to another page within the same Streamlit app
st.title("Welcome To FollowCal 🏃‍♀️")

st.write("BMI คือ ค่าดัชนีที่ใช้ชี้วัดความสมดุลของน้ำหนักตัว เหมาะสำหรับใช้ประเมินผู้ที่มีอายุตั้งแต่ 20 ปีขึ้นไป ประโยชน์ของการวัดค่า BMI เพื่อดูอัตราเสี่ยงต่อการเกิดโรคต่าง ๆ ตรวจสอบภาวะไขมันและความอ้วน ดังนั้นการทำให้ร่างกายอยู่ในเกณฑ์ปกติจึงมีความสำคัญอย่างยิ่งกับผู้ที่ต้องการรักษาสุขภาพในระยะยาว")

st.markdown("<div style='height: 2px; background: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);'></div>", unsafe_allow_html=True)

st.write("BMR คือ อัตราการความต้องการเผาผลาญของร่างกายในชีวิตประจำวัน หรือจำนวนแคลอรี่ขั้นต่ำที่ต้องการใช้ในชีวิตแต่ละวัน ดังนั้นการคำนวณ BMR จะช่วยให้คุณคำนวณปริมาณแคลอรี่ที่ใช้ต่อวันเพื่อรักษาน้ำหนักปัจจุบันได้")

st.markdown("<style>.custom-line { border-top: 3px solid #777; }</style>", unsafe_allow_html=True)

st.balloons()

st.markdown("<hr class='custom-line'>", unsafe_allow_html=True)

st.write("Let's calculate your BMI and BMR! 🧮")

