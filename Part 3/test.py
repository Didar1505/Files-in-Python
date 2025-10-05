from datetime import datetime


s1 = "15:50"
s2 = '14:10'
time1 = datetime.strptime(s1,"%H:%M")
time2 = datetime.strptime(s2, '%H:%M')
print((time1 - time2).seconds  // 60)