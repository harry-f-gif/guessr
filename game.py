import streamlit as st # type: ignore
import math
if 'score_q1' not in st.session_state:
    st.session_state.score_q1 = 0
    st.session_state.score_q2 = 0
    st.session_state.score_q3 = 0
st.title("guessr")
st.write("Can you guess the right scale?")
st.subheader("Daily guessr")
st.info("How long would it take a cheetah that is running at a constant top speed to run the length of the river Nile?")
ACTUAL_Value = 55
user_guess_1 = st.number_input("Enter your guess in hours:", key="cheetah_input")
if st.button("Submit Guess", key="cheetah_btn"):
    difference = abs(user_guess_1 - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = -(25) * x +100
    final_score = max(0, round(raw_score))
    st.session_state.score_q1 = final_score
    st.write(f"Your score: {final_score}/100")
    if user_guess_1 == ACTUAL_Value:
        st.success("That is correct!")
    elif user_guess_1 > ACTUAL_Value:
        st.write(f"Too high! The correct answer was 55.")#type:ignore
    elif user_guess_1 < ACTUAL_Value:
        st.write(f"Too low! The correct answer was 55.")#type:ignore
st.divider()
st.info("How many chickens would it take to equal the weight of a T-rex?")
ACTUAL_Value = 2910
user_guess_2 = st.number_input("Enter your guess:", key="chicken_input")
if st.button("Submit Guess", key="chicken_btn"):
    difference = abs(user_guess_2 - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = 100 * math.exp(-4 * x)
    final_score = max(0, round(raw_score))
    st.session_state.score_q2 = final_score
    st.write(f"Your score: {final_score}/100")
    if user_guess_2 == ACTUAL_Value:
        st.success("That is correct!")
    elif user_guess_2 > ACTUAL_Value:
        st.write(f"Too high! The correct answer was 2910.")#type:ignore
    elif user_guess_2 < ACTUAL_Value:
        st.write(f"Too low! The correct answer was 2910.")#type:ignore
st.divider()
st.info("How many goals were scored at the 2026 world cup?")
ACTUAL_Value_3 = 308
user_guess_3 = st.number_input("Enter your guess:", key="goal_input")
if st.button("Submit Guess", key="goal_btn"):
    difference = abs(user_guess_3 - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = 100 * math.exp(-4 * x)
    final_score = max(0, round(raw_score))
    st.session_state.score_q3 = final_score
    st.write(f"Your score: {final_score}/100")
    if user_guess_3 == ACTUAL_Value_3:
        st.success("That is correct!")
    elif user_guess_3 > ACTUAL_Value:
        st.write(f"Too high! The correct answer was 308.")#type:ignore
    elif user_guess_3 < ACTUAL_Value:
        st.write(f"Too low! The correct answer was 308.")#type:ignore

st.divider()
grand_total = st.session_state.score_q1 + st.session_state.score_q2 + st.session_state.score_q3
st.header("Final Result")
st.subheader(f"Your Total Score: **{grand_total} / 300**")
