import requests

api_key ="df103dedc52382f2b61d6845b7c4f120"                           #'da47158cfc0322d909e6af7c8f9d134e'  
form_id ="241565311751048"                             #'241481344123044'    

#api_key = 'eb33e61edc8c029f46108130918fea49'
#form_id = '241555930905055'

url = f"http://eu-api.jotform.com/form/{form_id}/submissions?apiKey={api_key}"
#url = f'https://api.jotform.com/form/{form_id}/submissions?apiKey={api_key}'

api_words = []

response = requests.get(url)
data = response.json()

submissions = data.get('content', [])
#print(submissions)
for submission in submissions:
    answers = submission.get('answers', {})

    #print(answers)
    
# adjust '3' according to the actual key for the name question. print the data result
# first and observe the structure or test the output to the api in.This can be found in settings, advanced settings, fields and input_field
#  https://api.jotform.com/docs/#form-id-submissions

    name_answer = answers.get('8',{}).get('answer', 'No name provided')   
    #print(name_answer)
    api_words.append(name_answer)
    words = api_words

print(words)


