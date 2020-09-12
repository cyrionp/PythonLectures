from datetime import datetime

#RESOURCE: https://w3school.com/python/python_datetime.asp
#RESOURCE: https://docs.python.org/3/library/datetime.html

simdi=datetime.now()
simdi=datetime.today()

result=datetime.now()
result=simdi.year
result=simdi.month
result=simdi.day
result=simdi.hour
result=simdi.minute
result=simdi.second
result=datetime.ctime(simdi)
result=datetime.strftime(simdi,"%Y") #year
result=datetime.strftime(simdi,"%X") #exact hour and min
result=datetime.strftime(simdi,"%d") #day
result=datetime.strftime(simdi,"%A") #day name
result=datetime.strftime(simdi,"%B") #month name
result=datetime.strftime(simdi,"%Y %B %A") #year, month name, day name

t="15 April 2019 hour 10:12:30"

result=datetime.strptime(t,"%d &B %Y hour %H:%M:%S")



print(result)
