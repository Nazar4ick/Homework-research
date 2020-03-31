import urllib.request
import json


base_url = 'https://www.quandl.com/api/v3/datasets/WWDI/UKR_NY_GDP_MKTP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp'

def get_ukraine_gdp(url):
    """
    Gets Ukraine's GDP from quandl in US dollars
    :param url: str
    :return: dict
    """
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = data.decode('utf-8')
        data = json.loads(data)
        gdp = data['dataset']['data']
        return gdp


print(get_ukraine_gdp(base_url))
