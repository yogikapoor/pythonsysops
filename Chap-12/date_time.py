import datetime # from datetime import datetime
import pytz
print(dir(datetime))
print(datetime.datetime.now())
print(datetime.datetime.today())

ist = pytz.timezone('Asia/kolkata')
print(datetime.datetime.now(ist))
print(datetime.datetime.now().strftime("%y-%m-%d"))