import urllib.request
import json
import matplotlib.pyplot as plt

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


def convert_gdp(gdp):
    """
    converts gdp to a list of dates and a list of gdp's
    :param gdp: list
    :return: list, list
    """
    dates = []
    gdps = []
    for element in gdp:
        dates.append(element[0][2:4])
        gdps.append(element[1])
    return dates, gdps


if __name__ == "__main__":
    # a simple chart of Ukraine's GDP
    ukr_gdp = get_ukraine_gdp(base_url)
    dates, gdps = convert_gdp(ukr_gdp)[0], convert_gdp(ukr_gdp)[1]
    plt.plot(dates, gdps, color='lightblue', linewidth=3)
    plt.show()

    # Pie chart of manufacturing distribution
    labels = 'Energy', 'Steal', 'Tractors', 'Automobiles'
    sizes = [30, 25, 15, 30]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
