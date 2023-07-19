from webpress import parse_plugins, get_download, download_unzip



#return a boolean on if it passes and probably other data i haven't decided on
def wpcheck(url: str) -> dict:
    plugins = parse_plugins(url)
    for i in plugins:
        dlink = get_download(i)
        download_unzip(dlink)
        
def policycheck(url: str) -> dict:
    pass

if __name__ == "__main__":
    wpcheck("https://www.sonymusic.com/")