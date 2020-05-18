from country import Country


def get_ukraine():
    """
    gets all the data for Ukraine
    :return: object
    """
    ukraine = Country('Ukraine')
    ukraine.get_gdp('https://www.quandl.com/api/v3/'
                    'datasets/WWDI/UKR_NY_GDP_PCAP_CD.'
                    'json?api_key=2jhCWecEKmuxzVY9ifwp')
    ukraine.get_investment_inflows('https://www.quandl.com'
                                   '/api/v3/datasets/WWDI/'
                                   'UKR_BX_KLT_DINV_WD_GD_ZS.'
                                   'json?api_key=2jhCWecEKmuxzVY9ifwp')
    ukraine.get_investment_outflows('https://www.quandl.com'
                                    '/api/v3/datasets/WWDI/'
                                    'UKR_BM_KLT_DINV_GD_ZS.'
                                    'json?api_key=2jhCWecEKmuxzVY9ifwp')
    ukraine.get_manufacturing('https://www.quandl.com/'
                              'api/v3/datasets/WWDI/'
                              'UKR_NV_IND_MANF_ZS.'
                              'json?api_key=2jhCWecEKmuxzVY9ifwp')
    return ukraine


def get_bulgaria():
    """
    gets all the data for Bulgaria
    :return: object
    """
    bulgaria = Country('Bulgaria')
    bulgaria.get_gdp('https://www.quandl.com/api/v3/'
                     'datasets/WWDI/BGR_NY_GDP_PCAP_CD.'
                     'json?api_key=2jhCWecEKmuxzVY9ifwp')
    bulgaria.get_investment_inflows('https://www.quandl.com'
                                    '/api/v3/datasets/WWDI/'
                                    'BGR_BX_KLT_DINV_WD_GD_ZS.'
                                    'json?api_key=2jhCWecEKmuxzVY9ifwp')
    bulgaria.get_investment_outflows('https://www.quandl.com/'
                                     'api/v3/datasets/WWDI/'
                                     'BGR_BM_KLT_DINV_GD_ZS.'
                                     'json?api_key=2jhCWecEKmuxzVY9ifwp')
    bulgaria.get_manufacturing('https://www.quandl.com/'
                               'api/v3/datasets/WWDI/'
                               'BGR_NV_IND_MANF_ZS.'
                               'json?api_key=2jhCWecEKmuxzVY9ifwp')
    return bulgaria


def get_hungary():
    """
    gets all the data for Hungary
    :return: object
    """
    hungary = Country('Hungary')
    hungary.get_gdp('https://www.quandl.com/api/'
                    'v3/datasets/WWDI/HUN_NY_GDP_PCAP_CD.'
                    'json?api_key=2jhCWecEKmuxzVY9ifwp')
    hungary.get_investment_inflows('https://www.quandl.com/'
                                   'api/v3/datasets/WWDI/'
                                   'HUN_BX_KLT_DINV_WD_GD_ZS.'
                                   'json?api_key=2jhCWecEKmuxzVY9ifwp')
    hungary.get_investment_outflows('https://www.quandl.com/'
                                    'api/v3/datasets/WWDI/'
                                    'HUN_BM_KLT_DINV_GD_ZS.'
                                    'json?api_key=2jhCWecEKmuxzVY9ifwp')
    hungary.get_manufacturing('https://www.quandl.com/'
                              'api/v3/datasets/'
                              'WWDI/HUN_NV_IND_MANF_ZS.'
                              'json?api_key=2jhCWecEKmuxzVY9ifwp')
    return hungary


def get_poland():
    """
    gets all the data for Poland
    :return: object
    """
    poland = Country('Poland')
    poland.get_gdp('https://www.quandl.com/api/v3'
                   '/datasets/WWDI/POL_NY_GDP_PCAP_CD.'
                   'json?api_key=2jhCWecEKmuxzVY9ifwp')
    poland.get_investment_inflows('https://www.quandl.com/'
                                  'api/v3/datasets/WWDI/'
                                  'POL_BX_KLT_DINV_WD_GD_ZS.'
                                  'json?api_key=2jhCWecEKmuxzVY9ifwp')
    poland.get_investment_outflows('https://www.quandl.com/'
                                   'api/v3/datasets/WWDI/'
                                   'POL_BM_KLT_DINV_GD_ZS.'
                                   'json?api_key=2jhCWecEKmuxzVY9ifwp')
    poland.get_manufacturing('https://www.quandl.com/api'
                             '/v3/datasets/WWDI/POL_NV_'
                             'IND_MANF_ZS.json?api_key'
                             '=2jhCWecEKmuxzVY9ifwp')
    return poland


def get_romania():
    """
    gets all data for Romania
    :return: object
    """
    romania = Country('Romania')
    romania.get_gdp('https://www.quandl.com/api/v3/datasets'
                    '/WWDI/ROU_NY_GDP_PCAP_CD.json'
                    '?api_key=2jhCWecEKmuxzVY9ifwp')
    romania.get_investment_inflows('https://www.quandl.com/api/v3'
                                   '/datasets/WWDI/ROU_BX_KLT_'
                                   'DINV_WD_GD_ZS.json?api_key='
                                   '2jhCWecEKmuxzVY9ifwp')
    romania.get_investment_outflows('https://www.quandl.com/api/v3'
                                    '/datasets/WWDI/ROU_BM_KLT_DINV'
                                    '_GD_ZS.json?api_key=2jhCWecEK'
                                    'muxzVY9ifwp')
    romania.get_manufacturing('https://www.quandl.com/api/v3/'
                              'datasets/WWDI/ROU_NV_IND_MANF_'
                              'ZS.json?api_key=2jhCWecEKmuxzVY9ifwp')
    return romania


def get_czech():
    """
    gets all the data for Czech Republic
    :return: object
    """
    czech = Country('Czech Republic')
    czech.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/CZE'
                  '_NY_GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    czech.get_investment_inflows('https://www.quandl.com/api/v3/dat'
                                 'asets/WWDI/CZE_BX_KLT_DINV_WD_GD_ZS'
                                 '.json?api_key=2jhCWecEKmuxzVY9ifwp')
    czech.get_investment_outflows('https://www.quandl.com/api/v3/data'
                                  'sets/WWDI/CZE_BM_KLT_DINV_GD_ZS.js'
                                  'on?api_key=2jhCWecEKmuxzVY9ifwp')
    czech.get_manufacturing('https://www.quandl.com/api/v3/datasets'
                            '/WWDI/CZE_NV_IND_MANF_ZS.json?api_key='
                            '2jhCWecEKmuxzVY9ifwp')
    return czech


def get_slovakia():
    """
    gets all the data for Slovakia
    :return: object
    """
    slovakia = Country('Slovak Republic')
    slovakia.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/SVK_'
                     'NY_GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    slovakia.get_investment_inflows('https://www.quandl.com/api/v3/data'
                                    'sets/WWDI/SVK_BX_KLT_DINV_WD_GD_ZS'
                                    '.json?api_key=2jhCWecEKmuxzVY9ifwp')
    slovakia.get_investment_outflows('https://www.quandl.com/api/v3/data'
                                     'sets/WWDI/SVK_BM_KLT_DINV_GD_ZS.j'
                                     'son?api_key=2jhCWecEKmuxzVY9ifwp')
    slovakia.get_manufacturing('https://www.quandl.com/api/v3/datasets/'
                               'WWDI/SVK_NV_IND_MANF_ZS.json?api_key=2j'
                               'hCWecEKmuxzVY9ifwp')
    return slovakia


def get_slovenia():
    """
    gets all the data for Slovenia
    :return: object
    """
    slovenia = Country('Slovenia')
    slovenia.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/SVN_'
                     'NY_GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    slovenia.get_investment_inflows('https://www.quandl.com/api/v3/datas'
                                    'ets/WWDI/SVN_BX_KLT_DINV_WD_GD_ZS.j'
                                    'son?api_key=2jhCWecEKmuxzVY9ifwp')
    slovenia.get_investment_outflows('https://www.quandl.com/api/v3/datas'
                                     'ets/WWDI/SVN_BM_KLT_DINV_GD_ZS.jso'
                                     'n?api_key=2jhCWecEKmuxzVY9ifwp')
    slovenia.get_manufacturing('https://www.quandl.com/api/v3/datase'
                               'ts/WWDI/SVN_NV_IND_MANF_ZS.json?api_'
                               'key=2jhCWecEKmuxzVY9ifwp')
    return slovenia


def get_croatia():
    """
    get all data for Croatia
    :return: object
    """
    croatia = Country('Croatia')
    croatia.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/HRV_N'
                    'Y_GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    croatia.get_investment_inflows('https://www.quandl.com/api/v3/data'
                                   'sets/WWDI/HRV_BX_KLT_DINV_WD_GD_ZS'
                                   '.json?api_key=2jhCWecEKmuxzVY9ifwp')
    croatia.get_investment_outflows('https://www.quandl.com/api/v3/data'
                                    'sets/WWDI/HRV_BM_KLT_DINV_GD_ZS.js'
                                    'on?api_key=2jhCWecEKmuxzVY9ifwp')
    croatia.get_manufacturing('https://www.quandl.com/api/v3/datasets/'
                              'WWDI/HRV_NV_IND_MANF_ZS.json?api_key='
                              '2jhCWecEKmuxzVY9ifwp')
    return croatia


def get_lithuania():
    """
    gets all the data for Lithuania
    :return: object
    """
    lithuania = Country('Lithuania')
    lithuania.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/LTU_'
                      'NY_GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    lithuania.get_investment_inflows('https://www.quandl.com/api/v3/data'
                                     'sets/WWDI/LTU_BX_KLT_DINV_WD_GD_ZS.'
                                     'json?api_key=2jhCWecEKmuxzVY9ifwp')
    lithuania.get_investment_outflows('https://www.quandl.com/api/v3/dat'
                                      'asets/WWDI/LTU_BM_KLT_DINV_GD_ZS.'
                                      'json?api_key=2jhCWecEKmuxzVY9ifwp')
    lithuania.get_manufacturing('https://www.quandl.com/api/v3/datasets'
                                '/WWDI/LTU_NV_IND_MANF_ZS.json?api_key='
                                '2jhCWecEKmuxzVY9ifwp')
    return lithuania


def get_latvia():
    """
    gets all the data for Latvia
    :return: object
    """
    latvia = Country('Latvia')
    latvia.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/LVA_NY_'
                   'GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    latvia.get_investment_inflows('https://www.quandl.com/api/v3/dataset'
                                  's/WWDI/LVA_BX_KLT_DINV_WD_GD_ZS.json?'
                                  'api_key=2jhCWecEKmuxzVY9ifwp')
    latvia.get_investment_outflows('https://www.quandl.com/api/v3/data'
                                   'sets/WWDI/LVA_BM_KLT_DINV_GD_ZS.jso'
                                   'n?api_key=2jhCWecEKmuxzVY9ifwp')
    latvia.get_manufacturing('https://www.quandl.com/api/v3/datasets'
                             '/WWDI/LVA_NV_IND_MANF_ZS.json?api_key='
                             '2jhCWecEKmuxzVY9ifwp')
    return latvia


def get_estonia():
    """
    gets all the data for Estonia
    :return: object
    """
    estonia = Country('Estonia')
    estonia.get_gdp('https://www.quandl.com/api/v3/datasets/WWDI/EST'
                    '_NY_GDP_PCAP_CD.json?api_key=2jhCWecEKmuxzVY9ifwp')
    estonia.get_investment_inflows('https://www.quandl.com/api/v3/data'
                                   'sets/WWDI/EST_BX_KLT_DINV_WD_GD_ZS.'
                                   'json?api_key=2jhCWecEKmuxzVY9ifwp')
    estonia.get_investment_outflows('https://www.quandl.com/api/v3/dat'
                                    'asets/WWDI/EST_BM_KLT_DINV_GD_ZS.'
                                    'json?api_key=2jhCWecEKmuxzVY9ifwp')
    estonia.get_manufacturing('https://www.quandl.com/api/v3/datasets/'
                              'WWDI/EST_NV_IND_MANF_ZS.json?api_key=2'
                              'jhCWecEKmuxzVY9ifwp')
    return estonia
