#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:45:18 2020

@author: riley
"""
import csv

def parse_to_csv(data, path):
    with open(path, 'w') as csvfile:
        accwr = csv.writer(csvfile)
        accwr.writerow(['time', 'ultra_sonic', 'resistor', 'x', 'y', 'z', 'orientation'])
        for line in data:
            arr = line.split(',')
            time = arr[0].split(':')[1]
            ultra_sonic = arr[1].split(':')[1]
            resistor = arr[2].split(':')[1]
            x = arr[3].split(':')[1]
            y = arr[4].split(':')[1]
            z = arr[5].split(':')[1]
            orientation = arr[6].split(':')[1]
            accwr.writerow([time, ultra_sonic, resistor, x, y, z, orientation])
        
def parse_from_txt(txt, csv):
    with open(txt, 'r') as txt_file:
        text = txt_file.readlines()
        parse_to_csv(text, csv)

if __name__=='__main__':
    parse_from_txt('2_19_test.txt', '2_19_test.csv')
