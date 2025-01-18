import requests
from datetime import datetime, timedelta
def get_prices():
    response = requests.get(API_URL)
    data = response.json()
    print("data received")
    
    
    prices = []
    current_time = datetime.now()
    for price_data in data['prices']:
        time_to_str = datetime.strptime(price_data['startDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
        time_to_str = time_to_str + timedelta(hours=2)
        if time_to_str > current_time: 
            fixed_time = time_to_str.strftime("%d.%m% Klo: %H:%M")
            #print(price_data['price'],"c/KwH", fixed_time)
            prices.append((price_data['price'], fixed_time))
            
    cheapest_hours = sorted(prices, key=lambda x: x[0])[:5]
    
    print("\n Cheapest 5 upcoming hours: \n")
    for i, (price, time) in enumerate(cheapest_hours, 1):
        print(f"{i}. {time} - {price} c/KwH" )
        
    
            
    
get_prices()

