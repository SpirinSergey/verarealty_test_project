from django.shortcuts import render
import requests


def index(request):
    return render(request, 'main/index.html')


def task_1(request):
    return render(request, 'main/task_1.html')

def task_2(request):
    return render(request, 'main/task_2.html')


def task_3(request):
    pic = []
    price = []
    property_type = []
    pic_obj = []
    price_obj = []
    obj = {}

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

    for i in range(5):
        obj[i] = [pic_obj[i], price[i], property_type[i]]
    return render(request, 'main/task_3.html', {'obj': obj})
