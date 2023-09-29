import requests
from datetime import datetime, timedelta
import numpy as np


latitude = 13.754
longitude = 100.5014
timezone = "Asia/Bangkok"

current_date = datetime.now()
one_week_from_now = current_date + timedelta(7)


current_day_str = current_date.strftime("%Y-%m-%d")
one_week_from_now_str = one_week_from_now.strftime("%Y-%m-%d")

api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone={timezone}&start_date={current_day_str}&end_date={one_week_from_now_str}"

try:
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        
        temp_array = data["hourly"]["temperature_2m"]
        hourly_array = data["hourly"]["time"]

        max_temp = np.max(temp_array)
        max_temp_index = np.argmax(temp_array)

        print(f"The highest temperature is {max_temp}°C at {hourly_array[max_temp_index]}")

       
        user_choice = input("Do you want to see all the days' weather hourly? (1 for yes, 2 for no): ")

        if user_choice == '1':
            # Print out all the weather info
            print("Weather Info for the next 7 days:")
            for i in range(len(temp_array)):
                print(f"Day: {hourly_array[i]}, Temperature: {temp_array[i]}°C")

    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
