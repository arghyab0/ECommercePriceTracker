import requests
from bs4 import BeautifulSoup
import smtplib

headers = {"User Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15'}

def check_price_Amazon():
	page = requests.get(URL,headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find(id="productTitle").get_text().strip()
	price = soup.find(id="priceblock_ourprice").get_text()
	nprice = float(price[0:5])
	print("\n\n",title)
	return nprice


def check_price_Flipkart():
	page = requests.get(URL,headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find("span", class_="_35KyD6")  
	price = soup.find("div", class_ ="_1vC4OE _3qQ9m1")
	nprice = float(price[0:5])
	print("\n\n",title)
	return nprice


def check_price_Snapdeal():
	page = requests.get(URL,headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	title = soup.find("h1", class_="pdp-e-i-head").get_text().strip()
	price = soup.find("span", class_="pdp-final-price").get_text()
	nprice = float(price[0:5])
	print("\n\n",title)
	return nprice

def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('[gmail username here]','[gmail password here]')
	subject = 'We found a lesser price!'
	body = 'The price fell down for the product you checked. Check the link:\n'+URL
	msg = f"Subject: {subject}\n\n{body}"
	server.sendmail('[gmail username here]','[destination email here]',msg)
	print("Email has been sent")
	server.quit()



choice = int(input("Enter the numeric choice corresponding to the e-commerce site you are using:\n1) Amazon\n2) Flipkart\n3) Snapdeal\n"))
URL = input("Enter the URL of the product you want to check the price of: ")
if choice==1:
	current_price = check_price_Amazon();
elif choice==2:
	current_price = check_price_Flipkart();
elif choice==3:
	current_price = check_price_Snapdeal();
else:
	print("Invalid choice")

min_price = float(input("Enter the minimum price below which you want to be notified: "))
if current_price < min_price:
	print("We found a lesser price !")
	send_email()












