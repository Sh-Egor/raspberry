import requests, json 
import lcd
import time
#543728 kotl

def weather(city_id):
    api_key = "81a77fe25629fa0937e8ebaf87df7bba"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&id=" + city_id +"&units=metric"
    try: 
        response = requests.get(complete_url)
        data = response.json()
        temp = data['main']['temp']
        cond = data['weather'][0]['main']
        return str(temp)+ 'C'
    
    except Exception as e:
        print("Exception (weather):", e)
        pass


LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0
LCD_CHR = True
LCD_CMD = False
lcd.lcd_init()
time.sleep(1)
lcd.lcd_byte(LCD_LINE_1, LCD_CMD)
lcd.lcd_string("Volgograd",2)
text = weather("472757")
print(text)
lcd.lcd_byte(LCD_LINE_2, LCD_CMD)
lcd.lcd_string(text,2)