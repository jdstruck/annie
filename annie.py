import requests
import random

def affirmation(mood, name):
    affirmations= [
        "you look very nice today " + name,
        "i hope you have a good day",
        "you are a kind person",
        "you are funny",
        "you are smart"
    ]
    affirmations_length = len(affirmations)
    randomnum = random.randrange(affirmations_length)
    print(affirmations[randomnum])

def joke(mood):
    print('here is a joke...')
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'WZOemn9w2f5qCuzo7u6CPw==htMLruAKkRKenGrR'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

def cheer_up(mood, name):
    print('I will cheer up your ' + mood + 'ness')
    joke(mood)
    affirmation(mood, name)

def main():
    name = input('what is your name: ')
    # age=input('what is your age ')
    # print('Hello, ' + name )
    while True:
        mood = input('hello ' + name + ' how are you doing, good, bad, or so-so?: ')
        if mood == 'good':
            fine=input ( 'why are you feeling ' + mood + '?:' )		
            print( ' that is great')
            break
        elif mood == 'bad':
            fine=input ( 'why are you feeling ' + mood + '?:' )	
            print( 'sorry to hear that ' )
            # TODO: if mood =bad or so-so cheer user up 
            #      cheer user up by printing positive affirmations
            cheer_up(mood, name)
            break
        elif mood == 'so-so':
            fine=input ( 'why are you feeling ' + mood + '?:' )
            print( 'I now understand ')
            cheer_up(mood, name)
            break
        else: 
            print('please,use good,bad or so-so')

main()

