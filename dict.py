from deep_translator import GoogleTranslator

print("===== English to Hindi Dictionary =====")

while True:
    word = input("\nEnter an English word (or type 'exit' to quit): ").strip()

    if word.lower() == "exit":
        print("Thank you for using the dictionary!")
        break

    try:
        meaning = GoogleTranslator(source='en', target='hi').translate(word)
        print(f"Hindi Meaning of '{word}': {meaning}")
    except Exception:
        print("Error! Please check your internet connection or try another word.")