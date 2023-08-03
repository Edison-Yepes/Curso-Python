import utils
import read_csv
import chart

def run():
  data = read_csv.read_csv('./app/data.csv')
  Country = input('Type Country => ')
  result = utils.population_by_country(data, Country)

  if len(result) > 0:
    Country = result[0]
    labels, values = utils.get_population(Country)
    chart.generate_bar_chart(labels, values)


if __name__ == '__main__':
  run()