import requests

if __name__ == '__main__':
    print(requests.__version__)

    r = requests.get('https://www.google.com')
    print(r.text)
