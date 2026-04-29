
"""
testing my website to see if its working or down
this is only a basic function - just trying out my server site 
"""

import requests



def main():

    url_resquest(url="https://tv.localstreamgh.com/admin")

def url_resquest(url):

    try:
        resonse = requests.get(url)
        if resonse.status_code == 200:
            print("site is running")
        else:
            print("could not reach the site")
    except Exception as e:
        print(e)




if __name__ == "__main__":
    main()