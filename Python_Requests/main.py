
import requests
from time import sleep
product_urls = []

offset = 0
size = 24


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
    "Content-Length": "453",
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://www.ikea.com",
    "Priority": "u=1, i",
    "Referer": "https://www.ikea.com/",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Session-Id": "bf85c069-0510-4780-ba4d-42cbdb99989b",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

payloads = [
    {"searchParameters":{"input":"10661","type":"CATEGORY"},"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a","sik_null_test_20240710_default":"b"},"isUserLoggedIn":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"sort":"RELEVANCE","window":{"offset":24,"size":24},"variantConfigs":None}]},
    {"searchParameters":{"input":"10662","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"16238","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"10663","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":12,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"20926","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"21825","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":12,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"25219","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"19145","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_fe_null_test_12122023":None,"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"variantConfigs":None,"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"20864","type":"CATEGORY"},"optimizely":{"listing_2785_mattress_text_variants":"a","sik_null_test_20240710_default":"b"},"isUserLoggedIn":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"sort":"RELEVANCE","window":{"offset":24,"size":24}}]},
    {"searchParameters":{"input":"20864","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"16284","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"25205","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"16285","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"45781","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"forceFilterCalculation":True}]},
    {"searchParameters":{"input":"19064","type":"CATEGORY"},"isUserLoggedIn":False,"optimizely":{"listing_2785_mattress_text_variants":"a"},"experimentalVariantGroups":False,"components":[{"component":"PRIMARY_AREA","columns":4,"types":{"main":"PRODUCT","breakouts":["PLANNER","LOGIN_REMINDER","MATTRESS_WARRANTY"]},"filterConfig":{"max-num-filters":4},"window":{"size":24,"offset":0},"forceFilterCalculation":True}]}
]
for payload in payloads:
    while True:
        response = requests.post("https://sik.search.blue.cdtapps.com/co/es/search?c=listaf&v=20240110", headers=headers, json=payload)
        print(response.status_code)
        data = response.json()
        
        products = data["results"][0]["items"]

        
        for product in products:
            product_url = product["product"]["pipUrl"]
            product_urls.append(product_url)

        offset += size
        
        
        if len(products) < size:
            break
        
        sleep(10)

    print("---------------Extracted Product URLS successfully------------------")

