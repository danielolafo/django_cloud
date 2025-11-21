import time

#from django.shortcuts import render
from rest_framework.views import APIView
#import requests
import nest_asyncio; nest_asyncio.apply()  # This is needed to use sync API in repl
from playwright.sync_api import sync_playwright
from django.http import HttpResponse

# Create your views here.
class Airlines(APIView):

    url_sample='https://www.despegar.com.co/shop/flights/results/roundtrip/BOG/ROM/2025-11-19/2025-11-29/1/0/0?from=SB&di=1'
    url = 'https://www.despegar.com.co/shop/flights/results/roundtrip/{ORIGIN}/{TARGET}/{DEPARTURE}/{RETURN}/1/0/0?from=SB&di=1'
    url_kayak='https://www.kayak.com.co/flights/BOG-ROM/2025-11-21/2025-11-29/3adults?ucs=13wdrlj&sort=bestflight_a'
    def get(self, search_params):
        cont = ''
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="chrome")
            page = browser.new_page()
            page.goto(self.url_kayak) #("https://www.us.despegar.com/")
            #time.sleep(1)
            print(page.__dict__)
            print(page.content())
            print('************************')
            print(page)
            cont = page.content()
            browser.close()
        return HttpResponse(cont) #('SCRAPPED SITE OK')