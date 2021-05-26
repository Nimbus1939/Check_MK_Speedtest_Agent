#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
# Update the location of .csv file if you don't want it in this location
file_path = '/home/ubuntu/speedtest.csv'

# Open file, "chop it up" and print it to Check_MK-agent
with open(file_path) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
    # Update the intervals to fit your connection - I have 1000/100 Mbps.
		print(f"P \"Internet ping\" ping={row[0]};20;500;0;1000 Pingtime {row[0]}ms")
		print(f"P \"Internet download\" download={row[1]};600:9999;300:9999 Download speed {row[1]} Mb/s")
		print(f"P \"Internet upload\" upload={row[2]};80:9999;50:9999 Upload speed {row[2]} Mb/s")
