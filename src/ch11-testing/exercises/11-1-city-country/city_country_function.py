"""Return City, Country"""


def city_country(city_name, country_name, population=0):
    return (
        f"{city_name}, {country_name}".title()
        if not population
        else f"{city_name}, {country_name}".title() + f" - population {population}"
    )
