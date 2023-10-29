import requests

def affirmation(mood):
    pass

def joke(mood):
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': 'WZOemn9w2f5qCuzo7u6CPw==htMLruAKkRKenGrR'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

def cheer_up(mood):
	print('I will cheer up your ' + mood + 'ness')
	joke(mood)

name = input('what is your name: ')
age=input('what is your age ')
print('Hello, ' + age + ' year old ' + name )
while True:
	mood = input(name + ' how are you doing, good, bad, or so-so?: ')
	if mood == 'good':
		fine=input ( 'why are you feeling ' + mood + '?:' )		
		print( ' that is great')
		break
	elif mood == 'bad':
		fine=input ( 'why are you feeling ' + mood + '?:' )	
		print( 'sorry to hear that ' )
		# TODO: if mood =bad or so-so cheer user up 
		#      cheer user up by printing positive affirmations
		cheer_up(mood)
		break
	elif mood == 'so-so':
		fine=input ( 'why are you feeling ' + mood + '?:' )
		print( 'I now understand ')
		cheer_up(mood)
		break
	else: 
		print('please,use good,bad or so-so')


