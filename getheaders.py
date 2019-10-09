from urllib.request import urlopen

#print the html header information
url = input("what address do you wish to go to ?:")
if "http://" not in url:
    url = "http://"+url
res = urlopen(url)
output = res.getheaders()
for line in output:
    print(line)
#print(res.getheaders())