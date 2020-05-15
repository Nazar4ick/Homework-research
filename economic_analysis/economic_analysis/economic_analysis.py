import countries_data as countries_data
import matplotlib.pyplot as plt
from custom_array import Array


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
        max_year = 2018
        commands = ('gdp', 'investment_inflows', 'investment_outflows',
                    'manufacturing')
        print(commands)
        command = input('What would you like to learn? ').lower()
        while command not in commands:
            command = input('What would you like to learn? ').lower()
        # find the desired command
        if command == 'gdp':
            info = searched.gdp
        elif command == 'investment_inflows':
            info = searched.investment_inflows
        elif command == 'investment_outflows':
            info = searched.investment_outflows
            # there is no data for outflows further than 2013
            max_year = 2013
        else:
            info = searched.manufacturing

        # Move on to the year
        min_year = searched.min_indexes[command]
        print(f'the minimal year is {min_year}, maximum: {max_year}')
        year = 1
        while not min_year <= year <= max_year:
            year = input("What year's info are you looking for? ")
            while True:
                try:
                    year = int(year)
                    break
                except ValueError:
                    year = input("What year's info are you looking for? ")
        # display the info
        if command == 'manufacturing' and min_year < 1995:
            # fix an error with index error
            year -= 2
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
                     ' ("all" to add all, type "next" to proceed) ')
        while name not in country_names and name != 'next' and name != 'all':
            name = input('What countries would you like to investigate?'
                         ' ("all" to add all, type "next" to proceed) ')
        chosen_names.append(name)

    # add chosen countries
    for name in chosen_names:
        for country in countries:
            if name == country.name:
                requested_countries.append(country)
            elif name == 'all':
                requested_countries = countries
                break

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
    year_info = get_max_base_year(countries, info)
    base_year = year_info[0]
    all_years = year_info[1]

    if info == 'gdp':
        for country in countries:
            slice_from = base_year - country.min_indexes[info]
            plt.plot(all_years, country.gdp[slice_from:],
                     label=country.name)
    elif info == 'investment_inflows':
        for country in countries:
            slice_from = base_year - country.min_indexes[info]
            plt.plot(all_years, country.investment_inflows[slice_from:],
                     label=country.name)
    elif info == 'investment_outflows':
        for country in countries:
            slice_from = base_year - country.min_indexes[info]
            # not all countries have info for 2014th year
            plt.plot(all_years,
                     country.investment_outflows[slice_from:2014 - base_year],
                     label=country.name)
    elif info == 'manufacturing':
        for country in countries:
            slice_from = base_year - country.min_indexes[info]
            # some countries have different start years, but have
            # the same amount of data, which causes an Error
            # Lithuania is an exception
            if slice_from >= 4 and country.name not in ('Lithuania', 'Latvia'):
                slice_from = 4
            elif len(all_years) != len(country.manufacturing[slice_from:]):
                all_years = all_years[len(all_years) -
                                      len(country.manufacturing[slice_from:]):]
            plt.plot(all_years, country.manufacturing[slice_from:],
                     label=country.name)
    plt.legend()
    plt.show()


def get_max_base_year(countries, info):
    """
    gets the max base year, so that the graphics don't shift
    and start from the same point
    :param countries: lst
    :param info: str
    :return: int
    """
    base_years = []
    max_year = 2018
    if info == 'investment_outflows':
        max_year = 2013
    for country in countries:
        base_years.append(country.min_indexes[info])
    base_year = max(base_years)
    # create an array, so there is no conflict when plotting
    all_years = Array(max_year + 1 - base_year)
    # get all years for the x axis
    for i in range(len(all_years)):
        all_years[i] = base_year + i
    return base_year, all_years


def main():
    """
    Controls the search and visualization systems
    :return: None
    """
    intro = 'This program is designed to help you analyse ' \
            'economics of Ukraine or any other\ncountry in ' \
            'comparison to other countries with a similar model of economics'
    warning = 'When visualizing, type all countries you would like ' \
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
