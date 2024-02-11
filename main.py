# Import the library
import csv
import matplotlib.pyplot as p
import os

# User type the file name
voltage = input("Please type the Voltage file name: ")
voltage = voltage+".csv"
amps = input("Please type the Amps file name: ")
amps = amps+".csv"

# Define the empty lists
voltage_value = []
int_voltage_value = []
time_value = []
int_time_value = []

# Use True to skip the first line(The title line)
skip1 = True

if os.path.exists(voltage):
    # Open the csv file and named it as f_v
    with open(voltage, encoding="utf-8-sig") as f_v:
        csvRead1 = csv.reader(f_v)
        for row in csvRead1:
            if skip1:
                Time_title = row[0]
                Voltage_title = row[1]
                skip1 = False
            else:
                time_value.append(row[0])
                voltage_value.append(row[1])

        # Put the string item to int item process
        for item in time_value:
            int_time_value.append(int(item))
        for item in voltage_value:
            int_voltage_value.append(int(item))

print("Your voltage values are: ", int_voltage_value)

# Define the empty lists
amps_value = []
int_amps_value = []

# Use True to skip the first line(the title line)
skip2 = True

if os.path.exists(amps):
    # Open the csv file and named it as f_a
    with open(amps, encoding="utf-8-sig") as f_a:
        csvRead2 = csv.reader(f_a)
        for row in csvRead2:
            if skip2:
                Amps_title = row[0]
                skip2 = False
            else:
                amps_value.append(row[0])
        for item in amps_value:
            int_amps_value.append(float(item))

print("Your amps values are: ", int_amps_value)

# Multiply the elements in int_voltage_value and int_amps_value one by one.
# Check the length of the 2 lists.
if not len(int_voltage_value) == len(int_amps_value):
    raise ValueError("Lists must be the same length. ")

power_value = []

# Use for i in range and Multiply one by one ## IMPORTANT ##
for i in range(len(int_voltage_value)):
    power_value.append(int_voltage_value[i] * int_amps_value[i])

print("Your power values are: ", power_value)

# Calculate the average of the power
average_power_value = sum(power_value) / len(power_value)
print("The average Power is: ", average_power_value)


# MAKE THE GRAPH
p.plot(int_time_value, power_value, color="red", linewidth=2, marker="o")
p.title("Power against Time")
p.xlabel(Time_title)
p.ylabel("Power/V*A")
p.grid(linestyle="dotted")
p.axhline(color="blue", linestyle="dotted")
p.axvline(color="blue", linestyle="dotted")
p.show()

quit()