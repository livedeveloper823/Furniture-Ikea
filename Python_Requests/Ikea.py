import json, requests
from bs4 import BeautifulSoup
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
    
product_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "ikea_geo=SG; MV_FAVOURITES_GUEST_ID=01ef402e-356a-1f5d-a67b-798039510ac6; MV_FAVOURITES_GUEST_PROVIDER=IRW; MV_CART_GUEST_ID=01ef402e-356a-1f5d-a67b-798039510ac6; MV_CART_GUEST_PROVIDER=IRW; OptanonAlertBoxClosed=2024-06-12T16:41:51.086Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+13+2024+02%3A41%3A51+GMT%2B1000+(Vladivostok+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3b08df7c-abcf-496a-b526-b26e59cf033f&interactionCount=3&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false; ikexp_id=87a34c11-77b7-4d21-8817-fca438acff9f; episod_id=1718004986993.sjupdv9m; _ga=GA1.1.1170101640.1718004988; _cs_ex=1677167115; _cs_c=1; ikea_cookieconsent_co=%7B%221%22%3Atrue%2C%222%22%3Atrue%2C%223%22%3Atrue%2C%224%22%3Atrue%7D; interIkeaConsent=v1.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+21+2024+15%3A49%3A49+GMT%2B1000+(Vladivostok+Standard+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=9849c3f4-53f6-478f-8441-c0c9d1bc46cd&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CC0003%3A0&AwaitingReconsent=false; ikea_cookieconsent_sg=%7B%221%22%3Atrue%2C%22showBanner%22%3Atrue%7D; _ld={'_ga':'1.1170101640.1718004988'};_ga_09FLM65N58=GS1.1.1719061953.18.0.1719061953.0.0.0; WC_PERSISTENT=MDFlZjQwMmUtMzU2YS0xZjVkLWE2N2ItNzk4MDM5NTEwYWM2fGNv; WC_AUTHENTICATION_01ef402e-356a-1f5d-a67b-798039510ac6=MDFlZjQwMmUtMzU2YS0xZjVkLWE2N2ItNzk4MDM5NTEwYWM2fGNv; JSESSION_ID=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIwMWVmNDAyZS0zNTZhLTFmNWQtYTY3Yi03OTgwMzk1MTBhYzYiLCJpYXQiOjE3MjA3NjgwMzcsImV4cCI6MTcyMzM2MDAzN30.HRo4XbhUrQNHvnwtElYgAhsmBSVrCnwy8rhQV14cpZE7D8JC5sk4_Km71hy3HgzINqNca-XMKlsckvzM9-YIrQ; WC_SESSION_ESTABLISHED=true; WC_ACTIVEPOINTER=ZXN8Y28=; WC_USERACTIVITY_01ef402e-356a-1f5d-a67b-798039510ac6=ZXN8Y28=; _fbp=fb.1.1721153974244.1858530988; PIM-SESSION-ID=bOtahdBl072wTCJs; akacd_PIM-prd_ah_rollout=3898610906~rv=52~id=5f21f00b07849dc3c1cc2e3f1666cae3; bm_sz=4DF7A889D9EC0F617AAA0060693CB456~YAAQF/AgF+EkZL2QAQAAJyG5vhgeefowxfxScIrSV1blgtf0uSRncXswWWTKKU2DgqjSZKdOmCquUnUiYovzpbIZmswT44qmKbKonfwGEDKRXYJbJRB0dRLq4biPZ+KAguvPMYnfgdDCTihemBHTevX+Op0FWDQYV7V8afLDKMG2mFFcq3Xfk28l01dIGCc/eWmmy7s3FVfG9e83xiaeqg0TjBkSV1j6YcQ1AfgPspwD6C0XIP19LFUR/yTIYn0ua4WDUcZKpGswQrb3z2Sq71hKr5FtneZcYVvC8kBg1fkbG7I7T+sskdOLlKnASJ/eUc/iPP0JdxKHcsGQD7H6mF4omM63LK8Ih7AtdAJK5R6nY8P0NnfkEGlpl13dSEc45BQNeOp67KtoCQQeFEM=~3293507~3425591; FPGSID=1.1721187092.1721187092.G-S4EX53B760.CW7GoeJ5RT504o8XSthAGg; ak_bmsc=1AA433B6F513B883986FF2528487319C~000000000000000000000000000000~YAAQHvAgF0ZX+7aQAQAAtdy+vhjNGdSs713AxS0o/HDHaeSOQLqGONyoi4lIlr/oPhnPM78UNaYdhvSZmBwOH9wxttVoY4w0awiiNIIfCK/AZMSm12QxLtovukCRltr0L7agr8D7bQdLWW5/R6G7QPVWTYi0SU1XAtdXVx+WBWqXgx1zmP+aXrocu4AZNFfTHavJeLjMDIhRZMCBll3FQnmxlPZRzb4LeYk/lSgqwDzb+2jSlPuzDrTAxCAWb90MQZ8aC42we+/+nExlByfxAkoO37XVPX3PrNdbmOikmb/EQ2brri5CGHtpr7sc8izSkbzlZjN52SNhqL0mPwS7XIkYN/OkdydTXQmqTxMNFbXsGAZErgBpcNUezQf7L/K6hv5zwiCqp88s7IrNPJ1M17XIbCIa1rqhE9cagf753AvAsMJzPTkz7fJWERC1U8eRPxF/Pw==; _cs_mk_ga=0.7191538089183991_1721187119518; bm_sv=DF5A1AADA6379734354A07A92603444C~YAAQHvAgFzFY+7aQAQAApeS+vhjasUU7APV9wldbeIzNk4lRLhpUKt2JfnCM6DT2SJjaCsK2hjmVdKnXDhmeCnTpy4DxnlMaaOo9FGev5ZrpjvkOVz0qcDJCx+GrkrEl15NRpnGwKwvXLUhiFb9C7pWYY8+fNb5e6dE1WCbru14+qVKLqIvHQMms8QsrY5cQz9kiLaGWJPwjsyTVBv7gvw8htn+DbHG5SHjWdZeZRPXRbe5mjdLmzsrErM68vw==~1; _abck=C0FFDDC6366F7017AD8C36A9AF878030~0~YAAQE/AgF6fHcbyQAQAA6vC+vgyASpu7RFbGIYKpZk3g+UsWb16B9ujMES5QBgbFaoP3fcAKOkCRQ8vF9HBbTVdYDi/mdkXvoCDjDRLzolN5jMoeILWxxPlI/R79wg4OqkcUWxSpN7ohudbjZijtIaaZTVVoT/jAGxzadzCa3GWRIoEtVf8KAccT5jhJYvXsyGQPYHA9PQyRCcrLZkLd++50/At66MIdFJdflujB36cISTzPmjlXsZD5F0Eoy7GAerC+SGZbc2LqJDNVL8qx+VW9yeVkh98uw2ri5g0bNoFH2whwFsCmRhVD4GadFzykwWb0WFBOOktIB1v+hdKOwoFYycHKg2SfsV/ZkCV7VW+5KSpUmhl+Z7ZUAjI=~-1~-1~1721190322; _ga_S4EX53B760=GS1.1.1721187112.22.1.1721187124.0.0.1947936961; episod_session_id=1721187112886.qzgfi7re.23.1721187124754",
        "Priority": "u=0, i",
        # "Referer": 'https://www.ikea.com/co/es/cat/butacos-22659/',
        "Sec-Ch-Ua": "\"Google Chrome\";v=\"126\", \"Chromium\";v=\"126\", \"Not.A/Brand\";v=\"8\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Service-Worker-Navigation-Preload": "true",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

urls = [
    "https://www.ikea.com/co/es/p/mandal-cabecero-de-cama-abedul-blanco-70176312/",
    "https://www.ikea.com/co/es/p/rykkinn-cabecero-de-cama-gunnared-gris-00479317/",
    "https://www.ikea.com/co/es/p/nordli-cabecero-de-cama-blanco-10372976/",
    "https://www.ikea.com/co/es/p/rykkinn-cabecero-de-cama-hillared-beige-20479316/",
    "https://www.ikea.com/co/es/p/rykkinn-cabecero-de-cama-gunnared-gris-70479314/",
    "https://www.ikea.com/co/es/p/rykkinn-cabecero-de-cama-hillared-beige-90479313/"
]
results = []
for url in urls:
    res = requests.get(url, headers=product_headers)
    print(res.status_code)
    soup = BeautifulSoup(res.content, "html.parser")

    # Variables
    product_name = ""
    product_price = ""

    # Medidas
    product_ancho = ""
    product_fondo = ""
    product_altura = ""
    product_ancho_asiento = ""
    product_fondo_asiento = ""
    product_altura_asiento = ""
    product_altura_conjines_espaldar = ""
    product_altura_bajo_mueble = ""
    product_altura_espaldar = ""
    product_ancho_cama = ""
    product_largo_cama = ""
    product_longitud = ""
    product_min_longitud = ""
    product_max_longitud = ""
    product_altura_piecero = ""
    product_altura_cabecera = ""
    product_ancho_colchon = ""
    product_largo_colchon = ""
    product_altura_cajon = ""
    product_ancho_cajon = ""
    product__medidas_fondo_cajon = ""
    product_altura_libre_bajo_cama = ""
    product_max_soportado = ""
    product_grosor = ""

    # Materials
    product_tela = ""
    product_estructura_respaldo_asiento = ""
    product_cojin_respaldo = ""
    product_clip = ""
    product_reposabrazos = ""
    product_cojin_asiento = ""
    product_marco = ""
    product_posterior_forro = ""
    product_estructura_reposabrazos = ""
    product_cuero = ""
    product_compas_puerta = ""
    product_cajon_cama = ""
    product_travesano = ""
    product_pata_borde_largo = ""
    product_pata_interior = ""
    product_tabla = ""
    product_tejido_base = ""
    product_asiento_respaldo = ""
    product_estructura_pata = ""
    product_cojin_respaldo_asiento = ""
    product_cinta = ""
    product_tablillas_cama = ""
    product_material_fondo_cajon = ""
    product_componentes_principales = ""
    product_lateral_cama = ""
    product_riel_cama = ""
    product_rellendo_cabecera = ""
    product_cabecera = ""
    product_hilo = ""


    product_info = str(soup).split("data-hydration-props='")[1].split("'")[0]
    product_info_json = json.loads(product_info)
    product_name = product_info_json["pipPriceModule"]["productName"]
    product_price = str(product_info_json["pipPriceModule"]["price"]["mainPriceProps"]["price"]["integer"]).replace(".", "")

    product_medidas = product_info_json["productInformationSection"]["dimensionProps"]["dimensions"]
    for medida in product_medidas:
        if medida["name"] == "Ancho":
            product_ancho = medida["measure"]
        elif medida["name"] == "Fondo":
            product_fondo = medida["measure"]
        elif medida["name"] == "Altura":
            product_altura = medida["measure"]
        elif medida["name"] == "Ancho del asiento":
            product_ancho_asiento = medida["measure"]
        elif medida["name"] == "Fondo del asiento":
            product_fondo_asiento = medida["measure"]
        elif medida["name"] == "Altura del asiento":
            product_altura_asiento = medida["measure"]
        elif medida["name"] == "Altura incl. cojines del espaldar":
            product_altura_conjines_espaldar = medida["measure"]
        elif medida["name"] == "Altura: espacio bajo el mueble":
            product_altura_bajo_mueble = medida["measure"]
        elif medida["name"] == "Altura del espaldar":
            product_altura_espaldar = medida["measure"]
        elif medida["name"] == "Ancho de cama":
            product_ancho_cama = medida["measure"]
        elif medida["name"] == "Largo de cama":
            product_largo_cama = medida["measure"]
        elif medida["name"] == "Longitud":
            product_longitud = medida["measure"]
        elif medida["name"] == "Longitud mínima":
            product_min_longitud = medida["measure"]
        elif medida["name"] == "Longitud máxima":
            product_max_longitud = medida["measure"]
        elif medida["name"] == "Altura piecero":
            product_altura_piecero = medida["measure"]
        elif medida["name"] == "Altura cabecera":
            product_altura_cabecera = medida["measure"]
        elif medida["name"] == "Ancho del colchón":
            product_ancho_colchon = medida["measure"]
        elif medida["name"] == "Largo del colchón":
            product_largo_colchon = medida["measure"]
        elif medida["name"] == "Altura cajón (int)":
            product_altura_cajon = medida["measure"]
        elif medida["name"] == "Ancho de cajón (int)":
            product_ancho_cajon = medida["measure"]
        elif medida["name"] == "Fondo de cajón (int)":
            product__medidas_fondo_cajon = medida["measure"]
        elif medida["name"] == "Altura libre bajo cuna":
            product_altura_libre_bajo_cama = medida["measure"]
        elif medida["name"] == "Máximo soportado":
            product_max_soportado = medida["measure"]
        elif medida["name"] == "Grosor":
            product_grosor = medida["measure"]

    product_materials = product_info_json["productInformationSection"]["productDetailsProps"]["accordionObject"]["materialsAndCare"]["contentProps"]["materials"]
    for materials in product_materials:
        sub_materials = materials["materials"]
        for material in sub_materials:
            try:
                if material["part"] == "Tela:":
                    product_tela = material["material"]
                elif  material["part"] == "Estructura del asiento:":
                    product_estructura_respaldo_asiento = material["material"]
                elif  material["part"] == "Cojín de respaldo:":
                    product_cojin_respaldo = material["material"]
                elif  material["part"] == "Estructura inferior/ Pata:":
                    product_estructura_pata = material["material"]
                elif  material["part"] == "Clip:":
                    product_clip = material["material"]
                elif  material["part"] == "Estructura de respaldo:":
                    product_estructura_respaldo_asiento = material["material"]
                elif  material["part"] == "Pata:":
                    product_pata_borde_largo = material["material"]
                elif  material["part"] == "Estructura de asiento:":
                    product_estructura_respaldo_asiento = material["material"]
                elif  material["part"] == "Reposabrazos:":
                    product_reposabrazos = material["material"]
                elif  material["part"] == "Estructura de asiento/ Estructura de asiento:":
                    product_estructura_respaldo_asiento = material["material"]
                elif  material["part"] == "Cojín de asiento:":
                    product_cojin_asiento = material["material"]
                elif  material["part"] == "Marco:":
                    product_marco = material["material"]
                elif  material["part"] == "Forro:":
                    product_posterior_forro = material["material"]
                elif  material["part"] == "Estructura del respaldo y del asiento:":
                    product_estructura_respaldo_asiento = material["material"]
                elif  material["part"] == "Estructura de reposabrazos:":
                    product_estructura_reposabrazos = material["material"]
                elif  material["part"] == "Cuero:":
                    product_cuero = material["material"]
                elif  material["part"] == "Compás para puerta:":
                    product_compas_puerta = material["material"]
                elif  material["part"] == "Tejido posterior:":
                    product_posterior_forro = material["material"]
                elif  material["part"] == "Clip/ Pata":
                    product_pata_borde_largo = material["material"]
                    product_clip = material["material"]
                elif  material["part"] == "Cajón para cama:":
                    product_cajon_cama = material["material"]
                elif  material["part"] == "Travesaño:":
                    product_travesano = material["material"]
                elif  material["part"] == "Borde largo/ Travesaño/ Frente/ Pata/ Armazón inferior:":
                    product_pata_borde_largo = material["material"]
                    product_travesano = material["material"]
                elif  material["part"] == "Pata/ Borde largo:":
                    product_pata_borde_largo = material["material"]
                elif  material["part"] == "Pata interior:":
                    product_pata_interior = material["material"]
                elif  material["part"] == "Tabla:":
                    product_tabla = material["material"]
                elif  material["part"] == "Respaldo:":
                    product_asiento_respaldo = material["material"]
                elif  material["part"] == "Asiento:":
                    product_asiento_respaldo = material["material"]
                elif  material["part"] == "Tejido de base:":
                    product_tejido_base = material["material"]
                elif  material["part"] == "Asiento/ Respaldo:":
                    product_asiento_respaldo = material["material"]
                elif  material["part"] == "Respaldo/ Asiento:":
                    product_asiento_respaldo = material["material"]
                elif  material["part"] == "Estructura de pata/ Riel transversal:'":
                    product_estructura_pata = material["material"]
                elif  material["part"] == "Cojín de respaldo/ Cojín de asiento:":
                    product_cojin_respaldo_asiento = material["material"]
                elif  material["part"] == "Estructura del respaldo:":
                    product_estructura_respaldo_asiento = material["material"]
                elif  material["part"] == "Tejido posterior/ Forro:":
                    product_posterior_forro = material["material"]
                elif  material["part"] == "Tabla/ Hoja de extensión:":
                    product_tabla = material["material"]
                elif  material["part"] == "Estructura de pata:":
                    product_estructura_pata = material["material"]
                elif  material["part"] == "Cabecera/pies de cama:":
                    product_cabecera = material["material"]
                elif  material["part"] == "Lateral de cama:":
                    product_lateral_cama = material["material"]
                elif  material["part"] == "Cinta:":
                    product_cinta = material["material"]
                elif  material["part"] == "Tablillas de cama:":
                    product_tablillas_cama = material["material"]
                elif  material["part"] == "Fondo de cajón:":
                    product_material_fondo_cajon = material["material"]
                elif  material["part"] == "Componentes principales/ Pared divisora/ Frente de cajón:":
                    product_componentes_principales = material["material"]
                elif  material["part"] == "Relleno de la cabecera:":
                    product_rellendo_cabecera = material["material"]
                elif  material["part"] == "Lateral de cama/ Pieza de fondo:":
                    product_lateral_cama = material["material"]
                elif  material["part"] == "Componentes principales/ Barrotes/ Estructura de somier:":
                    product_componentes_principales = material["material"]
                elif  material["part"] == "Componentes principales:":
                    product_componentes_principales = material["material"]
                elif  material["part"] == "Riel de cama:":
                    product_riel_cama = material["material"]
                elif  material["part"] == "Relleno de cabecera:":
                    product_rellendo_cabecera = material["material"]
                elif  material["part"] == "Cabecera:":
                    product_cabecera = material["material"]
                elif  material["part"] == "Hilo:":
                    product_hilo = material["material"]
            except:
                pass
    product_data = {
        "Nombre":product_name,
        "Precio":product_price,

        # Medidas
        "Medidas":"Medidas",
        "Ancho":product_ancho,
        "Fondo":product_fondo,
        "Altura":product_altura,
        "Ancho del asiento":product_ancho_asiento,
        "Fondo del asiento":product_fondo_asiento,
        "Altura del asiento":product_altura_asiento,
        "Altura incl cojines del espaldar":product_altura_conjines_espaldar,
        "Altura: espacio bajo el mueble":product_altura_bajo_mueble,
        "Altura del espaldar":product_altura_espaldar,
        "Ancho de cama":product_ancho_cama,
        "Largo de cama":product_largo_cama,
        "Longitud":product_longitud,
        "Longitud mínima":product_min_longitud,
        "Longitud máxima":product_max_longitud,
        "Altura piecero":product_altura_piecero,
        "Altura cabecera":product_altura_cabecera,
        "Ancho del colchón":product_ancho_colchon,
        "Largo del colchón":product_largo_colchon,
        "Altura cajón":product_altura_cajon,
        "Ancho de cajón":product_ancho_cajon,
        "Fondo de cajón":product__medidas_fondo_cajon,
        "Altura libre bajo cuna":product_altura_libre_bajo_cama,
        "Máximo soportado":product_max_soportado,
        "Grosor":product_grosor,

        # Materials
        "Materials":"Materials",
        "Tela":product_tela,
        "Estructura del asiento":product_estructura_respaldo_asiento,
        "Cojín de respaldo":product_cojin_respaldo,
        "Clip":product_clip,
        "Reposabrazos":product_reposabrazos,
        "Cojín de asiento":product_cojin_asiento,
        "Marco":product_marco,
        "Tejido posterior":product_posterior_forro,
        "Estructura reposabrazos":product_estructura_reposabrazos,
        "Cuero":product_cuero,
        "Compas para puerta":product_compas_puerta,
        "Cajón para cama":product_cajon_cama,
        "Travesaño":product_travesano,
        "Pata / borde largo":product_pata_borde_largo,
        "Pata interior":product_pata_interior,
        "Tabla":product_tabla,
        "Tejido base":product_tejido_base,
        "Asiento/ Respaldo":product_asiento_respaldo,
        "Estructura de pata":product_estructura_pata,
        "Cojín de respaldo/ Cojín de asiento":product_cojin_respaldo_asiento,
        "Cinta":product_cinta,
        "Tablillas de cama":product_tablillas_cama,
        "Fondo de cajón":product_material_fondo_cajon,
        "Componentes principales":product_componentes_principales,
        "Lateral de cama":product_lateral_cama,
        "Riel de cama":product_riel_cama,
        "Relleno de cabecera":product_rellendo_cabecera,
        "Cabecera":product_cabecera,
        "Hilo":product_hilo,
    }
    results.append(product_data)
    import os, csv
    if not os.path.exists("./results"):
        os.makedirs("./results")

    with open("./results/ikea.json", "w") as file:
        json.dump(results, file, indent=4)

    # JSON data
    with open("./results/ikea.json", "r") as file:
        json_data = json.load(file)

    # Define CSV file name
    csv_file = "./results/ikea.csv"

    # Define fieldnames for CSV header
    fieldnames = json_data[0].keys()

    # Write JSON data to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in json_data:
            writer.writerow(item)