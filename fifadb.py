import urllib.request
import json
file1 = open("db.json", "a")
i = 1
for i in range(905):
    url = urllib.request.urlopen("https://www.easports.com/fifa/ultimate-team/api/fut/item?ovr=75:99&page="+ str(i))
    data = json.loads(url.read())
    file1.write(json.dumps(data))
file1.close()
