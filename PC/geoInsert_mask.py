import csv
import iso8601
import calendar
import re
from datetime import datetime

# caliculate geo location in the middle of two points
def correction(deltaT, deltaTl, deg, degL):
    if deltaT < 0:
        totalDelta = deltaTl - deltaT
        degDiff    = degL    - deg
        resultDeg  = deg + degDiff * (-1) * deltaT / totalDelta

    else:
        totalDelta = deltaT - deltaTl
        degDiff    = degL   - deg
        resultDeg  = deg + degDiff * deltaT / totalDelta

    return resultDeg

# masking MAC address to publish
def extract(a_list, w_row):
    for i, w_info in enumerate(w_row):
        if i != 0 and w_info != "**:**:**:**:**:**": # in case your mobile AP is in the list
            masked = re.sub('([0-9A-F]{2}:)([0-9A-F]{2}:)([0-9A-F]{2}:)([0-9A-F]{2}:)([0-9A-F]{2}:)([0-9A-F]{2})',r'\1\2\3\4**:**',w_info)
            a_list.append(masked)
    return 0

# file Input
folder = "./0609/"
wifiinputFile = folder + "wifilist_mac_timetrim.csv"
geo_inputFile = folder + "20160609_epoch.csv"

wifiinput = file(wifiinputFile,'r')
geo_input = file(geo_inputFile, 'r')
wifireader = csv.reader(wifiinput)
geo_reader = csv.reader(geo_input)


geo_list = list(geo_reader)
deltaTl = 0

# buffer for wrinting
a_list = []
listOfList = []

# first line of csv, titles
a_list.append("lat")
a_list.append("lon")

for i in range(50):
    title = "MAC" + str(i)
    a_list.append(title)

listOfList.append(a_list)
a_list = []


next(wifireader,None)
for w_row in wifireader:
    for g_row in geo_list:
        if g_row[9] == "epoch": #skip first line
            continue

        deltaT = int(w_row[0]) - int(g_row[9])
        if deltaT == 0:
            lat = g_row[1]
            lon = g_row[2]

            a_list.append(lat)
            a_list.append(lon)
            extract(a_list, w_row)
            print lon
        elif deltaT*deltaTl < 0:
            lat = g_row[1]
            lon = g_row[2]
            lat = correction(deltaT, deltaTl, float(g_row[1]), float(latL))
            lon = correction(deltaT, deltaTl, float(g_row[2]), float(lonL))
            print deltaT, deltaTl, float(g_row[2]), float(lonL), lon
            a_list.append(lat)
            a_list.append(lon)
            extract(a_list, w_row)
            #print a_list

        deltaTl = deltaT   # for next loop
        latL    = g_row[1]
        lonL    = g_row[2]

    deltaTl = 0
    listOfList.append(a_list)
    a_list = []

# file Output
outputFile = folder + "mydata0609_geo_mask.csv"
with open(outputFile, 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile)
    for row in listOfList:
        thedatawriter.writerow(row)


wifiinput.close()
geo_input.close()
