# Print Date and Time
## Write a Python Program to display the current date and time.

# datetime function
print("[datetime function]")
import datetime

cd=datetime.datetime.today()
print(cd)

# strftime method
print("\n")
print("[strftime method]")
from datetime import datetime
now = datetime.now()
ct = now.strftime("%H:%M:%S")
td = now.strftime("%m/%d/%y")
print("Date:",td,"\n","Current Time:",ct)
