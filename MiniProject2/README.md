# Data Discovery Project: find software bug datasets


1. Your topic is software bug fix datasets that are for the specific language
   that you are assigned, see below. 
2. Submit 20 queries to find datasets that are related to that topic.
3. Compare results from the following search engines (you can use additional ones if you like)
   a) [google] google.com
   b) [scholar] scholar.google.com
   d) [gdata] https://toolbox.google.com/datasetsearch
   e) [GPT] chatGPT
   f) [github] github.com
   

3. For each of the 20 datasets you chose, determine if the underlying data can be accessed (some of these datasets do not provide public access)
4. Create a mongodb collection named YourNetId within the database fdac23mp2
   where you store metadata for each of the 20 datasets:
   - YourTopic,
   - dataset title,
   - dataset license,
   - dataset description,
   - url(s) were the data may be retrieved
   - search engine (see above or another)
   - search string/prompt used
```
import pymongo, json
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac23mp2']
coll = db ['YourNetId']
# for each dataset
coll.insert_one ( { 'owner':'YourNetID', 'topic':'YourTopic', 'title': 'Data title', 'license': 'license', 'description': 'Brief data description', 'engine': "Search Engine', 'query': 'search query', 'url': [ 'url1', 'url2', ... ] } )
```


To check what is recorded:
```
import pprint
import pymongo, json
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac23mp2']
coll = db ['YourNetId']
pp = pprint.PrettyPrinter(indent=1,width=65)
for r in coll. find({'owner':'YourNetID'}):
  print(pp .pformat (r))  
```

# Language assignments

[See common file extensions for each language](https://github.com/fdac23/MiniProject2/blob/master/LN.md)

|id|language|
|-|-|
|afranz1|JavaScript|
|afriend3|TypeScript|
|agreer26|Python|
|alay10|Jupyter notebook|
|amistry2|C/C++|
|andlrutt|Java|
|asharm42|C#|
|audris|PHP|
|ayu5|Ruby|
|azeng2|Go|
|bhaynie|Rust|
|bklein3|R|
|bmarth|Swift|
|bnd674|Scala|
|cfishe36|Perl|
|cgraha37|Fortran|
|cheadri6|Ada|
|cshubert|Erlang|
|dwoun|Lua|
|ebriggs4|Sql|
|echavez2|Lisp|
|ely1|Julia|
|emoran11|Cobol|
|evaugha3|Shell|
|fhill5|pascal|
|gbb823|Haskel|
|gjur1|VisualBasic|
|hcurl|Assembly|
|hdehler|Dart|
|hli102|JavaScript|
|hnguye48|TypeScript|
|ipelton|Python|
|jarmiger|Jupyter notebook|
|jblackab|C/C++|
|jbower31|Java|
|jbrouss2|C#|
|jchen125|PHP|
|jhalloy|Ruby|
|jhawki41|Go|
|jhulen|Rust|
|jkim172|R|
|jking148|Swift|
|jmcelr10|Scala|
|jmckni13|Perl|
|jrich19|Fortran|
|jshoffn3|Ada|
|jskeen6|Erlang|
|jskupien|Lua|
|jsteed|Sql|
|kchrist|Lisp|
|kcraddoc|Julia|
|knuchol1|Cobol|
|kpatel68|Shell|
|kzeligow|pascal|
|lbower10|Haskel|
|lliu58|VisualBasic|
|loneal7|Assembly|
|lsmit248|Dart|
|lswann|JavaScript|
|mpatel65|TypeScript|
|mstott3|Python|
|mtiwari|Jupyter notebook|
|mwang43|C/C++|
|naskew|Java|
|nshoap|C#|
|oselyuti|PHP|
|pgajjala|Ruby|
|rcarnes|Go|
|rgarg4|Rust|
|rlau|R|
|rrosenb4|Swift|
|san5|Scala|
|shuang24|Perl|
|sjeroute|Fortran|
|skerzel|Ada|
|slaughl2|Erlang|
|smalluri|Lua|
|smistry1|Sql|
|sshiran1|Lisp|
|tpanumat|Julia|
|ttahmid|Cobol|
|tvillarr|Shell|
|twu21|pascal|
|vpk542|Haskel|
|wcuny|VisualBasic|
|wfortner|Assembly|
|wouyang2|Dart|
|wquesinb|JavaScript|
|xzl263|TypeScript|
|zmille10|Python|
|zperry4|Jupyter notebook|
