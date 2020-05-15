import unittest
from economic_analysis.country import Country


class TestingCountries(unittest.TestCase):
    """
    Class for testing country module
    """
    def setUp(self):
        """
        Prescribe values for tests
        """
        self.ukraine = Country('Ukraine')
        self.ukraine.get_gdp('https://www.quandl.com/api/v3/'
                             'datasets/WWDI/UKR_NY_GDP_PCAP_CD.'
                             'json?api_key=2jhCWecEKmuxzVY9ifwp')
        self.bulgaria = Country('Bulgaria')
        self.bulgaria.get_investment_inflows('https://www.quandl.com'
                                             '/api/v3/datasets/WWDI/'
                                             'BGR_BX_KLT_DINV_WD_GD_ZS.json?'
                                             'api_key=2jhCWecEKmuxzVY9ifwp')
        self.hungary = Country('Hungary')
        self.hungary.get_investment_outflows('https://www.quandl.com/'
                                             'api/v3/datasets/WWDI/'
                                             'HUN_BM_KLT_DINV_GD_ZS.json?'
                                             'api_key=2jhCWecEKmuxzVY9ifwp')
        self.poland = Country('Poland')
        self.poland.get_manufacturing('https://www.quandl.com/api'
                                      '/v3/datasets/WWDI/POL_NV_'
                                      'IND_MANF_ZS.json?api_key'
                                      '=2jhCWecEKmuxzVY9ifwp')

    def test_gdp(self):
        """
        Testing how get_gdp works
        """
        self.assertEqual(self.ukraine.gdp[0], 1249.4432776058,
                         'get_gdp does not work')

    def test_investment_inflows(self):
        """
        Tests how get_investment_inflows works
        """
        self.assertEqual(self.bulgaria.investment_inflows[0], 0.0,
                         'get_investment_inflows does not work')

    def test_investment_outflows(self):
        """
        Tests how get_investment_outflows works
        """
        self.assertEqual(self.hungary.investment_outflows[0],
                         2.7554412051241,
                         'get_investment_outflows does not work')

    def test_manufacturing(self):
        """
        Tests how get_manufacturing works
        """
        self.assertEqual(self.poland.manufacturing[0], 19.120467211902,
                         'get_manufacturing does not work')
