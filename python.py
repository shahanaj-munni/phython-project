import matplotlib.pyplot as plt
import numpy as np
humidity3pm=[]
Pressure9am=[]
fpr=open("C:\\Users\\HomePC\\Downloads\\weather.csv","r")
head=fpr.readline()
line=fpr.readline()
while(len(line)>0):
    arr=line.strip().split(',')
    humidity3pm.append(float(arr[12]))
    Pressure9am.append(float(arr[13]))
    line=fpr.readline()
fpr.close()
humidity3pm_score=np.array(humidity3pm)
average=np.mean(humidity3pm)
lowest=np.min(humidity3pm)
highest=np.max(humidity3pm)
print('Average humidity3pm score is',average)
print('Lowest humidity3pm score is ',lowest)
print('Highest humidity3pm score is',highest)

Pressure9am_score=np.array(Pressure9am)
average=np.mean(Pressure9am)
lowest=np.min(Pressure9am)
highest=np.max(Pressure9am)
print('Average Pressure9am score is',average)
print('Lowest Pressure9am score is ',lowest)
print('Highest Pressure9am score is',highest)



plt.plot(humidity3pm_score,label='humidity3pm_score',color='blue',marker='*')
Y=np.random.randint(0,100,10)
plt.title('Weather Forecast')
plt.xlabel('Index')
plt.ylabel('humidity3pm_score')

plt.legend()
plt.show()