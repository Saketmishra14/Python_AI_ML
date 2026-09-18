from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime
path=Path("weather.csv")
lines=path.read_text().splitlines()

reader= csv.reader(lines)

header_row=next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
    
# Extract data from a column 

temps,dates=[],[]
for row in reader:
    temp=row[10]
    current_temp=row[2]
    temps.append(temp)
    dates.append(current_temp)
    
fix,ax=plt.subplots()
ax.plot(dates,temps,color="blue")
plt.show()
    
