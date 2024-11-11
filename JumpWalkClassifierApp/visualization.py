#
# ELEC 292 Final Project - Group 53
# Created by Boyan Fan, Naman Nagia, Walker Yee on 03/28/2024
#

import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with h5py.File('./dataset.h5','r') as hdf:
    '''randomly select three segments from both walking 
    and jumping to visulalize'''

    walking_set1=hdf.get(f'Dataset/Train/segment{0}') #get data from hdf5 file
    #print(type(walking_set1))
    walk_array1=np.array(walking_set1) #convert data to ndarray
    #print(type(walk_array1))
    #print(walk_array1.shape)
    #print(walk_array1[0][4])

    walking_set2=hdf.get(f'Dataset/Train/segment{30}')
    walk_array2 = np.array(walking_set2)
    #print(walk_array2[0][4])

    walking_set3 = hdf.get(f'Dataset/Train/segment{56}')
    walk_array3 = np.array(walking_set3)
    #print(walk_array3[0][4])

    jump_set1 = hdf.get(f'Dataset/Train/segment{74}')
    jump_array1 = np.array(jump_set1)
    #print(jump_array1[0][4])

    jump_set2 = hdf.get(f'Dataset/Train/segment{86}')
    jump_array2 = np.array(jump_set2)
    #print(jump_array2[0][4])

    jump_set3 = hdf.get(f'Dataset/Train/segment{140}')
    jump_array3 = np.array(jump_set3)
    #print(jump_array3[0][4])

#Plot acceleration vs time for all three dimensions of each segment(18 plots total)

x_accelwalk1_data=walk_array1[:,1]
time1=walk_array1[:,0]
plt.xlabel("Time(s)")
plt.ylabel("x Acceleration(m/s^2)")
plt.title("Walking Sample 1: x Acceleration")
plt.plot(time1,x_accelwalk1_data)

plt.show()

y_accelwalk1_data=walk_array1[:,2]
plt.xlabel("Time(s)")
plt.ylabel("y Acceleration(m/s^2)")
plt.title("Walking Sample 1: y Acceleration")
plt.plot(time1,y_accelwalk1_data)

plt.show()

z_accelwalk1_data=walk_array1[:,3]
plt.xlabel("Time(s)")
plt.ylabel("z Acceleration(m/s^2)")
plt.title("Walking Sample 1: z Acceleration")
plt.plot(time1,z_accelwalk1_data)

plt.show()


x_accelwalk2_data=walk_array2[:,1]
time2=walk_array2[:,0]
plt.xlabel("Time(s)")
plt.ylabel("x Acceleration(m/s^2)")
plt.title("Walking Sample 2: x Acceleration")
plt.plot(time2,x_accelwalk2_data)
plt.show()

y_accelwalk2_data=walk_array2[:,2]
plt.xlabel("Time(s)")
plt.ylabel("y Acceleration(m/s^2)")
plt.title("Walking Sample 2: y Acceleration")
plt.plot(time2,y_accelwalk2_data)

plt.show()

z_accelwalk2_data=walk_array2[:,3]

plt.xlabel("Time(s)")
plt.ylabel("z Acceleration(m/s^2)")
plt.title("Walking Sample 2: z Acceleration")
plt.plot(time2,z_accelwalk2_data)

plt.show()

x_accelwalk3_data=walk_array3[:,1]
time3=walk_array3[:,0]
plt.xlabel("Time(s)")
plt.ylabel("x Acceleration(m/s^2)")
plt.title("Walking Sample 3: x Acceleration")
plt.plot(time3,x_accelwalk3_data)
plt.show()

y_accelwalk3_data=walk_array3[:,2]
plt.xlabel("Time(s)")
plt.ylabel("y Acceleration(m/s^2)")
plt.title("Walking Sample 3: y Acceleration")
plt.plot(time3,y_accelwalk3_data)
plt.show()

z_accelwalk3_data=walk_array3[:,3]
plt.xlabel("Time(s)")
plt.ylabel("z Acceleration(m/s^2)")
plt.title("Walking Sample 3: z Acceleration")
plt.plot(time3,z_accelwalk3_data)
plt.show()

x_acceljump1_data=jump_array1[:,1]
time4=jump_array1[:,0]
plt.xlabel("Time(s)")
plt.ylabel("x Acceleration(m/s^2)")
plt.title("Jumping Sample 1: x Acceleration")
plt.plot(time4,x_acceljump1_data)
plt.show()

y_acceljump1_data=jump_array1[:,2]
plt.xlabel("Time(s)")
plt.ylabel("y Acceleration(m/s^2)")
plt.title("Jumping Sample 1: y Acceleration")
plt.plot(time4,y_acceljump1_data)
plt.show()

z_acceljump1_data=jump_array1[:,3]
plt.xlabel("Time(s)")
plt.ylabel("z Acceleration(m/s^2)")
plt.title("Jumping Sample 1: z Acceleration")
plt.plot(time4,z_acceljump1_data)
plt.show()

x_acceljump2_data=jump_array2[:,1]
time5=jump_array2[:,0]
plt.xlabel("Time(s)")
plt.ylabel("x Acceleration(m/s^2)")
plt.title("Jumping Sample 2: x Acceleration")
plt.plot(time5,x_acceljump2_data)
plt.show()

y_acceljump2_data=jump_array2[:,2]
plt.xlabel("Time(s)")
plt.ylabel("y Acceleration(m/s^2)")
plt.title("Jumping Sample 2: y Acceleration")
plt.plot(time5,y_acceljump2_data)
plt.show()

z_acceljump2_data=jump_array2[:,3]
plt.xlabel("Time(s)")
plt.ylabel("z Acceleration(m/s^2)")
plt.title("Jumping Sample 2: z Acceleration")
plt.plot(time5,z_acceljump2_data)
plt.show()


x_acceljump3_data=jump_array3[:,1]
time6=jump_array3[:,0]
plt.xlabel("Time(s)")
plt.ylabel("x Acceleration(m/s^2)")
plt.title("Jumping Sample 3: x Acceleration")
plt.plot(time6,x_acceljump3_data)
plt.show()

y_acceljump3_data=jump_array3[:,2]
plt.xlabel("Time(s)")
plt.ylabel("y Acceleration(m/s^2)")
plt.title("Jumping Sample 3: y Acceleration")
plt.plot(time6,y_acceljump3_data)
plt.show()

z_acceljump3_data=jump_array3[:,3]
plt.xlabel("Time(s)")
plt.ylabel("z Acceleration(m/s^2)")
plt.title("Jumping Sample 3: z Acceleration")
plt.plot(time6,z_acceljump3_data)
plt.show()


#Graphing the same dimension of walking and jumping against each other

#Create a new array by concatenating each segment together
all_x_walk=np.concatenate((x_accelwalk1_data,x_accelwalk2_data,x_accelwalk3_data),axis=None)
all_x_jump=np.concatenate((x_acceljump1_data,x_acceljump2_data,x_acceljump3_data),axis=None)
plt.ylabel("x Acceleration(m/s^2)")
time_15s=[]
for x in range(0,2258):
    time_15s.append(x*(15/2258))

plt.title("Walking and Jumping: x Acceleration")
plt.ylabel("x Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.plot(time_15s,all_x_walk)
plt.plot(time_15s,all_x_jump)
plt.legend(["Walking","Jumping"],loc="upper right")
plt.show()

#Graph same as above but in y dimension
all_y_walk=np.concatenate((y_accelwalk1_data,y_accelwalk2_data,y_accelwalk3_data),axis=None)
all_y_jump=np.concatenate((y_acceljump1_data,y_acceljump2_data,y_acceljump3_data),axis=None)
plt.title("Walking and Jumping: y Acceleration")
plt.ylabel("y Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.plot(time_15s,all_y_walk)
plt.plot(time_15s,all_y_jump)
plt.legend(["Walking","Jumping"],loc="upper right")
plt.show()

#Graph same as above but in z dimension
all_z_walk=np.concatenate((z_accelwalk1_data,z_accelwalk2_data,z_accelwalk3_data),axis=None)
all_z_jump=np.concatenate((z_acceljump1_data,z_acceljump2_data,z_acceljump3_data),axis=None)
plt.title("Walking and Jumping: z Acceleration")
plt.ylabel("z Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.plot(time_15s,all_z_walk)
plt.plot(time_15s,all_z_jump)
plt.legend(["Walking","Jumping"],loc="upper right")
plt.show()

#Plot all 3 walking dimension data in graph
plt.title("Walking: Acceleration in All Dimensions")
plt.ylabel("Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.plot(time_15s,all_x_walk)
plt.plot(time_15s,all_y_walk)
plt.plot(time_15s,all_z_walk)
plt.legend(["x Acceleration","y Acceleration", "z Acceleration"],loc="upper right")
plt.show()

#Plot all 3 jumping dimension data in graph
plt.title("Jumping: Acceleration in All Dimensions")
plt.ylabel("Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.plot(time_15s,all_x_jump)
plt.plot(time_15s,all_y_jump)
plt.plot(time_15s,all_z_jump)
plt.legend(["x Acceleration","y Acceleration", "z Acceleration"],loc="upper right")
plt.show()

#Create plot for how data was collected
data_collection_time = 16
labels='Walking with Phone in Hand', 'Walking with Phone Back Pocket', 'Walking with Phone in Front Pocket', 'Walking with Phone in Jacket Pocket', 'Jumping with Phone in Hand', 'Jumping with Phone in Back Pocket', 'Jumping with Phone in Front Pocket', 'Jumping with Phone in Jacket Pocket'
sizes=[8/data_collection_time,8/data_collection_time,8/data_collection_time,8/data_collection_time,
       8/data_collection_time,8/data_collection_time,8/data_collection_time,8/data_collection_time]
plt.title("Allocation of Time for Data Collection")
plt.pie(sizes,labels=labels,textprops={'size':'smaller'},radius=0.6)
plt.show()

#Find the mean of the data
walking_x_mean=np.mean(all_x_walk)
walking_y_mean=np.mean(all_y_walk)
walking_z_mean=np.mean(all_z_walk)
jumping_x_mean=np.mean(all_x_jump)
jumping_y_mean=np.mean(all_y_jump)
jumping_z_mean=np.mean(all_z_jump)

#Plot the mean of each set of data on a bar graph
titles=["x Walking", "y Walking","z Walking", "x Jumping", "y Jumping", "z Jumping"]
means=[walking_x_mean,walking_y_mean,walking_z_mean,jumping_x_mean,jumping_y_mean,jumping_z_mean]
bar_colours=["blue","red","green","blue","red","green"]
plt.title("Mean Acceleration")
plt.ylabel("Acceleration(m/s^2)")
plt.xlabel("Time(s)")
plt.bar(titles,means,color=bar_colours)
plt.show()