import requests				#importing requests library
url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC11PvrGPzo6Y7Zc6-e9cAKg&key=AIzaSyAOV6-TYOs7g8SySusCxDDWsbL9w4H9NmQ'
r = requests.get(url)			#assinging variable 'r' to the response from the JSON query
print("Status code:", r.status_code)	#Printing status code from JSON request
response_dict = r.json()		#Creating dictionary of the JSON response
print(response_dict.keys())		#Printing keys associated with response dictionary

items_dict = response_dict['items']

print(items_dict.keys())

statistics_dict = items_dict['statistics']

print(statistics_dict.keys())

#print(statistics_dict['subscriberCount'])




#print("Repositories returned:", len(repo_dicts))
#
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#        print(key)
#for repo_dict in repo_dicts:
#        print("\nSlected information about first repository:")
#        print('Name:', repo_dict['name'])
#        print('Owner:', repo_dict['owner']['login'])
#        print('Stars:', repo_dict['stargazers_count'])



