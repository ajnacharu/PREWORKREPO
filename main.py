import random

#From chatbot0.1 by lagrassom on replit https://replit.com/@lagrassom/chatbot01#main.py

input('Welcome to Good Burger Home of the Good Burger, Can i take your order?')

def generate_response(user_input):
  responses = [
    "do you like bacon?",
    "Did you know all burgers come with a side of fries!",
    "Got it, Would you like a soda?",
    "Do you want cheese added?","Will that be all?"
  ]
  return random.choice(responses)
name = input('can i have a name for the order')

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, what would you like to order? We sell Burgers.\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()


