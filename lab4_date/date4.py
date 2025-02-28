from datetime import datetime
date1 = datetime.fromisoformat(input())
date2 = datetime.fromisoformat(input())
res = abs(int((date2 - date1).total_seconds()))
print(int(res))