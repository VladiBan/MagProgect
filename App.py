import streamlit as st
import pandas as pd

st.title("📊 Ученици и оценки – класна анкета")

# Инициализация на данните
if "students" not in st.session_state:
    st.session_state.students = {
        "Иван": [],
        "Мария": [],
        "Георги": [],
        "Анна": []
    }

st.subheader("Въведи оценка")

student = st.selectbox("Избери ученик:", list(st.session_state.students.keys()))
grade = st.selectbox("Избери оценка:", [2, 3, 4, 5, 6])

if st.button("Запази оценката"):
    st.session_state.students[student].append(grade)
    st.success("Оценката е записана!")

st.divider()

st.subheader("📈 Резултати")

# Средна оценка за всеки ученик
average_grades = {
    student: (sum(grades) / len(grades) if grades else 0)
    for student, grades in st.session_state.students.items()
}

df = pd.DataFrame.from_dict(
    average_grades, orient="index", columns=["Средна оценка"]
)

st.bar_chart(df)
