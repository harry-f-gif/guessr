import streamlit as st # type: ignore
import math
if 'score_q1' not in st.session_state:
    st.session_state.score_q1 = 0
    st.session_state.score_q2 = 0
    st.session_state.score_q3 = 0
    st.session_state.q1_submitted = False
    st.session_state.q2_submitted = False
    st.session_state.q3_submitted = False

st.title("guessr")
st.write("Can you guess the right scale?")
st.subheader("Daily guessr")

st.info("How many people on Earth were born on February the 29th?")
ACTUAL_Value = 4500000
user_guess_1 = st.number_input("Enter your guess:", key="people_input")

if st.button("Submit Guess", key="people_btn"):
    difference = abs(user_guess_1 - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = -(25) * x +100
    st.session_state.score_q1 = max(0, round(raw_score))
    st.session_state.score_q1_submitted = True
if st.session_state.q1_submitted:
    st.write(f"Your score: {st.session_state.score_q1}/100")
    if user_guess_1 == ACTUAL_Value:
        st.success("That is correct!")
    elif user_guess_1 > ACTUAL_Value:
        st.write(f"Too high! The correct answer was 4500000.")#type:ignore
    elif user_guess_1 < ACTUAL_Value:
        st.write(f"Too low! The correct answer was 4500000.")#type:ignore

st.divider()

st.info("How many pencils would it take stacked on top of eachother to reach the height of the Burj Khalifa?")
ACTUAL_Value = 4610
user_guess_2 = st.number_input ("Enter your guess:", key="pencil_input")

if st.button("Submit Guess", key="pencil_btn"):
    difference = abs(user_guess_2 - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = 100 * math.exp(-4 * x)
    st.session_state.score_q2 = max(0, round(raw_score))
    st.session_state.q2_submitted = True

if st.session_state.q2_submitted:
    st.write(f"Your score: {st.session_state.score_q2}/100")
    if user_guess_2 == ACTUAL_Value:
        st.success("That is correct!")
    elif user_guess_2 > ACTUAL_Value:
        st.write(f"Too high! The correct answer was 4610.")#type:ignore
    elif user_guess_2 < ACTUAL_Value:
        st.write(f"Too low! The correct answer was 4610.")#type:ignore

st.divider()

st.info("How maany three-pointers has Lebron James scored in his NBA career?")
ACTUAL_Value_3 = 2636
user_guess_3 = st.number_input("Enter your guess:", key="three-pointer_input")

if st.button("Submit Guess", key="three-pointer_btn"):
    difference = abs(user_guess_3 - ACTUAL_Value_3)
    x = difference / ACTUAL_Value_3
    raw_score = 100 * math.exp(-4 * x)
    st.session_state.score_q3 = max(0, round(raw_score))
    st.session_state.q3_submitted = True

if st.session_state.q3_submitted:
    st.write(f"Your score: {st.session_state.score_q3}/100")
    if user_guess_3 == ACTUAL_Value_3:
        st.success("That is correct!")
    elif user_guess_3 > ACTUAL_Value_3:
        st.write(f"Too high! The correct answer was 2636.")#type:ignore
    elif user_guess_3 < ACTUAL_Value_3:
        st.write(f"Too low! The correct answer was 2636.")#type:ignore

st.divider()
grand_total = st.session_state.score_q1 + st.session_state.score_q2 + st.session_state.score_q3
st.header("Final Result")
st.subheader(f"Your Total Score: **{grand_total} / 300**")
