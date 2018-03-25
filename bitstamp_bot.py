import requests

def get_bot_updates(limit, offset):
    url = "https://api.telegram.org/bot560033881:AAGQigD1V0O6Q6PdScTiYUNqMzxHowT5FjY/getUpdates"
    params = {'limit': limit, 'offset': offset}
    result = requests.get(url, params=params)
    decoded = result.json()
    return decoded['result']

def send_message(chat_id, text):
    url = "https://api.telegram.org/bot560033881:AAGQigD1V0O6Q6PdScTiYUNqMzxHowT5FjY/sendMessage"
    params = {'chat_id':chat_id, 'text': text}
    requests.get(url, params=params)
    
def btcprice():
    url = 'https://www.bitstamp.net/api/v2/ticker/btcusd/'
    result = requests.get(url)
    decoded = result.json()
    return decoded['last']

def ethprice():
    url = 'https://www.bitstamp.net/api/v2/ticker/ethusd/'
    result = requests.get(url)
    decoded = result.json()
    return decoded['last']


btcp = btcprice()
ethp = ethprice()
    
update_result = get_bot_updates(5,0) 

for i in update_result:
       chat_id = i['message']['from']['id']
       answer = i['message']['text']
       last_update = i['update_id']

       if answer == '/btc':
           send_message(chat_id, btcp)

       elif answer == '/eth':
            send_message(chat_id, ethp)


       get_bot_updates(1, last_update + 1 )
