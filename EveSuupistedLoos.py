import requests
import pandas
import json

page_id = "" #enter the post id from facebook API graph
post_id = "" #enter the page id from facebook API graph
access_token = "" #enter the facebook API acces token

url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'

response = requests.request("GET", url)

data = json.loads(response.text)

def get_comment(comment):
    return {
        'name': comment['from']['name'],
        'time': comment['created_time'],
        'message': comment['message']
    }

excel_data = list(map(get_comment, data["data"]))
df = pandas.DataFrame(excel_data)
df.to_excel('comments.xlsx', index=False)
