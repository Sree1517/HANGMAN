import random
import nltk
from nltk.corpus import words
from flask import Flask, render_template, request
nltk.download("words")

app = Flask(__name__)

random_word = random.choice([w for w in words.words() if len(w) == 5]).lower()
word_blank = ["_"] * len(random_word)
attempts_left = 8
guessed_letters = []

@app.route("/", methods=["GET", "POST"])
def home():
    global word_blank, random_word, attempts_left, guessed_letters

    message = ""  

    if request.method == "POST":
        guess = request.form.get("guess")
        if guess:
            guess = guess.lower()
            if guess in guessed_letters:
                message = f"You already guessed '{guess}'!"
            elif guess in random_word:
                for i in range(len(random_word)):
                    if random_word[i] == guess:
                        word_blank[i] = guess
                message = f"Good guess! '{guess}' is in the word."
            else:
                attempts_left -= 1
                message = f"Wrong guess! '{guess}' is not in the word."
            guessed_letters.append(guess)

    
    if "_" not in word_blank:
        message = f"Congratulations! You guessed the word: {random_word}"
    elif attempts_left <= 0:
        message = f"Game Over! The word was: {random_word}"

    return render_template(
        "index.html",
        word=" ".join(word_blank),
        attempts=attempts_left,
        guessed=", ".join(guessed_letters),
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
