# Metis coding challenge
# Find details about commits in D3 repository

import math
import sys
import os
import datetime
import matplotlib.pyplot as plt
import calendar

# Ask for file path
filepath = raw_input("Enter file path:")
filepath = filepath.replace(" ","")

# Check if file path is correct
if os.path.isfile(filepath):
	print "Found the file."
else:
	print "Path incorrect, exiting."
	sys.exit()

# Create empty list
mylist = []

# Create dictionary of week numbers for tally
weekcount = {}
for i in range(1,54):
	weekcount[i] = 0

# Create dictionary of abbreviated month names and numbers
monthref = {}
for i in range(1,13):
	monthref[calendar.month_abbr[i]] = i

# Create counts for days of the week (extra credit)
dayscount = { "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0 }

# Open file
with open(filepath, "r") as f:
	
	for line in f:
		
		if line.startswith("Date:"):

			# Add date of commit to list
			if line[17] == " ":
				mylist.append(line[12:17] + " " + line[27:31])	
			else: 
				mylist.append(line[12:18] + " " + line[28:32])
			
			# Check day of week and tally results
			if line[8:11] == "Mon":
				dayscount["Mon"] += 1
			elif line[8:11] == "Tue":
				dayscount["Tue"] += 1
			elif line[8:11] == "Wed":
				dayscount["Wed"] += 1
			elif line[8:11] == "Thu":
				dayscount["Thu"] += 1
			elif line[8:11] == "Fri":
				dayscount["Fri"] += 1
			elif line[8:11] == "Sat":
				dayscount["Sat"] += 1
			elif line[8:11] == "Sun":
				dayscount["Sun"] += 1


# Print out day of week with maximum number of commits
print "Day with most commits: " + str(max(dayscount, key=dayscount.get))

# Transform the date to the fiscal week number, and tally up in the dictionary, print result
for i in mylist:
	 weekcount[datetime.date(int(i[7:]), int(monthref[i[0:3]]), int(i[4:6])).isocalendar()[1]] += 1

print "Week number with most number of commits: " + str(max(weekcount, key=weekcount.get))

# Graph number of commits by day of the week
plt.bar(range(len(dayscount)), dayscount.values(), align = "center")
plt.xticks(range(len(dayscount)), dayscount.keys())
plt.show()

sys.exit()


