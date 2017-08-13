from urllib2 import urlopen
import xml.etree.ElementTree as ET
import requests

rss_xml = urlopen(
    'https://iptorrents.com/torrents/rss?u=379571;tp=10a38607b96146711f6191a48263c5e3;78;23;25;66;82;65;79;22;5;99')\
    .read()

# tree = ET.parse(rss_xml)
# root = tree.getroot()

root = ET.fromstring(rss_xml)

while True:
    for item in root.findall('channel/item'):
       title = item.find('title').text
       if 'Rick and Morty' and 'S03E04' in title:
            r = requests.post(
                'http://timothy-z-searcy.com/email_form',
                data={
                    'name' : 'Testing',
                    'email' : 'Test 2 tim',
                    'request' : 'rick'
                })