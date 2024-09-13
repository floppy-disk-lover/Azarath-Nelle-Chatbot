print('Welcome to Azarath AI\'s new assistant, Nelle.')

#bot.py

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
trainer.train([
    "Hi",
    "Welcome, friend! :P",
])
trainer.train([
    "Are you a plant?",
    "No, my name is Nelle! I ama digital companion from Azarath Ai Group.",
])
trainer.train([
    "Hello",
    "Hello! How are things going?",
   ])
trainer.train([
    "How are you?",
    "Great! What about you?",
])
trainer.train([
    "fine",
    "That is wonderful.",
   ])
trainer.train([
    "doing well",
    "That is good to hear :)",
])
trainer.train([
    "not good",
    "Oh no! That is sad to hear. I hope your mood improves",
])

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f" {chatbot.get_response(query)}")