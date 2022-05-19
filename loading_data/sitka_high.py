import csv
from datetime import datetime
from matplotlib import pyplot as plt


# filename = 'sitka_weather_2018_simple.csv'
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Чтение максимальных температур
    # for index, column_header in enumerate(header_row):
    #     print(index, '---->', column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Нанесение данных на диаграмму.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    # Форматирование диаграммы.
    plt.title('Daily high and low temperatures - 2018', fontsize=10)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()





