import requests
from config import API_AIRVISUAL_KEY, API_AIRVISUAL_URI

# url = "api.airvisual.com/v2/nearest_city?lat=48.02&lon=-50.20&key={{YOUR_API_KEY}}"
# url = "https://api.airvisual.com/v2/nearest_city?lat=13.8081547&lon=100.5607044&key=997fd440-6a2e-48a9-9336-7cb0eaef4a99"
# API_AIRVISUAL_KEY="997fd440-6a2e-48a9-9336-7cb0eaef4a99"
# url = f"https://api.airvisual.com/v2/nearest_city?lat={lat}&lon={long}&key={API_AIRVISUAL_KEY}"


def getpm(lat: str = None, long: str = None):
    payload = {}
    headers = {}
    url = f"{API_AIRVISUAL_URI}/nearest_city?lat={lat}&lon={long}&key={API_AIRVISUAL_KEY}"

    session = requests.Session()
    # response = requests.request("GET", url.format(lat, long, API_AIRVISUAL_KEY), headers=headers, data=payload)
    response = session.get(url, headers=headers, data=payload)
    data = response.json()
    city = data['data']['city']
    state = data['data']['state']
    country = data['data']['country']
    pm_val = data['data']['current']['pollution']['aqius']
    temperature = data['data']['current']['weather']['tp']
    icon_weather = data['data']['current']['weather']['ic']
    # print(response.text.encode('utf8'))
    # print(city, state, country, val)
    return city, state, country, pm_val, temperature, icon_weather
