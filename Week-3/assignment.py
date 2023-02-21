#create an empty list of favourite musicians
#favourite_musicians = []
#using for loop add 5 new musicians
#copy to a new list called celeb
#sort the list
#pop out two celebrities from the list
#count the remaining celebrities in the list
my_favourite_musicians = []



favourite_musicians = ["Jayzee","offset","Niki","Meghan","Kiki"]
for musician in favourite_musicians:
    print(musician)
my_favourite_musicians.append("Sam Smith")
for musician in favourite_musicians:
    print(musician)


celeb = my_favourite_musicians.copy()
print(celeb)

celeb.sort()
print(celeb)


celeb.pop()
print(celeb)
print(len(celeb))