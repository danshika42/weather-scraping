import smtplib
import requests
import json
from bs4 import BeautifulSoup
import os

os.chdir(r"C:\Users\91859\weather-scraping")

if __name__=="__main__":
	
	with open('data.json', 'r') as f:
		data = json.load(f)
	city = "Ghaziabad"
	url = "https://www.google.com/search?q=" + "weather" + city

	html = requests.get(url).content
	soup = BeautifulSoup(html, 'html.parser')

	temperature = soup.find('div',attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
	time_sky = soup.find('div',attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
	
	sky = time_sky.split('\n')[1].lower()
	if "rain" in sky:
		smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
		smtp_object.starttls()
		smtp_object.login(data["GMAIL_ID"],data["GMAIL_PSWD"])
		
		subject = "Rain Alert!!"
		body = f"Take an umbrella before leaving ☔.\n\nWeather condition for today is {sky.upper()} and temperature is {temperature} in {city}."
		msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nAnshika Dubey".encode('utf-8')
	
		smtp_object.sendmail("danshika42@gmail.com","danshika42@gmail.com", msg)

		smtp_object.quit()
		print("Email Sent!")
	else:
		print("not rainy")


