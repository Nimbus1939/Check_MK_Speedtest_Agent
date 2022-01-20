#!/usr/local/env python
# -*- coding: utf-8 -*-
import os
import csv
import time
import subprocess
from decimal import *

file_path = '/home/ubuntu/speedtest.csv'
if os.path.exists('/home/ubuntu/speedtest.csv'):
  os.remove('/home/ubuntu/speedtest.csv')

def format_speed(bits_string):
  # changes string bit/s to megabits/s and rounds to two decimal places 
  return (Decimal(bits_string) / 1000000).quantize(Decimal('.01'), rounding=ROUND_UP)

def write_csv(row):
  # writes a header row if one does not exist and test result row 
  # straight from csv man page
  # see: https://docs.python.org/3/library/csv.html
  with open(file_path, 'a+', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')

    #if os.stat(file_path).st_size == 0:
      #writer.writerow(['Date','Time','Ping','Download (Mbit/s)','Upload (Mbit/s)','myip'])

    writer.writerow(row)


response = subprocess.run(['/usr/bin/speedtest', '--accept-gdpr', '--format=csv'], capture_output=True, encoding='utf-8')

 # if speedtest-cli exited with no errors / ran successfully
if response.returncode == 0:

 # from the csv man page
 # And while the module doesn’t directly support parsing strings, it can easily be done
 # this will remove quotes and spaces vs doing a string split on ','
 # csv.reader returns an iterator, so we turn that into a list
  cols = list(csv.reader([response.stdout]))[0]

  # turns 13.45 ping to 13
  ping = Decimal(cols[2]).quantize(Decimal('1.00'))
  jitter = Decimal(cols[3]).quantize(Decimal('1.00'))
  # speedtest-cli --csv returns speed in bits/s, convert to bytes
  download = 8 * format_speed(cols[5])
  hdownload = (Decimal(cols[5]) * 8)
  hupload = (Decimal(cols[6]) * 8)
  upload = 8 * format_speed(cols[6])

  write_csv([ping,download,upload,jitter,hdownload,hupload])

else:
  print('speedtest-cli returned error: %s' % response.stderr)
