from datetime import datetime, timedelta
time = datetime.now()
without = time.replace(microsecond=0)
print(without)