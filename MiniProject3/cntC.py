import pymongo, sys
#client = pymongo.MongoClient () # the gcp instance forwards back to da1
client = pymongo.MongoClient (host='localhost') # use this instead if running on da0
db = client ['fdac23mp3']

#print ("|id|result|\n|--|--|")

#for l in db.clusters.find ({ "$where": "function() { return this.label != this.cluster_name }" }):
f = open("../students/NetID2GHID.md")

'''
"id" : "CVE-2019-20107",
"commit" : "146b4f38010a48c36b7d9650060ca354c92ab4ac",
"inWoC" : 1,
"project" : "https://github.com/TestLinkOpenSourceTRMS/testlink-code",
"blobs": [],
"oldblobs": [],
"pathnames" : [ "lib/requirements/re qCompareVersions.php" ],
"published" : "2020-03-05T13:15:11.200",
"fixed"
'''

for l in f:
  # |[@afranz125](https://github.com/afranz125)|afranz1|Anna Franz|
  v = l.split('|')
  if (len(v) == 5 and v[2] != "netid" and v[2] !=  "------" and v[2] != "audris" and v[2] != "bklein3" and v[2] != "tvillarr"):
    u = db[v[2]]
    nu = 0
    nfull = 0
    for x in u.find( {} ):
      nu+=1
      fs = 0
      for f in ('id', "commit", "inWoC" ,"blobs", "oldblobs", "project","pathnames" ,"published", "fixed"):
        if f in x: fs+= 1
      if fs == 9: nfull += 1
    if (nu ==0):
      print ("|" + v[2]+" | nothing|")
    else:
      sys.stdout.write("|"+v[2]+ "|" + str(nu) + " records "+ str(nfull) + " complete|\n")




