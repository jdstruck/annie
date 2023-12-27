import random
take_how_many_down = 1
x = random.randint(1,100)
for i in reversed(range(1, x, take_how_many_down)):
    bottles = "bottle" if i == 1 else "bottles"
    print (f'{i} {bottles} of Fanta on the wall,\n{i} {bottles} of Fanta,\ntake {take_how_many_down} down')
    
    if i-take_how_many_down < 0:
        print("I can't because you drank all of my darn Fanta now I have to go to the store you dingus")
        exit()
    else:
        print(f'pass it around {i-take_how_many_down} bottles of Fanta on the wall\n\n')