import random

def chatbot():
    user_input = input("Olá, como posso ajudá-lo hoje? ")

    responses = ["Entendo", "Por favor, continue", "Isso é interessante", "Poderia me contar mais?"]

    while user_input != "sair":
        print(random.choice(responses))
        user_input = input()

chatbot()