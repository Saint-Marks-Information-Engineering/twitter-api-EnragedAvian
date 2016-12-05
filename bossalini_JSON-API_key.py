import requests											#importing requests library

from operator import itemgetter									#importing itemgetter library

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'					#defining URL from which to pull initial bit of information
r = requests.get(url)										#Assinging request return value to variable 'r'
print("Status code:", r.status_code)								#Printing status code associated with JSON query

submission_ids = r.json()									#Creating 'submission_ids' library which contains the JSON contents of the http request
submission_dicts = []										#Creating empty 'submission_dicts' array to be filled with various items later on
for submission_id in submission_ids[:30]:							#Cycling through the first 30 items in the submission_ids list
	url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')	#Retrieving more information about the specific article through the use of another JSON query
	submission_r = requests.get(url)							#Creating 'submission_r' which contains the JSON response for the specific article
	print(submission_r.status_code)								#Printing the status code associated with each article request
	response_dict = submission_r.json()							#Creating 'response_dict' which contains the JSON contents of the query from the article

	submission_dict = {									#Creating a new dictionary to hold selected information pulled from the larger 'response_dict'
		'title': response_dict['title'],						#Assigning a value for 'title' based upon the 'title' value retrieved from the JSON query
		'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),		#Creating link to the website using the submission ID
		'comments': response_dict.get('descendants', 0)					#Determining the number of comments on an article by looking for the key 'descendants' and if the key doesn't exist, returns a value of zero
		}
	submission_dicts.append(submission_dict)						#Adding the previously created 'submission_dict' to the submission_dicts library

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)		#Sorting the submission_dicts library by number of comments in reverse order

for submission_dict in submission_dicts:							#Printing various values for each item in the submission_dicts library
	print('\nTitle:', submission_dict['title'])
	print("Discussion link:", submission_dict['link'])
	print("Comments:", submission_dict['comments'])
