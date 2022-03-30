import json
import locale

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data
  
def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  car_model = {}
  car_year = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item['car']['car_model'] not in car_model.keys():
      car_model[item['car']['car_model']] = item['total_sales']
    else:
      car_model[item['car']['car_model']] += item['total_sales']
    # TODO: also handle most popular car_year
    if item['car']['car_year'] not in car_year.keys():
      car_year[item['car']['car_year']] = item['total_sales']
    else:
      car_year[item['car']['car_year']] +=  item['total_sales']
  
  max_sales = max(car_model, key=lambda key: car_model[key])
  popular_car_year = max(car_year, key=lambda key: car_year[key])
  
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    f"The {max_sales} had the most sales: {car_model[max_sales]}",
    f"The most popular year was {popular_car_year} with {car_year[popular_car_year]} sales."
  ]

  return (car_model, car_year)


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [[" ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

def main():
    json = load_data('car_sales.json')
    # bruh = process_data(json)
    # print(bruh)
    # print(json)

main()
