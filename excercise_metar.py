import requests
from lxml import etree
r = requests.get("https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=LKTB,%20PHNL&hoursBeforeNow=2")
tree = etree.fromstring(r.content)
for element in tree.findall('.//data/METAR'):
        time = element.find('./observation_time').text
        temp = element.find('./temp_c').text
        print('{} - {}'.format(time, temp))