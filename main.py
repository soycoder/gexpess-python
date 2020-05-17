import requests
import json

def gsheetapi(method):
    sheetID = "AKfycbwZcZ9zFkyVMoNaJcU-1xwAHtVTeTP8JRfLQnWlXPxVuNis0k2B"
    path = "/2aqi"
    method = method
    url = "https://script.google.com/macros/s/"+sheetID+"/exec?path=" + \
        path + "&method=" + method

    datetime = "2020-5-17"
    light = 54621
    temp = 40
    humi = 30
    pressure = 1500
    rain = 2
    o3 = 0.2
    no2 = 0.0
    co = 0.2
    so2 = 0.0
    ws = 5
    wdi = 128

    x = {
        "datetime": datetime,
        "light": light,
        "temp": temp,
        "humi": humi,
        "pressure": pressure,
        "rain": rain,
        "o3": o3,
        "no2": no2,
        "co": co,
        "so2": so2,
        "ws": ws,
        "wdi": wdi
    }

    # convert into JSON:
    payload = json.dumps(x)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text.encode('utf8'))
    print(res)

if __name__ == "__main__":
    gsheetapi("PUT")
