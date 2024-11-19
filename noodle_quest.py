import time
import math

def welcome_player():
    welcome_input = input("Welcome to Noodlequest! Would you like to begin?\n (y/n) ")
    if welcome_input.lower() == "y":
        name = input("What's your name?")
    elif welcome_input == "n":
        exit()
    return 


def scene_1():
    print("You get a call from Lord Farquaad.")
    # Here is where we put the ringtone
    pickup_input = input("Do you pick up?\n (y/n)")
    if pickup_input == "y":
        print("You must venture into the Italian Chinese food restaurant to acquire infinite Chinese food. I am starving and my 5 meals a day just won't do any longer. I will lend you a backpack chockablock with items pivotal to your journey, which are a Grappling Hook, a Flashlight, a Freddy Fazbear Watch, an SOS Reciever, and a bag of Cheezits. If you fail to complete within 48 hours, I will put you in the oven with the gingerbread man. Do you acquiesce?")
    elif pickup_input == "n":
        print("The call picks up regardless\n You must venture into the Italian Chinese food restaurant to acquire infinite Chinese food. I am starving and my 5 meals a day just won't do any longer. I will lend you a backpack chockablock with items pivotal to your journey, if you fail to complete within 48 hours, I will put you in the oven with the gingerbread man. Do you acquiesce?")
    begin_quest = input("(y/n)")


welcome_player()

scene_1()

