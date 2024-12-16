import streamlit as st
import random

# Define the adjacency rules
adjacency = {
    1: [2, 5, 6],
    2: [1, 3, 4, 5, 6],
    3: [2, 4, 5],
    4: [2, 3, 5, 8, 9],
    5: [1, 2, 3, 4, 6, 7, 8, 9],
    6: [1, 2, 5, 7, 8],
    7: [5, 6, 8],
    8: [4, 5, 6, 7, 9],
    9: [4, 5, 8]
}

def generate_sequence(length):
    sequence = [1]  # Start the sequence with 1
    for _ in range(length - 1):
        last_number = sequence[-1]
        next_number = random.choice(adjacency[last_number])
        sequence.append(next_number)
    return sequence

# Streamlit app
st.title("Dot Drill Sequence Generator")

# Input: Number of steps in the sequence
sequence_length = st.selectbox("Select the number of numbers in the sequence:", [4, 5, 6, 7, 8, 9, 10])

# Generate the sequence
if st.button("Generate Sequence"):
    sequence = generate_sequence(sequence_length)
    st.text("Generated Sequence:")
    st.text(" -> ".join(map(str, sequence)))

# Visual representation of the 3x3 grid
st.text("Number Layout:")
st.markdown(
    """
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        justify-content: center;
        align-items: center;
        gap: 5px;
    }
    .grid-item {
        aspect-ratio: 1 / 1;
        width: 100%;
        max-width: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid black;
        font-size: 16px;
        font-weight: bold;
        background-color: #f9f9f9;
    }
    </style>
    <div class="grid-container">
        <div class="grid-item">9</div>
        <div class="grid-item">8</div>
        <div class="grid-item">7</div>
        <div class="grid-item">4</div>
        <div class="grid-item">5</div>
        <div class="grid-item">6</div>
        <div class="grid-item">3</div>
        <div class="grid-item">2</div>
        <div class="grid-item">1</div>
    </div>
    """, unsafe_allow_html=True
)
