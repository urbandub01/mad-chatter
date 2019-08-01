

import time
import random
import os


random_name = (
"hello, my name is RAD, what's your name? "
,"Oops, I was on mute, who's there? "
,"*Ding-dong, knock knock, who's at the door? "
,"RAD is the name, chatting is the game, so who you might be? "
,"To whom do I owe the pleasure of this chat? "
,"Name please? ")

greeting_positive = (
"good"
,"cool"
,"awesome"
,"wicked!"
,"feeling good"
,"all right!")

rand = random.Random()
rand_no = round(rand.uniform(0,5))

#var_name = random_questions[rand_no]
var_name = random_name[rand_no]
var_prefix = greeting_positive[rand_no]


var1 = input(var_name)

for i in var1:
    print(i, end='', flush=True)
    time.sleep(0.1)
print('\n')

print(f"how are u today? ")

