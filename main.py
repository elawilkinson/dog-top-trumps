## IMPORTING API

import requests
response_API = requests.get('https://api.thedogapi.com/v1/breeds')


## STARTING THE GAME
name = input("Hello dog lover! What is your name?")
played = int(input("{}, how many times have you played this game before?".format(name)))

if played <1:
 print("First time? Welcome!")
 print("Instructions: pick your dog, pick your characteristic and hope to beat the computer's pick!")
elif played >1:
 print("Welcome back! Best of luck.")

print("Let's start!")


## IMPORTING LIBRARIES
import random
import requests


## USING DOG API LIBRARY TO GET STATISTICS
def random_dog():
   dog_number = random.randint(1, 200)
   url = "https://api.thedogapi.com/v1/breeds/{}".format(dog_number)
   headers = {"Accept": "70d00ebf-b2fa-493a-bd63-a84eab2ec567"}
   response = requests.get(url,headers)
   dog = response.json()

   return {
       'name':dog['name'],
       'id':dog['id'],
       'life_span':dog['life_span'],
       'height': dog['height']['imperial'],
       'weight': dog['weight']['imperial']
   }


## BLOCK OF GAME CODE TO REPEAT
def top_trumps():

    my_dog = random_dog()
    opponent_dog=random_dog()

    print("Your dog for this round is...")
    print("a {}".format(my_dog['name']))

    ## STICK OR TWIST?
    dog_switch = input("How do you feel about that? Would you like to stick (s) or twist (t)?")

    new_dog = random_dog()

    if dog_switch == 's':
        print("Great. Loyalty. We love to see it.")
    if dog_switch == 't':
        print("Your {} is extremely sad about your decision".format(my_dog['name']))
        print("But we can reveal that your new breed is...")
        print("The mighty {}".format(new_dog['name']))
        my_dog = new_dog


    ## WHICH VALUE WOULD YOU LIKE TO COMPETE ON?
    stat_choice = input("What characteristic of this breed would you like to select? (life_span, height, weight)")
    print('{} selected. Loading details...'.format(stat_choice))
    print("Your opponent dog breed is a {}".format(opponent_dog['name']))
    print("Comparing their {} ...".format(stat_choice))


    ## COMPETITION & RESULTS
    # LIFE SPAN
    if stat_choice == 'life_span':
        life_val = my_dog['life_span'].split(' -')
        single_val = int(life_val[0])
        print('Your breeds life span is {} years'.format(single_val))
        op_life = opponent_dog['life_span'].split(' -')
        op_single = int(op_life[0])
        print('Your opponents life span is {} years'.format(op_single))
        if single_val > op_single:
            print("This can only mean...")
            print("Your dog won!")
        elif op_single > single_val:
            print("This can only mean...")
            print("Sorry - your opponent dog won this round")
        else:
            print("This can only mean...")
            print("DRAW!")
    # HEIGHT
    elif stat_choice == 'height':
        heightr = my_dog['height'].split(' -')
        height_val = int(heightr[0])
        print('Your breeds height is {} inches'.format(height_val))
        op_heightr = opponent_dog['height'].split(' -')
        op_height = int(op_heightr[0])
        print('Your opponents height is {} inches'.format(op_height))
        if height_val > op_height:
            print("This can only mean...")
            print("Your dog won!")
        elif op_height > height_val:
            print("This can only mean...")
            print("Sorry - your opponent dog won this round")
        else:
            print("This can only mean...")
            print("DRAW!")
    elif stat_choice == 'weight':
        weight_r = my_dog['weight'].split(' -')
        weight_val = int(weight_r[0])
        print('Your breeds weight is {} pounds'.format(weight_val))
        op_weightr = opponent_dog['weight'].split('-')
        op_weight = int(op_weightr[0])
        print('Your opponents weight is {} pounds'.format(op_weight))
        if weight_val > op_weight:
            print("This can only mean...")
            print("Your dog won!")
        elif op_weight > weight_val:
            print("This can only mean...")
            print("Sorry - your opponent dog won this round")
        else:
            print("This can only mean...")
            print("DRAW!")

## LOOP
play = True
count = 1

while play:
    top_trumps()
    again = str(input("Do you want to play again, type yes or no "))
    if again == "no":
      play = False
      print("The dogs are sorry to see you go but they hope you have a woofly day.")
    elif again == "yes":
      print("Good choice, the dogs will be pleased!")
      play = True







