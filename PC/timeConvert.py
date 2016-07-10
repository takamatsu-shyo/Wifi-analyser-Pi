import csv
import iso8601
import calendar
from datetime import datetime

# convert iso8601 to epoch
with open('./0609/20160609.csv', 'r') as csvinput:
  with open('./0609/201609_epoch.csv','w') as csvoutput:
    reader = csv.reader(csvinput)
    writer = csv.writer(csvoutput, lineterminator='\n')

    all = []
    row = reader.next()
    row.append('epoch')
    all.append(row)

    for row in reader:
      myDate = iso8601.parse_date(row[0])

      row.append(calendar.timegm(myDate.timetuple()))
      all.append(row)
    writer.writerows(all)
