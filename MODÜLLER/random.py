import random
#result=dir(random)
#print(result)

#result=help(random)
#print(result)


result=random.random()*100
result=random.uniform(1,10) #1 ile 10 arasında sayı 
result=random.randint(1,100) #1 ile 100 arasında tam sayı


names=["ali","yağmur","deniz","cenk"]
result=names[random.randint(0,len(names)-1)]

result=random.choice(names)

greeting="hello three"
result=random.choice(greeting)

liste=list(range(10))
random.shuffle(liste)
result=liste
print(result)



