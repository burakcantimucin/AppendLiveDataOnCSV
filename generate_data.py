import csv
from decimal import Decimal
import random
import datetime

with open("/your/own/path/temp_data.csv", newline=' ') as myfile:
    data = csv.reader(myfile, delimiter=',')
    temps = []
    for i in data:
        temps.append(i[5])

temps.pop(0)

minTemp = min(temps)
minTemp = round(Decimal(minTemp), 0)

maxTemp = max(temps)
maxTemp = round(Decimal(maxTemp), 0)

digit = random.randint(1,15)

newTemp = round(random.uniform(int(minTemp), int(maxTemp)), digit)

now = datetime.datetime.now()

with open("/your/own/path/temp_data.csv", "a", newline=' ') as csvfile:
    fieldnames = ["day", "month", "year", "hour", "minute", "temp"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"day": now.day, "month": now.month, "year": now.year,
                    "hour": now.hour, "minute": now.minute, "temp": newTemp})
