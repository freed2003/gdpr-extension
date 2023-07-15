from bs4 import BeautifulSoup
import requests

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

#return a boolean on if it passes and probably other data i haven't decided on
def wpcheck(url: str) -> dict:
    plugins = parse_plugins(url)
    print("detected plugins: ")
    for i in plugins:
        print(i)

def policycheck(url: str) -> dict:
    pass

if __name__ == "__main__":
    wpcheck("https://www.sonymusic.com/")