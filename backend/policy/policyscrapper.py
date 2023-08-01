from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from htmltotext.Preprocessor import Preprocessor
from selenium import webdriver
from apikey import key, cx
import requests
import json


ENDPOINT = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}"

def getpolicyurl(url: str) -> str:
    dommame = "https://" + url.split("https://")[1].split("/")[0]
    q = f"{dommame}%20privacy policy"
    query = f"{ENDPOINT}&exactTerms=privacy&q={q}"
    resp = requests.get(query)
    jresp = json.loads(resp.text)
    return jresp["items"][0]['link']

def gethtml(url: str) -> str:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    text = driver.find_element("tag name", "body").get_attribute("innerHTML")
    return text
def parse(url: str) -> str:
    text = gethtml(getpolicyurl(url))
    with open("temp", "w", encoding="UTF-8") as f:
        f.write(text)
    pp = Preprocessor("temp")
    return "\n".join(pp.parse())

print(parse("https://google.com"))