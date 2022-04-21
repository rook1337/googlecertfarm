import requests, json
import urllib.parse
import argparse
import os

domains=[]
def getnextpagedomains(nextpage):
    try:
        url1 = requests.get("https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch/page?p="+str.strip(nextpage))
        text = url1.text
        jsondata=json.loads(str(text.replace(")]}'","")))
        for i in range(11):
            try:
                print(jsondata[0][1][i][1])
                domains.append(jsondata[0][1][i][1])
                domaincerthash=jsondata[0][1][i][5]
                getdnsnamesbycerthash(urllib.parse.quote(domaincerthash))
            except:
                pass
    except:
        pass

def getdnsnamesbycerthash(domaincerthash):
    try:
        url1 = requests.get("https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certbyhash?hash="+str.strip(domaincerthash))
        text = url1.text
        jsondata=json.loads(str(text.replace(")]}'","")))
        for i in range(int(len(jsondata[0][1][7]))):
            try:
                print(jsondata[0][1][7][i])
                domains.append(jsondata[0][1][7][i])
            except:
                pass
    except:
        pass



parser = argparse.ArgumentParser()
parser.add_argument("-d", "--Domain", help = "Enter domain like:- python3 googlecertfarm.py -d test.com")
args = parser.parse_args()
 
if args.Domain:
    domainname=str.strip(args.Domain)
else:
    exit
url = requests.get("https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch?include_subdomains=true&domain="+str.strip(domainname))
text = url.text
jsondata=json.loads(str(text.replace(")]}'","")))
domaincerthash=""
print("==================[OutSide domains]=======================\n")
for i in range(11):
    try:
        print(jsondata[0][1][i][1])
        domains.append(jsondata[0][1][i][1])
        domaincerthash=jsondata[0][1][i][5]
        getdnsnamesbycerthash(urllib.parse.quote(domaincerthash))
    except:
        pass

nextpage=jsondata[0][3][1]
allpagecount=jsondata[0][3][4]
for a in range(int(allpagecount)):
    try:
        url1 = requests.get("https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch/page?p="+str.strip(nextpage))
        text = url1.text
        jsondata=json.loads(str(text.replace(")]}'","")))
        getnextpagedomains(nextpage)
        nextpage=jsondata[0][3][1]
    except:
        pass
    

textfile = open("out.txt", "w")
for element in domains:
    textfile.write(element + "\n")
textfile.close()
print("\n=========================================[Scan Completed: check out.txt file]=========================================")
os.system('python3 dupremover.py out.txt')
