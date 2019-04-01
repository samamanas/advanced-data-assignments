# Imports the standard Python libraries urllib2 (used to work
# with websites) and csv (used to work with .csv files)
import urllib2, csv
# Imports the BeautifulSoup portion of the bs4 package
from bs4 import BeautifulSoup

# Opens the file jaildata.csv in write mode, assigns
# it the variable name outfile
outfile = open('jaildata.csv', 'w')

# Calls the writer function of the csv library on outfile which reads
# data, converts it to delimited strings and returns that result. Because
# outfile is being called, those returned strings will be written to jaildata.csv
writer = csv.writer(outfile)

# Sets the URL to reference as a string variable
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
# Sets html to the result of running the standard Python function read() on the
# contents of the URL (in this case, variable url) opened by urlopen(), a
# function from library urllib2 that opens a URL for processing in Python
html = urllib2.urlopen(url).read()

# Runs the BeautifulSoup constructor, which interprets a web page, on the data
# from the read function. It's run on the html variable, which is the data
# read from the url argument passed into urlopen. It's using Python's built-in
# HTML parser
soup = BeautifulSoup(html, "html.parser")

# Pulls the first instance of the tbody tag in the html that has a stripe class
tbody = soup.find('tbody', {'class': 'stripe'})

# Pulls any and all instances of the tr HTML tag
rows = tbody.find_all('tr')

# starts a loop that iterates through each instance of the table row (tr) tag
for row in rows:

    # sets variable cells equal to each instance of the table cell (td) tag in each row
    cells = row.find_all('td')

    # creates an empty list to dump cells into
    data = []
    # a secondary loop for each cell in each table row
    for cell in cells:
        # addes the text of each cell, encoded in utf-8, to the data list
        data.append(cell.text.encode('utf-8'))

    # writes the row of data you've collected
    writer.writerow(data)
