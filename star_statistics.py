import re
import json
import requests

def getStarStatistic():
    url = 'https://shopee.vn/Gel-r%E1%BB%ADa-m%E1%BA%B7t-v%C3%A0-t%E1%BA%AFm-Effaclar-Micro-Peeling-Purifying-La-Roche-Posay-400ml-i.37251700.7041040114'

    r = re.search(r'i\.(\d+)\.(\d+)', url)
    shop_id, item_id = r[1], r[2]
    ratings_url = 'https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=1&itemid={item_id}&limit=20&offset={offset}&shopid={shop_id}&type=0'

    offset = 0
    d1=0
    d2=0
    d=[]
    while True:

        data = requests.get(ratings_url.format(shop_id=shop_id, item_id=item_id, offset=offset)).json()

        # uncomment this to print all data:
        #print(json.dumps(data, indent=4))
        #leng enumerate tra ket qua duoi dang liet ke
        i = 1
        for i, rating in enumerate(data['data']['ratings'], 1):
            if (str(rating['rating_star']) == '5'):
                d1=d1+1
            else:
                d2=d2+1

        if i % 20:
            break

        offset += 20
    d.append(d1)
    d.append(d2)
    return d