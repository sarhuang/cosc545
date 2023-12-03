# Collecting CVE Fixes

The National Vulnerability Database (NVD) at https://nvd.nist.gov/
has information about vulnerabilities.

This information can be retrieved via wen APIs.
The web API documentation is: https://nvd.nist.gov/developers/vulnerabilities

Here's a simple example that uses the web API to find all vulnerabilities published between Jan 1 and Jan 15 of 2021:
```
curl "https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2021-01-01T00:00:00.000&pubEndDate=2021-01-15T00:00:00.000"
```
piping through jq makes it more readable:
```
curl "https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2021-01-16T00:00:00.000&pubEndDate=2021-01-31T00:00:00.000" | jq .
```
Searching for a "tags" value of "Patch" finds patches. For open
source projects, "Patch" is often the fixing commits. For
proprietary code, there is often no "Patch" or it is just a web page
that explains the issue.
We will only look at open source projects.

Here's an example entry for CVE-2021-25323 based on the Jan1 - Jan 15 2021 data:
```
        "cve": {
        "id": "CVE-2021-25323",
        "sourceIdentifier": "cve@mitre.org",
        "published": "2021-01-19T16:15:13.327",
        "lastModified": "2021-01-22T15:40:54.153",
        "vulnStatus": "Analyzed",
        "descriptions": [

         ..... bunch of stuff deleted to keep it short....


           "references": [
             {
               "url": "https://github.com/MISP/MISP/commit/afbf95a478b6e94f532ca0776c79da1b08be7eed",
               "source": "cve@mitre.org",
               "tags": [
                 "Patch",
                 "Third Party Advisory"
               ]
             }
           ]
```
Based on this information, the commit that fixes the vulnerability
             for CVE-2021-25323 is probably
             afbf95a478b6e94f532ca0776c79da1b08be7eed. That needs to
be verified by reading the NVD entry for that CVE.


### You are each are assigned a specific period, for example

|id|from|to|
|-|-|-|
|audris|2023-10-01T00:00:00.000|2023-10-12T00:00:00.000|

Translates into 
"https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=2023-10-01T00:00:00.000&pubEndDate=2023-10-12T00:00:00.000"
etc.


## Your task is

1. Write a python script that retrieves all vulnerabilities for the assigned period
2. Identify in pick out the ones that have a patch that is a commit
or pull request for a public repo
3. Find the project based on the url.
4. Determine if commit is in WoC
```
curl "https://worldofcode.org/api/lookup?command=showCnt&sha1=afbf95a478b6e94f532ca0776c79da1b08be7eed&type=commit"
output format:
commit;tree;parent commit(s);author;committer;author time;committer time
{"stdout":"afbf95a478b6e94f532ca0776c79da1b08be7eed;69037a92030ea284080a6fe766bd077811c70d4a;95ba8d0fd8a8b549b58ab34e7fff1770f0d89057;iglocska <andras.iklody@gmail.com>;iglocska <andras.iklody@gmail.com>;1611061296;1611061296\n","stderr":""}
```

5. in WoC list all blobs and file created by the commit (for
```
curl "https://worldofcode.org/api/lookup?command=getValues&sha1=afbf95a478b6e94f532ca0776c79da1b08be7eed&type=c2fbb"
output format:
commit;file1;new blob1;old blob1;...
{"stdout":"afbf95a478b6e94f532ca0776c79da1b08be7eed;app/Config/config.default.php;ab368842749ebf766586b6405f4a84906dac962c;c1f944dba78985030771b8b5c6d8c85b90cf754f\n","stderr":""}
```

6. List all files modified by the commit (see above)


7. If you need to get the content of the blob (e.g., for MP4)
```
curl "https://worldofcode.org/api/lookup?command=showCnt&sha1=c1f944dba78985030771b8b5c6d8c85b90cf754f&type=blob"
output format:
commit;file1;new blob1;old blob1;...
{"stdout":"<?php\n$config = array(\n\t'debug'            => 0,\n\t
....
in to update user fields (e.g. role)\n\t\t),\n\t*/\n);\n\n","stderr":""}
```



Output:
```
Create a mongodb collection named YourNetId within the database
fdac23mp3 with schema: (key=description)
id=CVE id
commit=commit hash for the fixing commit
inWoC=is commit in WoC (0|1)
blobs=[blobs created by the commit: see c2fbb output]
oldblobs=[blobs modified by the commit: see c2fbb output]
project=project URL
pathnames=[pathname(s) of the vulnerable file(s): see c2fbb output]
published=date the CVE entry was published
fixed=date of the fix (see commit output)
```

As an example, for CVE-2021-25323 used in the example above, the information would be:
```
id:"CVE-2021-25323",
commits:"afbf95a478b6e94f532ca0776c79da1b08be7eed",
inWoC:1,
blobs: [ ab368842749ebf766586b6405f4a84906dac962c  ],
oldblobs: [ c1f944dba78985030771b8b5c6d8c85b90cf754  ],
project:"https://github.com/MISP/MISP",
pathnames:"app/Config/config.default.php",
published:"2021-01-19 14:01:36+01:00",
fixed:1611061296
```

|id|from|to|
|-|-|-|
|afranz1|2023-09-14T09:29:00.000|2023-09-28T09:29:00.000|
|afriend3|2023-08-17T09:29:00.000|2023-08-31T09:29:00.000|
|agreer26|2023-07-20T09:29:00.000|2023-08-03T09:29:00.000|
|alay10|2023-06-22T09:29:00.000|2023-07-06T09:29:00.000|
|amistry2|2023-05-25T09:29:00.000|2023-06-08T09:29:00.000|
|andlrutt|2023-04-27T09:29:00.000|2023-05-11T09:29:00.000|
|asharm42|2023-03-30T09:29:00.000|2023-04-13T09:29:00.000|
|ayu5|2023-03-02T08:29:00.000|2023-03-16T09:29:00.000|
|azeng2|2023-02-02T08:29:00.000|2023-02-16T08:29:00.000|
|bhaynie|2023-01-05T08:29:00.000|2023-01-19T08:29:00.000|
|bmarth|2022-12-08T08:29:00.000|2022-12-22T08:29:00.000|
|bnd674|2022-11-10T08:29:00.000|2022-11-24T08:29:00.000|
|cfishe36|2022-10-13T09:29:00.000|2022-10-27T09:29:00.000|
|cgraha37|2022-09-15T09:29:00.000|2022-09-29T09:29:00.000|
|cheadri6|2022-08-18T09:29:00.000|2022-09-01T09:29:00.000|
|cshubert|2022-07-21T09:29:00.000|2022-08-04T09:29:00.000|
|dwoun|2022-06-23T09:29:00.000|2022-07-07T09:29:00.000|
|ebriggs4|2022-05-26T09:29:00.000|2022-06-09T09:29:00.000|
|echavez2|2022-04-28T09:29:00.000|2022-05-12T09:29:00.000|
|ely1|2022-03-31T09:29:00.000|2022-04-14T09:29:00.000|
|emoran11|2022-03-03T08:29:00.000|2022-03-17T09:29:00.000|
|evaugha3|2022-02-03T08:29:00.000|2022-02-17T08:29:00.000|
|fhill5|2022-01-06T08:29:00.000|2022-01-20T08:29:00.000|
|gbb823|2021-12-09T08:29:00.000|2021-12-23T08:29:00.000|
|gjur1|2021-11-11T08:29:00.000|2021-11-25T08:29:00.000|
|hcurl|2021-10-14T09:29:00.000|2021-10-28T09:29:00.000|
|hdehler|2021-09-16T09:29:00.000|2021-09-30T09:29:00.000|
|hli102|2021-08-19T09:29:00.000|2021-09-02T09:29:00.000|
|hnguye48|2021-07-22T09:29:00.000|2021-08-05T09:29:00.000|
|ipelton|2021-06-24T09:29:00.000|2021-07-08T09:29:00.000|
|jarmiger|2021-05-27T09:29:00.000|2021-06-10T09:29:00.000|
|jblackab|2021-04-29T09:29:00.000|2021-05-13T09:29:00.000|
|jbower31|2021-04-01T09:29:00.000|2021-04-15T09:29:00.000|
|jbrouss2|2021-03-04T08:29:00.000|2021-03-18T09:29:00.000|
|jchen125|2021-02-04T08:29:00.000|2021-02-18T08:29:00.000|
|jhalloy|2021-01-07T08:29:00.000|2021-01-21T08:29:00.000|
|jhawki41|2020-12-10T08:29:00.000|2020-12-24T08:29:00.000|
|jhulen|2020-11-12T08:29:00.000|2020-11-26T08:29:00.000|
|jkim172|2020-10-15T09:29:00.000|2020-10-29T09:29:00.000|
|jking148|2020-09-17T09:29:00.000|2020-10-01T09:29:00.000|
|jmcelr10|2020-08-20T09:29:00.000|2020-09-03T09:29:00.000|
|jmckni13|2020-07-23T09:29:00.000|2020-08-06T09:29:00.000|
|jrich19|2020-06-25T09:29:00.000|2020-07-09T09:29:00.000|
|jshoffn3|2020-05-28T09:29:00.000|2020-06-11T09:29:00.000|
|jskeen6|2020-04-30T09:29:00.000|2020-05-14T09:29:00.000|
|jskupien|2020-04-02T09:29:00.000|2020-04-16T09:29:00.000|
|jsteed|2020-03-05T08:29:00.000|2020-03-19T09:29:00.000|
|kchrist|2020-02-06T08:29:00.000|2020-02-20T08:29:00.000|
|kcraddoc|2020-01-09T08:29:00.000|2020-01-23T08:29:00.000|
|knuchol1|2019-12-12T08:29:00.000|2019-12-26T08:29:00.000|
|kpatel68|2019-11-14T08:29:00.000|2019-11-28T08:29:00.000|
|kzeligow|2019-10-17T09:29:00.000|2019-10-31T09:29:00.000|
|lbower10|2019-09-19T09:29:00.000|2019-10-03T09:29:00.000|
|lliu58|2019-08-22T09:29:00.000|2019-09-05T09:29:00.000|
|loneal7|2019-07-25T09:29:00.000|2019-08-08T09:29:00.000|
|lsmit248|2019-06-27T09:29:00.000|2019-07-11T09:29:00.000|
|lswann|2019-05-30T09:29:00.000|2019-06-13T09:29:00.000|
|mpatel65|2019-05-02T09:29:00.000|2019-05-16T09:29:00.000|
|mstott3|2019-04-04T09:29:00.000|2019-04-18T09:29:00.000|
|mtiwari|2019-03-07T08:29:00.000|2019-03-21T09:29:00.000|
|mwang43|2019-02-07T08:29:00.000|2019-02-21T08:29:00.000|
|naskew|2019-01-10T08:29:00.000|2019-01-24T08:29:00.000|
|nshoap|2018-12-13T08:29:00.000|2018-12-27T08:29:00.000|
|oselyuti|2018-11-15T08:29:00.000|2018-11-29T08:29:00.000|
|pgajjala|2018-10-18T09:29:00.000|2018-11-01T09:29:00.000|
|rcarnes|2018-09-20T09:29:00.000|2018-10-04T09:29:00.000|
|rgarg4|2018-08-23T09:29:00.000|2018-09-06T09:29:00.000|
|rlau|2018-07-26T09:29:00.000|2018-08-09T09:29:00.000|
|rrosenb4|2018-06-28T09:29:00.000|2018-07-12T09:29:00.000|
|san5|2018-05-31T09:29:00.000|2018-06-14T09:29:00.000|
|shuang24|2018-05-03T09:29:00.000|2018-05-17T09:29:00.000|
|sjeroute|2018-04-05T09:29:00.000|2018-04-19T09:29:00.000|
|skerzel|2018-03-08T08:29:00.000|2018-03-22T09:29:00.000|
|slaughl2|2018-02-08T08:29:00.000|2018-02-22T08:29:00.000|
|smalluri|2018-01-11T08:29:00.000|2018-01-25T08:29:00.000|
|smistry1|2017-12-14T08:29:00.000|2017-12-28T08:29:00.000|
|sshiran1|2017-11-16T08:29:00.000|2017-11-30T08:29:00.000|
|tpanumat|2017-10-19T09:29:00.000|2017-11-02T09:29:00.000|
|ttahmid|2017-09-21T09:29:00.000|2017-10-05T09:29:00.000|
|twu21|2017-08-24T09:29:00.000|2017-09-07T09:29:00.000|
|vpk542|2017-07-27T09:29:00.000|2017-08-10T09:29:00.000|
|wcuny|2017-06-29T09:29:00.000|2017-07-13T09:29:00.000|
|wfortner|2017-06-01T09:29:00.000|2017-06-15T09:29:00.000|
|wouyang2|2017-05-04T09:29:00.000|2017-05-18T09:29:00.000|
|wquesinb|2017-04-06T09:29:00.000|2017-04-20T09:29:00.000|
|xzl263|2017-03-09T08:29:00.000|2017-03-23T09:29:00.000|
|zmille10|2017-02-09T08:29:00.000|2017-02-23T08:29:00.000|
|zperry4|2017-01-12T08:29:00.000|2017-01-26T08:29:00.000|

