import requests

if __name__ == '__main__':
    print(requests.__version__)

    r = requests.get('https://raw.githubusercontent.com/Ana16boo/CMPUT404-Lab1/main/versionRequests.py')
    print(r.text)
