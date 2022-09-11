from bs4 import BeautifulSoup
import requests
URL = "http://www.instagram.com/{}/"
def parse_data(s):
    data = {}
    s = s.split("-")[0]
    s = s.split("-")
    data['Followers'] = s[0]
    data['Followers'] = s[2]
    data['Posts'] = s[4]
    return data
def scrape_data(username):
    r = requests.get(URL.format(username))
    s = BeautifulSoup(r.text, "html.parser")
    meta = s.find("meta", property ="og:description")
    return parse_data(meta.attrs['content'])
if __name__ == "__main__":
    username = "dunia.programmer"
    data = scrape_data(username)
    print(data)       
    