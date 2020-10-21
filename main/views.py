from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests


# Create your views here.

def connect(request):
    print("Connected")
    return render(request=request,
                  template_name="main/default.html")


def get_wind_speed(request):
    print("before try")

    zip = request.GET['zip_value']
    print("Zipcode from the user" + zip)
    try:
        # http://api.http://api.openweathermap.org/data/2.5/weather?zip=28202&appid=548f8a02117b6433e211a2f4dd9435a8
        result = requests.get(url="http://api.openweathermap.org/data/2.5/weather",
                              params={"zip": zip,
                                      "appid": "548f8a02117b6433e211a2f4dd9435a8",
                                      "units": "imperial"})
        print(result)
        result_dic = result.json()
        wind_speed = result_dic['wind']['speed']
        city = result_dic['name']
    except Exception as e:
        wind_speed = "Error while retrieving data"

    return JsonResponse({"wind_speed": wind_speed,
                         "city": city})

