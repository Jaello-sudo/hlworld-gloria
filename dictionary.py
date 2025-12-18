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

print("📘 English to German Dictionary")
word = input("Enter an English word to translate: ").lower()

if word in english_to_german:
    print(f"The German translation of '{word}' is '{english_to_german[word]}'.")
else:
    print("❌ Word not found in dictionary.")
