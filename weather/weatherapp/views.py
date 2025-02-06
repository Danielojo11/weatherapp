from django.shortcuts import render
from django.contrib import messages
import requests, datetime
# Create your views here.

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'lagos'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d8f6be824c6d61aefd4662b86a5ec6ea'
    PARAMS = {
        'units' : 'metric'
    }

    API_KEY = 'AIzaSyD6WY1KR9i60XoR4oF2NY4DC2V67wDIyZQ'
    SEARCH_ENGINE_ID = 'e1152c675c79f4497'

    query = city + '1920*1080'
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'images'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    

    try:
        data = requests.get(url, PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        return render(request, 'index.html', {'description' : description, 'icon' : icon, 'temp' : temp, 'day' : day, 'city' : city, 'exception_occured' : False})
    except:
        exception_occured = True
        messages.error(request, 'entered data is not a vailable to api')
        day = datetime.date.today()

        return render(request, 'index.html', {'description' : 'Clear Sky', 'icon' : '01d', 'temp' : 25, 'day' : day, 'city' : 'Lagos', 'exception_occured' : False,})
