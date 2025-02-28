from datetime import datetime, timedelta
today= datetime.today()
yesterday = today - timedelta(days=1)
tmrw = today + timedelta(days=1)
print(today,"; " ,yesterday,"; " ,tmrw)