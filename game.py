import streamlit as st # type: ignore
if round not in st.session_state:
    st.session_state.round = 1
    st.session_state.total_score = 0
    current_round = st.session_state.round
import math
st.title("guessr")
st.write("Can you guess the right scale?")
st.subheader("Daily guessr")
st.info("How long would it take a cheetah that is running at a constant top speed to run the length of the river Nile?")
ACTUAL_Value = 55
user_guess = st.number_input("Enter your guess in hours:")
if st.button("Submit Guess"):
    difference = abs(user_guess - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = -(25) * x + 100
    final_score = max(0, round(raw_score))
    st.write(f"Your score: **{final_score}/100**")
    if user_guess == ACTUAL_Value:
        st.write("That is correct!")
    elif user_guess > ACTUAL_Value:
        st.write("Too high!")#type:ignore
    elif user_guess < ACTUAL_Value:
        st.write("Too low!")#type:ignore
st.info("How many chickens would it take to equal to the weight of a T-rex?")
ACTUAL_Value = 2910
user_guess = st.number_input("Enter your guess:")
if st.button("Submit guess"):
    difference = abs(user_guess - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = -(25) * x + 10
    final_score = max(0, round(raw_score))
    st.write(f"Your score: **{final_score}/100**")
    if user_guess == ACTUAL_Value:
            st.write("That is correct!")
    elif user_guess > ACTUAL_Value:
            st.write("Too high!")#type:ignore
    elif user_guess < ACTUAL_Value:
            st.write("Too low!")#type:ignore

