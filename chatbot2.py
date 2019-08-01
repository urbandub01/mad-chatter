
##define progress bar
import time
import random
import csv
import time
import colorama
from colorama import init
from colorama import Fore, Back, Style
init()

##load random questions
with open('random_questions.csv', 'r') as f:
  reader = csv.reader(f)
  random_questions  = list(reader)

import re
list = random_questions
random_questions = re.sub('[\[\]]','',repr(list))


my_dict = {}

from questions import *

rand = random.Random()
rand_no = round(rand.uniform(0,5))

#var_name = random_questions[rand_no]
var_name = random_name[rand_no]
var_prefix = greeting_positive[rand_no]


var1 = input(var_name)
my_dict['name'] = var1

for i in var1:
    print(i, end='', flush=True)
    time.sleep(0.1)
print('\n')

var_greeting = greeting_positive[rand_no]
print(var_greeting)
time.sleep(0.5)

var_address = random_address[rand_no]
##var2 = input(f"{var_prefix} "+ my_dict['name'] + ", " +var_address)
var2 = input(var_address+"\n")
my_dict['address'] = var2
time.sleep(0.5)

var_sports = random_sports[rand_no]
var3 = input(f"{var_prefix} seems like "+ my_dict['address']+ " is a nice place. "+ var_sports+"\n")
my_dict['sports'] = var3
time.sleep(0.5)

var_movies = random_movie[rand_no]
var4 = input(f"That's a really {var_prefix} hobby "+my_dict['name']+ " So I'm curious "+ var_movies+"\n")
my_dict['movies'] = var4
time.sleep(0.5)

print("That's an interesting movie")
time.sleep(0.5)
print(Fore.RED+"Ok...")
time.sleep(0.5)

var_joke_ask = random_yes_no_joke[rand_no]
var4 = input(var_joke_ask+"\n")


if var4 in affirmative:
   
   var_joke1 = random_jokes[rand_no]
   input(var_joke1+"\n")
   time.sleep(0.5)
   var_punch1 = random_jokes_punchline[rand_no]
   print(Fore.BLUE+var_punch1+ " HAHAHAHA!")
   time.sleep(0.5)

else:
   print(Back.YELLOW+f"ok, you're stubborn guy!")
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