import urllib.request
import json
file1 = open("databaseGiocatoriFifa.json", "a")
i = 0
for i in range(909):
    url = urllib.request.urlopen("https://www.easports.com/fifa/ultimate-team/api/fut/item?ovr=40:99&page="+ str(i))
    data = json.loads(url.read())
    file1.write(json.dumps(data))
file1.close()
