# Data Analysis Project


Your assigned language for MP5 is not the same as in
[MP2](https://github.com/fdac23/MiniProject2/) or [MP4](https://github.com/fdac23/MiniProject4/)!


For this assignment please create a Jupyter notebook named YourNetId.ipynb with answers to the following questions (tasks).
Each question has to be preceded by the text cell containing '# TN' where N is the task number, i.e., 1-7 

Part I Summarize results from MP2

   - T1: Does the programming language affect the number of distinct
   bug datsets found in 445/545 (use all collections in MP2)? 
   - T2: Does programming language affect which search engines will have more
   datasets (use all collections in MP2)?
   - T3: Produce a complete compilation of the bug datasets collected
   by everyone in MP2 for your assigned language in fdac23mp52
   collection YourNetId. (For your convenience, file LN2.md here
   provides the map between user id and language in MP2. Please use all
   collections corresponding to your MP5 language)

```
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac23mp52']
coll = db ['YourNetId']
```
   - T4: What are the most frequent licenses for the the datasets in your
   assigned language? 

Part II Summarize results from MP3
   - T5: How many CVEs are listed in all collections, how many have
   associated commits, and how many of these commits are in WoC (use all collections in MP3)?
   - T6: Does the number of CVEs with commits go up or down over time?
   What about the fraction of commits in WoC (use all collections in MP3)?


Part III Summarize results from MP4 for your assigned language (For your convenience, file LN4.md here
   provides the map between user id and language in MP4. Please use all
   collections corresponding to your MP5 language) 
   - T7: How many PRs did you count? How many had lineFix: true, how
   many had moreChanges: true?

|ID|Language|
|-|-|
|afranz1|Haskel|
|afriend3|Rust|
|agreer26|PHP|
|alay10|C/C++|
|amistry2|Perl|
|andlrutt|Swift|
|asharm42|Ruby|
|ayu5|C#|
|azeng2|JavaScript|
|bhaynie|Go|
|bmarth|Dart|
|bnd674|Julia|
|cfishe36|Cobol|
|cgraha37|Scala|
|cheadri6|Jupyter notebook|
|cshubert|Fortran|
|dwoun|pascal|
|ebriggs4|Lisp|
|echavez2|Ada|
|ely1|Lua|
|emoran11|VisualBasic|
|evaugha3|Python|
|fhill5|Sql|
|gbb823|Assembly|
|gjur1|R|
|hcurl|Shell|
|hdehler|Java|
|hli102|Haskel|
|hnguye48|Rust|
|ipelton|PHP|
|jarmiger|C/C++|
|jblackab|Perl|
|jbower31|Swift|
|jbrouss2|Ruby|
|jchen125|Erlang|
|jhalloy|C#|
|jhawki41|JavaScript|
|jhulen|Go|
|jkim172|TypeScript|
|jking148|Dart|
|jmcelr10|Julia|
|jmckni13|Cobol|
|jrich19|Scala|
|jshoffn3|Jupyter notebook|
|jskeen6|Fortran|
|jskupien|pascal|
|jsteed|Lisp|
|kchrist|Ada|
|kcraddoc|Lua|
|knuchol1|VisualBasic|
|kpatel68|Python|
|kzeligow|Sql|
|lbower10|Assembly|
|lliu58|R|
|loneal7|Shell|
|lsmit248|Java|
|lswann|Haskel|
|mpatel65|Rust|
|mstott3|PHP|
|mtiwari|C/C++|
|mwang43|Perl|
|naskew|Swift|
|nshoap|Ruby|
|oselyuti|Erlang|
|pgajjala|C#|
|rcarnes|JavaScript|
|rgarg4|Go|
|rlau|TypeScript|
|rrosenb4|Dart|
|san5|Julia|
|shuang24|Cobol|
|sjeroute|Scala|
|skerzel|Jupyter notebook|
|slaughl2|Fortran|
|smalluri|pascal|
|smistry1|Lisp|
|sshiran1|Ada|
|tpanumat|Lua|
|ttahmid|VisualBasic|
|twu21|Sql|
|vpk542|Assembly|
|wcuny|R|
|wfortner|Shell|
|wouyang2|Java|
|wquesinb|Haskel|
|xzl263|Rust|
|zmille10|PHP|
|zperry4|C/C++|
