import requests
import csv

pic = []
price = []
property_type = []
pic_obj = []
price_obj = []

api_bridge_interactive = 'https://api.bridgedataoutput.com/api/v2/test/' \
                         'listings?access_token=b0acc9b69acb8bdfdec77dce31fc2ef2'

response = requests.get(api_bridge_interactive).json()

for k, v in response.items():
    if k == 'bundle':
        for el in v:
            price_obj = []
            for key, val in el.items():
                if 'ListPrice' in key and type(val) == int:
                    price_obj.append({key: val})
                if 'PropertyType' in key:
                    property_type.append({key: val})
                if 'Media' in key and val != None:
                    pic_obj = []
                    for e in val:
                        for km, vm in e.items():
                            if 'MediaURL' in km:
                                pic_obj.append(vm)
            pic.append(pic_obj)
            price.append(price_obj)

with open('objects.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(5):
        writer.writerow([pic[i], price[i], property_type[i]])

print("Writing complete 👍")

