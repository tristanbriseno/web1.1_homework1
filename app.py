from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"

@app.route('/triple/<user_word>')
def triple_word(user_word):
    """Outputs user word three times"""
    triple_word = (user_word + ' ') * 3
    return triple_word

@app.route('/penguins')
def show_penguins():
    """Shows a message about penguins to the user"""
    return "Penguins are cute!"

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Shows a message with user's animal"""
    return f"Wow, {users_animal} is my favorite animal, too!"

@app.route('/dessert/<users_dessert>')
def favorite_desert(users_dessert):
    """Shows a message with user's dessert"""
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    """Shows a silly story based on words the user enters"""
    return f"The silly old goat rammed into the {adjective} {noun}."

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiplies two numbers user enters"""
    if number1.isdigit() and number2.isdigit():
        product = int(number1) * int(number2)
        return f"{number1} times {number2} is {product}."
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Repeats user's word amount of times as number entered"""
    if n.isdigit():
        for words in range (int(n)):
            string = f"{word} " * int(n)
    return string

@app.route('/reverse/<users_word>')
def reverse_word(users_word):
    """Takes user's word and reverses it"""
    result = users_word[::-1]
    return result

# Thank you to vik on StackOverflow for responding to a question regarding how to do this - my solution is largely based on his
@app.route('/strangecaps/<user_word>')
def make_strangecaps(user_word):
    """Makes user's word appear in alternating caps"""
    result = ''
    caps = True
    for char in user_word:
        if caps:
            result += char.upper()
        else:
            result += char.lower()
        if char != '':
            caps = not caps
    return result

@app.route('/dicegame')
def dicegame():
    diceroll = random.randint(1, 6)
    """Rolls a die for the user - they win if it rolls six!"""
    win_status = 'lost'
    if diceroll == 6:
        win_status = 'won'
    else:
        win_status = 'lost'
    return f"You rolled a {diceroll}, you {win_status}!"



if __name__ == "__main__":
    app.run(debug=True)