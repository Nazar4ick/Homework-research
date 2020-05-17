import json
import urllib.request
from economic_analysis.custom_array import Array


class Country:
    """
    Class for representing countries
    """

    def __init__(self, name):
        """
        Initializes a new country
        Note: GDP counts as GDP per capita
        foreign investment inflows, outflows
        and manufacturing are counted as % of GDP
        :param name: str
        """
        self.name = name
        self.gdp = None
        self.investment_inflows = None
        self.investment_outflows = None
        self.manufacturing = None
        self.min_indexes = {}

    @staticmethod
    def read_url(url):
        """
        reads the desired url
        Note: All countries have their values stored by keys
        'dataset' and 'data'
        :param url: str
        :return: list
        """
        with urllib.request.urlopen(url) as response:
            data = response.read()
            data = data.decode('utf-8')
            data = json.loads(data)
            data = data['dataset']['data']
            return data

    def get_gdp(self, url):
        """
        gets country's gdp
        Note: for the later searching system, the base year
        (the year from which the values begin) should be stored,
        so the user will search for gdp[year-base_year] value
        :param url: str
        :return: None
        """
        data = self.read_url(url)
        base_search_index = int(data[-1][0][0:4])
        self.min_indexes['gdp'] = base_search_index
        data = self.convert_to_array(data)
        self.gdp = data
        return None

    def get_investment_inflows(self, url):
        """
        gets country's foreign investment inflows as % of GDP
        :param url: str
        :return: None
        """
        data = self.read_url(url)
        base_search_index = int(data[-1][0][0:4])
        self.min_indexes['investment_inflows'] = base_search_index
        data = self.convert_to_array(data)
        self.investment_inflows = data
        return None

    def get_investment_outflows(self, url):
        """
        get country's foreign investment outflows as % of GDP
        :param url: str
        :return: None
        """
        data = self.read_url(url)
        base_search_index = int(data[-1][0][0:4])
        self.min_indexes['investment_outflows'] = base_search_index
        data = self.convert_to_array(data)
        self.investment_outflows = data
        return None

    def get_manufacturing(self, url):
        """
        get country's manufacturing as % of GDP
        :param url: str
        :return: None
        """
        data = self.read_url(url)
        base_search_index = int(data[-1][0][0:4])
        self.min_indexes['manufacturing'] = base_search_index
        data = self.convert_to_array(data)
        self.manufacturing = data
        return None

    @staticmethod
    def convert_to_array(data):
        """
        converts the information from list to array
        Note: data will be reversed, because all countries
        years are in descending order and it is better to
        present them in ascending order for visualization
        :param data: list
        :return: array
        """
        data.reverse()
        size = len(data)
        array = Array(size)
        for i in range(size):
            array[i] = data[i][1]
        return array
