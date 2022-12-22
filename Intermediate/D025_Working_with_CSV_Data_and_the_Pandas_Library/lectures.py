# with open("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/weather_data.csv") as data_file:
#   data = data_file.readlines()
#   print(data)

# import csv

# with open("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperature = []
#   for row in data:
#     if row[1].isnumeric():
#       temperature.append(int(row[1]))
#   print(temperature)

import pandas

# data = pandas.read_csv("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/weather_data.csv")
# print(type(data)) #Series
# print(data["temp"]) 

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# ave_temp = data["temp"].mean()
# print(ave_temp)

# max_temp = data["temp"].max()
# print(max_temp)

# # get data in columns
# print(data["condition"])
# print(data.condition)

# # get data in Row by the request day
# print(data)
# print(data[data.day == "Monday"])

# # get data from max temp 
# print(data[data.temp == max_temp])

# # get the condition in specific row
# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp_F = int(monday.temp) * 9/5 + 32
# print(monday_temp_F)

# data_dict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/new_data.csv")

data = pandas.read_csv("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
  "Fur Color": ["Gray", "Black", "Cinnamon"],
  "Count": [gray, black, cinnamon],
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Intermediate/D025_Working_with_CSV_Data_and_the_Pandas_Library/squirrel_count.csv")
