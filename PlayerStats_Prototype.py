import urllib
from urllib import urlopen as uReq
import re
import json
import sqlite3

# htmltext = urllib.urlopen("http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/teams/celtics_roster.json")



urls = ['http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/players/playercard_1628464_02.json',
'http://data.nba.com/data/v2015/json/mobile_teams/nba/2017/players/playercard_1627759_02.json']

for url in urls:

	uClient = uReq(url)
	page_html = uClient.read()
	uClient.close()

	data = json.loads(page_html)

	# teamID = data['t']['tid']
	# team = data['t']['tn']

	for x in data['pl']['ca']['sa']:
		points = x['pts']
		conn = sqlite3.connect('NBA.db')
		cursor = conn.cursor()
		cursor.execute("INSERT INTO PlayerStats VALUES (?)", (points,))

		conn.commit()
		cursor.close()
		conn.close() 



