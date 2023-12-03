#To create an txt with all vulnerabilities, use this cmd
#curl "https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2018-05-03T09:29:00.000	&pubEndDate=2018-05-17T09:29:00.000" | jq .

import json
import os
import pymongo
import pprint


def findElementIndex(stdout, badChar, end):
    while(stdout[end] != badChar):
        end += 1
    return end
    
    

#Curl command to get all vulnerabilities for the assigned period 
cmd = "curl 'https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2018-05-03T09:29:00.000&pubEndDate=2018-05-17T09:29:00.000'"
data = json.loads(os.popen(cmd).read())
vulnerabilities = data.get("vulnerabilities", [])

#Search vulnerabilities with a commit or pull request for a public repo
#A commit in git always has a hash that contains 40 characters (https://support.configura.com/hc/en-us/articles/360052644053-Are-Git-Commit-id-s-Truncated-in-CET-Developer-#:~:text=A%20commit%20in%20git%20always,commit%20within%20the%20same%20repo.)
patchList = []
for vulnerability in vulnerabilities:
    for reference in vulnerability["cve"]["references"]:
        if "tags" in reference and "Patch" in reference["tags"]:
            url = reference["url"]
            commitHash = url[-40:]
            cveId = vulnerability["cve"]["id"]
            cvePublished = vulnerability["cve"]["published"]

            #Need to make sure that the patch is actually a commit
            if ';' not in commitHash and '/' not in commitHash and '-' not in commitHash and '_' not in commitHash:
                patchList.append([])
                patchList[len(patchList)-1].append(cveId)
                patchList[len(patchList)-1].append(commitHash)
                patchList[len(patchList)-1].append(0)
                patchList[len(patchList)-1].append([])
                patchList[len(patchList)-1].append([])
                patchList[len(patchList)-1].append(url)
                patchList[len(patchList)-1].append([])
                patchList[len(patchList)-1].append(cvePublished)
                patchList[len(patchList)-1].append(0)

    
#Curl commands for WoC
woc1 = "curl 'https://worldofcode.org/api/lookup?command=showCnt&sha1={}&type=commit'"
woc2 = "curl 'https://worldofcode.org/api/lookup?command=getValues&sha1={}&type=c2fbb'"
                
#WoC #1 - Find commits in World of Code
for patch in patchList:
    commit = woc1.format(patch[1])
    data = json.loads(os.popen(commit).read())
    stdout = data.get("stdout", [])
    
    if len(stdout) != 0:
        patch[2] = 1 #It is in WoC
        #Extract the fixed time from stdout
        i = len(stdout)-1
        while(stdout[i] != ';'):
            i-=1
        patch[8] = stdout[i+1:len(stdout)-1]
    else:
        patch[2] = 0
        patch[8] = -1
        
        
        
#WoC #2 - List all blobs and file created by commit
for patch in patchList:
    commit = woc2.format(patch[1])
    data = json.loads(os.popen(commit).read())
    stdout = data.get("stdout", [])
    
    if patch[2] == 1 and len(stdout) != 0:
        #Calculate which index the file name in stdout starts at 
        begin = findElementIndex(stdout, ';', 0) + 1
        end = begin + 1
        
        while(stdout[end-1] != '\n'):
            #Record file name
            end = findElementIndex(stdout, ';', end)
            patch[6].append(stdout[begin:end])
            
            #Record new blob
            begin = end + 1
            end = findElementIndex(stdout, ';', end + 1)
            patch[3].append(stdout[begin:end+1])
            
            #Record old blob
            begin = end + 1
            end += 1
            while stdout[end] != ';' and stdout[end] != '\n':
                end += 1
            if stdout[end] == '\n':
                patch[4].append(stdout[begin:end])
            else:
                patch[4].append(stdout[begin:end+1])
            begin = end + 1
            end += 1  
    else:
        #No blobs (either no output OR not in WoC)
        patch[3].append("NA")
        patch[4].append("NA")
        patch[6] = "NA"


#Create mongodb collection
client = pymongo.MongoClient(host="da1.eecs.utk.edu")
db = client['fdac23mp3'];
coll = db['shuang24'];
coll.drop() #Deletes the pre-existing one to avoid making duplicates

for patch in patchList:    
    entry = {};
    entry["id"] = patch[0]
    entry["commit"] = patch[1]
    entry["inWoC"] = patch[2]
    entry["blobs"] = patch[3]
    entry["project"] = patch[5]
    entry["pathnames"] = patch[6]
    entry["published"] = patch[7]
    entry["fixed"] = patch[8]
    coll.insert_one(entry)
    
for x in coll.find():
    print(x)
    print("\n")