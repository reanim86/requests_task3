import requests
import time
from pprint import pprint

def get_question(list_number):
    current_date = time.time()
    two_days_ago = int(current_date) - 2 * (3600 * 24)
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'fromdate': two_days_ago,
        'order': 'desc',
        'sort': 'activity',
        'tagged': 'Python',
        'filter': 'default',
        'site': 'stackoverflow',
        'pagesize': 100,
        'page': list_number
        }
    response = requests.get(url, params=params)
    res_temp = response.json()
    return res_temp

if __name__ == '__main__':
    res = []
    number_list = 1
    answer_stackoverflow = get_question(number_list)
    res.extend(answer_stackoverflow['items'])
    while answer_stackoverflow['has_more']:
        number_list += 1
        answer_stackoverflow = get_question(number_list)
        res.extend(answer_stackoverflow['items'])
    pprint(res)
