
##define progress bar
import time
import random
import csv
import time

##load random questions
with open('random_questions.csv', 'r') as f:
  reader = csv.reader(f)
  random_questions  = list(reader)

import re
list = random_questions
random_questions = re.sub('[\[\]]','',repr(list))


##random number generator
def random_func(x):
   for i in range(1):
      rand_no =  random.randint(0,5)
      



#print(random_questions)
#exit()
my_dict = {}

random_name = (
"hello, my name is RAD, what's your name? "
,"Oops, I was on mute, who's there? "
,"*Ding-dong, knock knock, who's at the door? "
,"RAD is the name, chatting is the game, so who you might be? "
,"To whom do I owe the pleasure of this chat? "
,"Name please? ")


random_address = (
"So where's home for you? "
,"Where's your house located? "
,"What's your address? "
,"Do you live far from here? so where? "
,"Are you from the city, where are you from exactly? "
,"Country or residence please? ")


random_sports = (
"What sports do you play? "
,"I play basketball, what sports do you play? "
,"Keeping my self in shape by lifting weights, which sports do you play to keep fit? "
,"Is there any sports you like? "
,"I just bought these NIKEs for running, which sports do you do? "
,"I love biking, what about you? ")

random_movie = (
"Which movie is your favorite? "
,"I like movies, my favorite is Ready player one, which one is your favorite? "
,"Do you have a favorite movie? "
,"I like going to the cinema, what movies have you watched lately? "
,"about movies do you like watching? What's your favorite? "
,"Man do you go to movies? What's top of your list? ")

random_yes_no_joke = (
"Do you want me to tell you a joke? "
,"Wanna hear a joke? "
,"You seem bored, wanna hear a joke!? "
,"I forgot to tell you i'm funny, wanna hear me crack a joke? "
,"I can tell you a joke if you want? "
,"You want to know how funny I can be? wanna hear a joke? ")


greeting_positive = (
"good","yep","o.k."
,"cool", "sure"
,"awesome"
,"wicked!"
,"go ahead"
,"all right!")

affirmative = ["yes","yup","ok"
,"fine","absolutely","alright","sure"
,"go ahead","alright","o.k.","awesome!"
]

rand = random.Random()
rand_no = round(rand.uniform(0,5))

#var_name = random_questions[rand_no]
var_name = random_name[rand_no]
var_prefix = greeting_positive[rand_no]


var1 = input(var_name)
my_dict['name'] = var1
time.sleep(0.5)

for i in var1:
    print(i, end='', flush=True)
    time.sleep(0.1)
print('\n')

print(f"How are u today? ")
time.sleep(0.5)

var_address = random_address[rand_no]
##var2 = input(f"{var_prefix} "+ my_dict['name'] + ", " +var_address)
var2 = input(var_address)
my_dict['address'] = var2
time.sleep(0.5)


var_sports = random_sports[rand_no]
var3 = input(f"{var_prefix} seems like "+ my_dict['address']+ " is a nice place. "+ var_sports)
my_dict['sports'] = var3
time.sleep(0.5)

var_movies = random_movie[rand_no]
var4 = input(f"That's a really {var_prefix} hobby "+my_dict['name']+ " So I'm curious "+ var_movies)
my_dict['movies'] = var4
time.sleep(0.5)

print("That's an interesting movie")
time.sleep(0.5)

var_joke_ask = random_yes_no_joke[rand_no]
var4 = input(var_joke_ask)

if var4 in affirmative:
   input("Why did the chicken cross the road? ")
   time.sleep(0.5)
   print(f"To get to the other side!!! HAHAHA ", end ='', flush = True)
else:
   print(f"ok, you're stubborn guy!")
time.sleep(0.2)

print(f"goodbye!")
exit()






#_____________________________________________________________________





if "name" in varq:
   my_dict['name'] = var1
   print (f"im glad to meet you"+my_dict['name'])
elif "from" in varq:
   my_dict['address'] = var1
   print (f"oh so is "+my_dict['address']+" a nice place?")
elif "sports" in varq:
   my_dict['fav_sports'] = var1
   print (f"I don't play "+my_dict['fav_sports']+" but i do play soccer")
elif "away" in varq:
   my_dict['get_lost'] = var1
   print (f"I don't want to anyone right now! ")




#_____________________________________________________________________

# import csv
# from itertools import chain

# with open('nice_words.csv', 'r') as f:
#    reader = csv.reader(f)
#    good_expressions = list(reader)
#    #good_expressions = list(chain(reader))
#    #good_expressions =str(good_expressions)[1:-1]

# ##print(your_list)


# import re
# list = good_expressions
# string = re.sub('[\[\]]','',repr(list))
# print(string)

# #good_expressions  = list(reader)
# #good_expressions  = list(chain(good_expressions))

# #print(good_expressions)