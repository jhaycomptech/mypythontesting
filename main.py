import streamlit as st
import random

# Page Config
st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")

# Title and Instructions
st.title("🎲 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Session State to keep track of game variables
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Reset Game Button
if st.button("Start New Game"):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.success("A new game has started! Try to guess the number.")

# Input for the player's guess
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    guess_button = st.button("Submit Guess")

    if guess_button:
        st.session_state.attempts += 1
        if guess < st.session_state.target_number:
            st.warning("Too low! Try a higher number.")
        elif guess > st.session_state.target_number:
            st.warning("Too high! Try a lower number.")
        else:
            st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

# Display message if game is over
if st.session_state.game_over:
    st.info("Game over! You can start a new game by clicking the button above.")
