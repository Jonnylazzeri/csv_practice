import pandas

# csv_list = []
#
# with open('weather_data.csv') as file:
#     csv_list = (file.readlines())
#
# print(csv_list)
#
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# data = pandas.read_csv('weather_data.csv')
#
# # print(data)
# # print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# reducer = 0
# for temp in temp_list:
#     reducer += temp
# avg_weather = reducer / len(temp_list)
# print(avg_weather)

# avg = data['temp'].mean()
# maximum = data['temp'].max()
# print(maximum)
#
# print(data['condition'])
# print(data.condition)

# print(data[data.day == "Wednesday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

# data_dict = {
#     "students": ["Amy", "James", "Fabio"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

black_count = 0
cinnamon_count = 0
gray_count = 0

color_set = set(data["Primary Fur Color"])
color_set.pop()
color_set = list(color_set)
print(color_set)

fur_list = data["Primary Fur Color"].to_list()


for color in fur_list:
    if color == "Black":
        black_count += 1
    elif color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1

data_dict = {
    'colors': color_set,
    'amount': [black_count, gray_count, cinnamon_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_squirrel_data.csv")
print(data)

