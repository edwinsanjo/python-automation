from playwright.sync_api import sync_playwright
import threading
import time

product = [{'link':"https://www.amazon.in/HARLEY-DAVIDSON-Motorcycle-Metallic-booking-Ex-Showroom/dp/B0FDGWRMMN/?_encoding=UTF8&ref_=pd_hp_d_btf_ls_gwc_pc_en4",'history':[]}]
pricehistory = []
interval = 5

def get_amazon_price(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        page.goto(url["link"])
        
        price_selector = ".a-price-whole"
        page.wait_for_selector(price_selector)
        
        price = page.locator(price_selector).first.inner_text()
        price = str(price).rstrip("\n.")

        url["history"].append({"price":price, "time":time.time()})
        
        browser.close()

def menu():
    print("-=====-Price Tracker-=====-")
    print("1. Add to tracking list.")
    print("2. View raw data.")
    print("3. change interval of price query.")


def loop1():
    while True:
        for i in product:
            print()
            get_amazon_price(i)
        time.sleep(interval)

t1 = threading.Thread(target=loop1).start()

while True:
    menu()
    i = int(input("\nChoose an Option"))
    if(i==1):
        link = str(input("\nEnter Your amazon Link:\n"))
        product.append({'link':link,'history':[]})
    if(i==2):
        print(product)
    if(i==3):
        inter = int(input(f"current interval: {interval}\nEnter your interval in seconds:"))
        if inter <= 3 or inter >=1000000:
            continue
        interval = inter