#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
# Update the location of .csv file if you don't want it in this location
file_path = '/home/ubuntu/speedtest.csv'

# Open file, "chop it up" and print it to Check_MK-agent
with open(file_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
    # Update the speed intervals to fit your connection - I have 1000/100 Mbps.
		# The next three lines will produce one service each, if you prefer to have them as one service use the fourth line only and comment out the next three lines.
		print(f"P \"Internet ping\" ping={row[0]};20;500;0;1000 Pingtime {row[0]}ms")
		print(f"P \"Internet download\" download={row[1]};600:9999;300:9999 Download speed {row[1]} Mb/s")
		print(f"P \"Internet upload\" upload={row[2]};80:9999;50:9999 Upload speed {row[2]} Mb/s")
		# The line below will produce one service with three graphs instead of three services, if you do not want them all in one service comment out the next line.
		print(f"P \"Internet speed\" Download={row[1]};600:1000;300:1000|Upload={row[2]};80:1000;50:1000|PING={row[0]};20;500")
