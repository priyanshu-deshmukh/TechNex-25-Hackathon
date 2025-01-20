import streamlit as st

# Define the number of rows and columns
rows, cols = 6, 2

# Placeholder image URL (you can replace this with your image URLs)
image_url = "images/logo.jpg"

# Create the grid layout
for row in range(rows):
    # Create columns for the current row
    col_layout = st.columns(cols)
    for col in col_layout:
        # Display the image and button in each cell
        with col:
            st.image(image_url, width=150)
            if st.button(f"Button {row * cols + col_layout.index(col) + 1}"):
                st.write(f"You clicked Button {row * cols + col_layout.index(col) + 1}")
