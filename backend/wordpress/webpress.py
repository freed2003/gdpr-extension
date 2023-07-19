from io import BytesIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import zipfile
import shutil
import os
def parse_plugins(url: str) -> set:
    req = requests.get(url)
    plugins = set()
    soup = BeautifulSoup(req.text, 'html.parser')
    all = soup.find_all(True)
    for tag in all:
        for attr in tag.attrs:
            content = tag[attr]
            if type(content) == type([]):
                for c in content:
                    split = c.split("wp-content/plugins/")
                    if len(split) > 1:
                        plugins.add(split[1].partition("/")[0])
                continue
            split = content.split("wp-content/plugins/")
            if len(split) > 1:
                plugins.add(split[1].partition("/")[0])
    # do we have a source that says only scripts and links contain plugins?
    # links = soup.find_all('link', attrs={'href': True})
    # scripts = soup.find_all('script', attrs={'src': True})
    # for link in links:
    #     split = link['href'].split("wp-content/plugins/")
    #     if len(split) > 1:
    #         plugins.add(split[1].partition("/")[0])
    # for script in scripts:
    #     split = script['src'].split("wp-content/plugins/")
    #     if len(split) > 1:
    #         plugins.add(split[1].partition("/")[0])
    return plugins

def get_download(plugin: str) -> str:
    link = f"https://wordpress.org/plugins/{plugin}/"
    req = requests.get(link)
    if len(req.history) != 0:
        search = f"https://wordpress.org/search/{plugin}/"

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(search)
        link = driver.find_element("xpath", "//a[@class='gs-title']")
        link = (link.get_attribute("href"))
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "html.parser")
    download = soup.find("a", attrs={'class':"plugin-download button download-button button-large"})
    return download['href']

def download_unzip(url: str) -> None:
    req = requests.get(url, stream=True)
    zf = zipfile.ZipFile(BytesIO(req.content))
    shutil.rmtree("currentplugin")
    zf.extractall(path="currentplugin")
    zf.close()    
    tbc = os.listdir("currentplugin")[0]
    tbc = os.path.join("currentplugin", tbc)
    to = os.path.join("currentplugin", "cur")
    os.rename(tbc, to)
download_unzip("https://downloads.wordpress.org/plugin/custom-twitter-feeds.2.1.1.zip")