#!/usr/local/env python
# -*- coding: utf-8 -*-
import os
import csv
import time
import subprocess
from decimal import *

# Update the location of .csv file if you don't want it in this location
file_path = '/home/ubuntu/speedtest.csv'

#Start by deleting the file if it allready exists
if os.path.exists('/home/ubuntu/speedtest.csv'):
  os.remove('/home/ubuntu/speedtest.csv')

def format_speed(bits_string):
  # changes string bit/s to megabits/s and rounds to two decimal places 
  return (Decimal(bits_string) / 1000000).quantize(Decimal('.01'), rounding=ROUND_UP)

def write_csv(row):
  # Write the file, if it does not exist it will be created
  with open(file_path, 'a+', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    writer.writerow(row)

response = subprocess.run(['/usr/bin/speedtest', '--accept-gdpr', '--format=csv'], capture_output=True, encoding='utf-8')

 # if speedtest-cli exited with no errors / ran successfully
if response.returncode == 0:

 # csv.reader returns an iterator, so we turn that into a list
  cols = list(csv.reader([response.stdout]))[0]

  # turns 13.45 ping to 13
  ping = Decimal(cols[2]).quantize(Decimal('1.'))

  # speedtest-cli --csv returns speed in bytes/s, convert to bits by multiplying it by 8
  download = 8 * format_speed(cols[5])
  upload = 8 * format_speed(cols[6])

  write_csv([ping,download,upload])

else:
  print('speedtest-cli returned error: %s' % response.stderr)
