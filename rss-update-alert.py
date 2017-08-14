from urllib2 import urlopen
import xml.etree.ElementTree as ET
import requests
import time
import os
import datetime

def read_feed():
    write_log("reading feed")
    return urlopen(
        'https://iptorrents.com/torrents/rss?u=379571;tp=10a38607b96146711f6191a48263c5e3;78;23;25;66;82;65;79;22;5;99')\
        .read()
def write_log(s):    
    with open('logfile.out', 'a+') as f:
        f.write('time: %s Action: %s \n' % (str(datetime.datetime.now()), s))


# tree = ET.parse(rss_xml)
# root = tree.getroot()

root = ET.fromstring(read_feed())
write_log("Starting search")
end_flag = False
while True:
    time.sleep(30)
    root = ET.fromstring(read_feed())
    for item in root.findall('channel/item'):
        title = item.find('title').text
        if 'Rick and Morty' in title and 'S03E04' in title:
            write_log("Found Morty")
            end_flag = True
            r = requests.post(
                'http://timothy-z-searcy.com/email_form',
                data={
                    'name' : 'Testing',
                    'email' : 'Test 2 tim',
                    'request' : 'rick'
                })
            break
    if end_flag:
        break
