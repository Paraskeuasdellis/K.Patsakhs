import json
import urllib
url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/.json"
x = raw_input("Please Enter Date(ex. dd-MM-yyyy)\n")
url = ("http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json"%x)

response = urllib.urlopen(url)
data = json.loads(response.read())
w = str(data)
nums =[]
k = json.loads(w)
for i in range(0,len(k["draws"]["draw"])):
    nums.append(k["draws"]["draw"][i]["results"])

print nums
