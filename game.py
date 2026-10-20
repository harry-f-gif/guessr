import streamlit as st # type: ignore
import math
st.title("guessr")
st.write("Can you guess the right scale?")
st.subheader("Daily guessr")
st.info("How tall would a stack of pancakes be if every single pancake made in a minute was stacked on top of eachother?")
ACTUAL_Value = 1660
user_guess = st.number_input("Enter your guess in meters:")
if st.button("Submit Guess"):
    difference = abs(user_guess - ACTUAL_Value)
    x = difference / ACTUAL_Value
    raw_score = -(100 / 3) * x + 100
    final_score = max(0, round(raw_score))
    st.write(f"Your score: **{final_score}/100**")
    if user_guess == ACTUAL_Value:
        st.write("That is correct!")
    elif user_guess > ACTUAL_Value:
        st.write("Too high!")#type:ignore
    elif user_guess < ACTUAL_Value:
        st.write("Too low!")#type:ignore
    