import urllib.request
urllib.request.urlretrieve("http://www.google.com/","webpage.html")
for line in open('webpage.html'):
    print(line.strip())

