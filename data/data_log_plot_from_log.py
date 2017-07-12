## Plotting Rb laser data

import numpy as np
import matplotlib.pyplot as plt
import datetime,time
import matplotlib


discriminator_error = 8.4 #mV/MHz
discriminator_correction = 1.15 #mV/MHz

fname='C:\\Users\\admin\\Google Drive\\data\\logs\\780_laser_err_signal\\2017-06-27.txt'

with open(fname,) as data_file:
    data_log = data_file.readlines()


for i in range(0,len(data_log)):
    data_log[i] = data_log[i].replace('{',',')
    data_log[i] = data_log[i].replace(':',',')
    data_log[i] = data_log[i].replace('}','')
    
data = np.genfromtxt(data_log,delimiter = ',',invalid_raise = False,skip_header = 335000)

timeread = data[:,0]
error = data[:,6]*1000/discriminator_error #MsHz
correction = data[:,2]*1000/discriminator_correction #MHz

hrs = np.zeros(len(timeread))
for i in range (0,len(timeread)):
    timestamp = datetime.datetime.fromtimestamp(timeread[i]).time()
    seconds = timestamp.hour*3600 + timestamp.minute*60 + timestamp.second + timestamp.microsecond/1e6
    hrs[i] = seconds/3600
    
print len(data)
    

## optional: append a second file:
fname2='C:\\Users\\admin\\Google Drive\\data\\logs\\780_laser_err_signal\\2017-06-28.txt'

with open(fname2,) as data_file2:
    data_log2 = data_file2.readlines()


for i in range(0,len(data_log2)):
    data_log2[i] = data_log2[i].replace('{',',')
    data_log2[i] = data_log2[i].replace(':',',')
    data_log2[i] = data_log2[i].replace('}','')
    
data2 = np.genfromtxt(data_log2,delimiter = ',',invalid_raise = False)

timeread2 = data2[:,0]
error2 = data2[:,6]*1000/discriminator_error #MsHz
correction2 = data2[:,2]*1000/discriminator_correction #MHz

hrs2 = np.zeros(len(timeread2))
for i in range (0,len(timeread2)):
    timestamp = datetime.datetime.fromtimestamp(timeread2[i]).time()
    seconds = timestamp.hour*3600 + timestamp.minute*60 + timestamp.second + timestamp.microsecond/1e6
    hrs2[i] = seconds/3600 + 24


error = np.append(error,error2)
correction = np.append(correction,correction2)
hrs = np.append(hrs,hrs2)



## Generate Plot

rms_error = np.sqrt(np.mean(np.square(error)))
rms_error_mhz = rms_error/discriminator_error

xlim_lower = 0
xlim_upper = 20


fig = plt.figure()

ax1 = fig.add_subplot(111)
  
ax1.set_title("780 Laser")
ax1.set_xlabel('time [hr]')
ax1.set_ylabel('$\\Delta \\nu$ (MHz)')
ax1.set_xlim(xlim_lower,xlim_upper)
ax1.plot(hrs-14,error, c='r',label='Error Signal')
ax1.plot(hrs-14,correction-2700, c='b', label='Correction Signal')
ax1.legend(loc=2)

text_template = 'RMS Error Signal = %2.1f kHz'
plt.text(10,-200,text_template%(rms_error_mhz*1000))


plt.show()