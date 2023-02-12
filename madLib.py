#MadLib Project

print('Information :\nA verb is an action.\nAn adverb usually ends in “ly” and describes an action (like slowly).\nA noun is a person/place/thing.\nAn adjective describes a person/place/thing.)\n')

person=input('Please type in the name of a person : ')
adjective=input('Please type in an adjective : ')
number=input('Please type in a number : ')
adverb=input('Please type in an adverb : ')
place=input('Please type in a place : ')
verb=input('Please type in an verb : ')
things1=input('Please type in some things (plural) e.g. socks : ')
animal=input('Please type in an animal : ')
emotion=input('Please type in an emotion : ')
things2=input('Please type in some things (plural) e.g. socks : ')

madLib=f'''\nWhenever I go shopping, I always feel {emotion}.
For example, last night I had to buy a birthday present for {person} so I went to \
The {things1} Emporium.
There must have been {number} other people also trying to buy {adjective} {things2}.
We were packed in so tight, I wasn't even able to \
{verb} like I usually do.
I quickly left the Emporium and picked up a {animal} from \
{place} instead. Maybe next year I'll find something better.'''

print(madLib)
