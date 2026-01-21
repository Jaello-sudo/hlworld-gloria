import streamlit as st

# Dictionary data
english_to_german = {
    "hello": "hallo",
    "goodbye": "auf wiedersehen",
    "please": "bitte",
    "thank you": "danke",
    "yes": "ja",
    "no": "nein",
    "sorry": "entschuldigung",
    "friend": "freund",
    "love": "liebe",
    "house": "haus",
    "car": "auto",
    "book": "buch",
    "school": "schule",
    "food": "essen",
    "water": "wasser",
    "computer": "computer",
    "phone": "telefon",
    "cat": "katze",
    "dog": "hund",
    "family": "familie"
}

# App title
st.title("📘 English to German Dictionary")

# Text input
word = st.text_input("Enter an English word to translate:")

# Button
if st.button("Translate"):
    if word.lower() in english_to_german:
        st.success(
            f"The German translation of '{word.lower()}' is '{english_to_german[word.lower()]}'"
        )
    else:
        st.error("❌ Word not found in dictionary")
