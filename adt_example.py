from country import Country
import matplotlib.pyplot as plt


ukraine = Country('Ukraine')
ukraine.get_gdp('https://www.quandl.com/api/v3/'
                'datasets/WWDI/UKR_NY_GDP_PCAP_CD.'
                'json?api_key=2jhCWecEKmuxzVY9ifwp')

poland = Country('Poland')
poland.get_gdp('https://www.quandl.com/api/v3'
               '/datasets/WWDI/POL_NY_GDP_PCAP_CD.'
               'json?api_key=2jhCWecEKmuxzVY9ifwp')

plt.plot(ukraine.gdp)
plt.plot(poland.gdp)
plt.show()
