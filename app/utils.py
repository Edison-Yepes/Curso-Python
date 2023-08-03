def get_population(Country_dict):
  population_dict={ 
    '2022': int(Country_dict['2022 Population']),
    '2020': int(Country_dict['2020 Population']),
    '2015': int(Country_dict['2015 Population']),
    '2010': int(Country_dict['2010 Population']),
    '2000': int(Country_dict['2000 Population']),
    '1990': int(Country_dict['1990 Population']),
    '1980': int(Country_dict['1980 Population']),
    '1970': int(Country_dict['1970 Population'])
  }

  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_by_country(data, Country):
  result = list(filter(lambda item: item['Country/Territory'] == Country, data))
  return result