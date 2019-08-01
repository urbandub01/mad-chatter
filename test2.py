
# import urllib.request
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts = dict()
# for line in fhand: 
#     words = line.decode().split() 
# for word in words: 
#     counts[word] = counts.get(word, 0) + 1 
# print(counts) 

# exit()


import nltk   
##from urllib import urlopen
import urllib.request
from bs4 import BeautifulSoup

#url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
#url = "http://data.pr4e.org/romeo.txt"
url = "https://www.rd.com/culture/random-trivia-never-knew/"
html = urllib.request.urlopen(url).read()    
soup = BeautifulSoup(html)





# url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
# html = urllib3.urlopen(url).read()
# soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)



exit()
##random number generator
def random_func(x):
   for i in range(1):
      rand_no =  random.randint(0,5)
      







##define progress bar
import time
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


##random number generator
def random_func(x):
   for i in range(1):
       rand_no =  random.randint(0,5)

random_no = random_func(i)

print(random_no)
exit()



#---------------------------------------


from colorama import init
import time
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
time.sleep(0.3)
print(Fore.BLUE + 'some blue text text')
exit()

#-------------------------------------

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

exit ()