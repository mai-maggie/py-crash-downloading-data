from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path=Path('weather_data/death_valley_2021_simple.csv')
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)


# Extract dates, high and low temperatures.
dates,highs,lows=[],[],[]
# NOTE: Because the first row is read by next() so the loop begins at the second line.
for row in reader:
    current_date=datetime.strptime(row[2],'%Y-%m-%d')
    try:
        high=int(row[3])
        low=int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('ggplot')
fig,ax=plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Format plot.
title="Daily High and Low Temperature Data,2021\nDeath Valley,CA"
ax.set_title(title,fontsize=13)
ax.set_xlabel('',fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)',fontsize=10)
ax.tick_params(labelsize=10)

plt.show()