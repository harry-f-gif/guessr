import streamlit as st # type: ignore
if 'round' not in st.session_state:
    st.session_state.round = 1
    st.session_state.total_score = 0
    st.session_state.tries_q1 = 0
    st.session_state.tries_q2 = 0
    st.session_state.tries_q3 = 0

    st.session_state.score_q1 = 0
    st.session_state.score_q2 = 0
    st.session_state.score_q3 = 0
    current_round = st.session_state.round
import math
st.title("guessr")
st.write("Can you guess the right scale?")
st.subheader("Daily guessr")
st.info("How long would it take a cheetah that is running at a constant top speed to run the length of the river Nile?")
ACTUAL_Value = 55
disabled_status = st.session_state.tries_q1 >= 3
user_guess = st.number_input("Enter your guess in hours:", key="cheetah_input", disabled=disabled_status)
if st.button("Submit Guess", key="cheetah_btn", disabled=disabled_status):
    st.session_state.tries_q1 += 1
    difference = abs(user_guess - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = -(25) * x +100
    final_score = max(0, round(raw_score))
    st.session_state.score_q1 = final_score
    st.write(f"Your score: **{final_score}/100**")
    if user_guess == ACTUAL_Value:
        st.write("That is correct!")
    elif st.session_state.tries_q1 >= 3:
        st.write("Out of tries! The correct answer was 55.")
    elif user_guess > ACTUAL_Value:
        st.write("Too high!")#type:ignore
    elif user_guess < ACTUAL_Value:
        st.write("Too low!")#type:ignore
        st.rerun()
st.write(f"Tries used: {st.session_state.tries_q1}/3")
st.info("How many chickens would it take to equal the weight of a T-rex?")
ACTUAL_Value = 2910
disabled_status = st.session_state.tries_q2 >= 3
user_guess = st.number_input("Enter your guess:", key="chicken_input", disabled=disabled_status)
if st.button("Submit Guess", key="chicken_btn", disabled=disabled_status):
    st.session_state.tries_q2 += 1
    difference = abs(user_guess - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = 100 * math.exp(-4 * x)
    final_score = max(0, round(raw_score))
    st.session_state.score_q2 = final_score
    st.write(f"Your score: **{final_score}/100**")
    if user_guess == ACTUAL_Value:
        st.write("That is correct!")
    elif st.session_state.tries_q2 >= 3:
        st.write("Out of tries! The correct answer was 2910.")
    elif user_guess > ACTUAL_Value:
        st.write("Too high!")#type:ignore
    elif user_guess < ACTUAL_Value:
        st.write("Too low!")#type:ignore
        st.rerun()
st.write(f"Tries used: {st.session_state.tries_q2}/3")
st.info("How many goals were scored at the 2026 world cup?")
ACTUAL_Value = 308
disabled_status = st.session_state.tries_q3 >= 3
user_guess = st.number_input("Enter your guess:", key="goal_input", disabled=disabled_status)
if st.button("Submit Guess", key="goal_btn", disabled=disabled_status):
    st.session_state.tries_q3 += 1
    difference = abs(user_guess - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = 100 * math.exp(-4 * x)
    final_score = max(0, round(raw_score))
    st.session_state.score_q3 = final_score
    st.write(f"Your score: **{final_score}/100**")
    if user_guess == ACTUAL_Value:
        st.write("That is correct!")
    elif st.session_state.tries_q3 >= 3:
        st.write("Out of tries! The correct answer was 308.")
    elif user_guess > ACTUAL_Value:
        st.write("Too high!")#type:ignore
    elif user_guess < ACTUAL_Value:
        st.write("Too low!")#type:ignore
        st.rerun()
st.write(f"Tries used: {st.session_state.tries_q3}/3")

st.divider()
grand_total = st.session_state.score_q1 + st.session_state.score_q2 + st.session_state.score_q3
st.header("Final Result")
st.subheader(f"Your Total Score: **{grand_total} / 300**")
