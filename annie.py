import requests
import random
import json

moods = """
{
    "moods": [
        {"mood": "excited", "rating": 75},
        {"mood": "happy", "rating": 60},
        {"mood": "so-so", "rating": 50},
        {"mood": "sad", "rating": 30},
        {"mood": "miserable", "rating": 0},
        {"mood": "angry", "rating": 10}
    ]
}
"""

data = json.loads(moods)

#print(data["moods"])
#for mood in data["moods"]:
#    print(mood["mood"])
# print(json.dumps(moods, indent=4, sort_keys=True))

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
    if mood != 'happy' and mood != 'exited':
        print('I will cheer up your ' + mood + 'ness')
    joke(mood)
    affirmation(mood, name)

if __name__ == "__main__":
    name = input('what is your name: ')
    while True:
        mood = input('hello ' + name + ' how are you doing, happy, excited, bad, so-so or angry?: ')
        if mood == 'happy' or mood == 'excited':
            fine=input ( 'why are you feeling ' + mood + '?:' )		
            print( ' that is great.')
            cheer_up(mood,name)
            
            break
        elif mood == 'bad':
            fine=input ( 'why are you feeling ' + mood + '?:' )	
            print( 'sorry to hear that ' )
            cheer_up(mood, name)
            break
        elif mood == 'so-so':
            fine=input ( 'why are you feeling ' + mood + '?:' )
            print( 'I now understand ')
            cheer_up(mood, name)
            break
        elif mood == 'angry':
            fine = input ( ' why are you feeling '+ mood + '?:')
            print( 'touch each finger to your thomb while taking deep breaths ')
            cheer_up(mood,name)
            break
        else: 
            print('please,use happy, excited, bad, so-so or angry')


