import countries_data
import matplotlib.pyplot as plt


def get_countries():
    """
    gets information about all researched countries
    :return: tuple
    """
    ukraine = countries_data.get_ukraine()
    bulgaria = countries_data.get_bulgaria()
    hungary = countries_data.get_hungary()
    poland = countries_data.get_poland()
    romania = countries_data.get_romania()
    czech = countries_data.get_czech()
    slovakia = countries_data.get_slovakia()
    slovenia = countries_data.get_slovenia()
    croatia = countries_data.get_croatia()
    lithuania = countries_data.get_lithuania()
    latvia = countries_data.get_latvia()
    estonia = countries_data.get_estonia()
    return \
        ukraine, bulgaria, hungary, poland, \
        romania, czech, slovakia, slovenia, \
        croatia, lithuania, latvia, estonia


def launch_search_system(countries, country_names):
    """
    launches the search system
    :param countries: list
    :param country_names: list
    :return: None
    """
    choice = 'yes'
    while choice != 'no':
        print(country_names)
        name = input("What country you would like to investigate? ")
        while name not in country_names:
            name = input("What country you would like to investigate? ")
        # find the desired country
        for country in countries:
            if country.name == name:
                searched = country

        # Move on to the info
        commands = ('gdp', 'investment_inflows', 'investment_outflows',
                    'manufacturing')
        print(commands)
        command = input('What would you like to learn? ').lower()
        while command not in commands:
            command = input('What would you like to learn? ').lower()
        # find the desired command
        if command == 'gdp':
            info = searched.gdp
            min_year = searched.min_indexes['GDP']
        elif command == 'investment_inflows':
            info = searched.foreign_investment_inflows
            min_year = searched.min_indexes['foreign_investment_inflows']
        elif command == 'investment_outflows':
            info = searched.foreign_investment_outflows
            min_year = searched.min_indexes['foreign_investment_outflows']
        else:
            info = searched.manufacturing
            min_year = searched.min_indexes['manufacturing']

        # Move on to the year
        print(f'the minimal year is {min_year}, maximum: 2018')
        year = 1
        while not min_year <= year <= 2018:
            year = input("What year's info are you looking for? ")
            while True:
                try:
                    year = int(year)
                    break
                except ValueError:
                    year = input("What year's info are you looking for? ")
        # display the info
        print(info[year - min_year])

        # give an opportunity to learn something more
        choice = input('Would you like to learn something more? (yes/no) ')
        while choice not in ('yes', 'no'):
            choice = input('Would you like to learn something more? (yes/no) ')


def get_requested_countries(countries, country_names):
    """
    gets requested countries for visualization and info
    :param countries: list of all available countries for research
    :param country_names: list
    :return: (list, str)
    """
    print(country_names)

    # gather the requested information
    chosen_names = []
    requested_countries = []
    name = ''
    while name != 'next':
        name = input('What countries would you like to investigate?'
                     ' (type next to proceed) ')
        while name not in country_names and name != 'next':
            name = input('What countries would you like to investigate?'
                         ' (type next to proceed) ')
        chosen_names.append(name)

    # add chosen countries
    for name in chosen_names:
        for country in countries:
            if name == country.name:
                requested_countries.append(country)

    # ask what info would the user like to learn
    commands = ('gdp', 'investment_inflows', 'investment_outflows',
                'manufacturing')
    print(commands)
    info = input('What would you like to visualize? ')
    while info not in commands:
        info = input('What would you like to visualize? ')
    return requested_countries, info


def visualize(countries, country_names):
    """
    visualizes requested information
    :param countries: list of all available countries for research
    :param country_names: list
    :return: None
    """
    countries_and_info = get_requested_countries(countries, country_names)
    countries, info = countries_and_info[0], countries_and_info[1]
    if info == 'gdp':
        for country in countries:
            plt.plot(country.gdp, label=country.name)
    elif info == 'investment_inflows':
        for country in countries:
            plt.plot(country.foreign_investment_inflows, label=country.name)
    elif info == 'investment_outflows':
        for country in countries:
            plt.plot(country.foreign_investment_outflows, label=country.name)
    else:
        for country in countries:
            plt.plot(country.manufacturing, label=country.name)
    plt.legend()
    plt.show()


def main():
    """
    Controls the search and visualization systems
    :return: None
    """
    intro = 'This program is designed to help you analyse ' \
            'economics of Ukraine or any other\ncountry in ' \
            'comparison to other countries with a similar model of economics'
    warning = 'Not all countries have data for specific years, ' \
              'so the graphics might be shifted when visualized.\n' \
              'When visualizing, type all countries you would like ' \
              'to visualize one by one and type "next"'
    note = 'GDP is GDP per capita. Investment and manufacturing ' \
           'count as percent of GDP'
    print(intro)
    print('WARNING')
    print(warning)
    print('NOTE')
    print(note)

    # get information about all countries in advance
    countries = get_countries()
    country_names = []
    for country in countries:
        country_names.append(country.name)

    # get the user's choice
    choice = ''
    while choice != 'q':
        choice = input('Would you like to search or visualize?'
                       ' (s or v, q to quit) ')
        while choice not in ('s', 'v') and choice != 'q':
            choice = input('Would you like to search or visualize?'
                           ' (s or v, q to quit) ')

        # proceed to the choice
        if choice == 's':
            launch_search_system(countries, country_names)
        elif choice == 'v':
            visualize(countries, country_names)


main()
