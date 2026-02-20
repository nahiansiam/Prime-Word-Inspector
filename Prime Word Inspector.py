# ==========================================
# Project: Prime Word Inspector
# Created by: (Nahian Kabir Siam)
# ==========================================

import string
import datetime

def display_intro():
    print("\n" + "="*45)
    print("        PRIME WORD INSPECTOR")
    print("="*45)
    print("Analyze your text in a smart way!\n")
    print("Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-"*45)

def clean_text(text):
    # Remove punctuation using custom logic
    for symbol in string.punctuation:
        text = text.replace(symbol, "")
    return text

def analyze_text(text):
    cleaned = clean_text(text)

    words = cleaned.split()
    word_count = len(words)
    char_with_spaces = len(text)
    char_without_spaces = len(text.replace(" ", ""))
    sentence_count = text.count('.') + text.count('!') + text.count('?')

    return word_count, char_with_spaces, char_without_spaces, sentence_count

def main():
    display_intro()

    while True:
        print("\nChoose an option:")
        print("1. Analyze new text")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            user_text = input("\nEnter your paragraph:\n> ")

            if len(user_text.strip()) == 0:
                print("⚠ You entered empty text!")
                continue

            results = analyze_text(user_text)

            print("\n--- Analysis Result ---")
            print("Total Words:", results[0])
            print("Characters (with spaces):", results[1])
            print("Characters (without spaces):", results[2])
            print("Total Sentences:", results[3])
            print("------------------------")

        elif choice == "2":
            print("\nThank you for using Prime Word Inspector!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()