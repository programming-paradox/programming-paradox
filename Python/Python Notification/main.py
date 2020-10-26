from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="corona.ico",
        timeout=10
    )

def get_data(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyme("Harry", "Let's stop the spread of virus together")
    myhtmldata = get_data("http://covid.gov.pk/")

    # print(myhtmldata)
    soup = BeautifulSoup(myhtmldata, 'html.parser')
    # print(soup.prettify())
    for data in soup.find(class_="numanimate"):
        pass

    notifyme("Covid 19", f"The Total Cases In Pakistan Are {data}")
    # for data in soup.find(class_='deaths'):
    #     print(data)
