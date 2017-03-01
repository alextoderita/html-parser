#!/usr/bin/python

from bs4 import BeautifulSoup
from dateparser import parse
from datetime import datetime

now = datetime.now()
soup = BeautifulSoup(open("git.html"),"html.parser")
table = soup.find("table")
tbody = table.find('tbody')
rows = tbody.find_all('tr')
for row in rows:
 cols = row.find_all('td')
 if len(cols) == 6:
  repo = cols[0].text.strip()
  last = cols[4].text.strip()
  last_parsed = parse(last)
  diff = now - last_parsed
  days = diff.total_seconds() / 60 / 60 / 24
  if days > 30:
   print repo,int(days)
