from datetime import datetime,timedelta

now=datetime.now()
print(f"Current Date And Time :{now} ")

future_date= now + timedelta(days=10)
print(f"Date 10 Days form now {future_date}")

formatted_date=now.strftime("%m/%d/%y, %H:%M:%S")
print(f"formatted date : {formatted_date}")