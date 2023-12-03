# MP4

Try to reproduce a fix to a bug or to a vulnerability using [UT Verse (chatGPT)](https://utverse.utk.edu/)

Step 1: select your assigned language below *** Not the same as in
[MP2](https://github.com/fdac23/MiniProject2/) ***

Step 2: Select four PRs for your assigned language (you can use the steps below
or utilize datasetses collected by others in MP2). Preferably try to
get PRs that modify only one source code file.

Step 3: Select four vulnerabilities from your collection in MP3
As with bug fixes preferably try to
get PRs that modify only one source code file.

Step 4: List all eight fixed in the file yournetid.md in the fork
of this repo and submit a PR by Oct 31

Step 5: for each of eight fixes ask UT Verse to fix it
"please fix ``quote the commit comment of the fix`` the following
code

``include pre-fix file or function (or block where fix was done)``

Step 6: Obtain answers and populate MongoDB fdac23mp4 collection
yournetid with the required felds (see example Answer below).


## Example

### MP2 help for rare languages


```
find references to bug fixes in haskell code
UT Verse AI8:13 AM
```

Based on my training data up to Saturday, January 1, 2022, there are several resources that could help you find references to bug fixes in Haskell code. One option is the GitHub issues dataset, which includes bug reports (among other issue types) from a wide range of open-source projects hosted on GitHub. Another possibility is the Haskell Package Database (Hackage), which has a collection of packages and their documentation for the Haskell programming language.

To search for references to bug fixes specifically, you may want to try using keywords such as "bug", "fix", "issue", or "patch" in your search queries. Additionally, looking through the commit history of popular Haskell projects on GitHub may also provide insights into how bugs were fixed in those projects.

I hope this information helps! Let me know if you have any further
questions or if there's anything else I can assist you with.


## Steps

1. Looked for fix on hackage (sorted in descending order by rating),
top package was clock, the source code had
[44 closed PRs](https://github.com/corsis/clock/pulls?q=is%3Apr+is%3Aclosed)
selected [PR 89: Fix RealFrac Seconds instance](https://github.com/corsis/clock/pull/89/files) 


### question to  UT Verse (chatGPT)

```
Fix RealFrac Seconds instance in the following code
```

```
instance RealFrac Seconds where
  properFraction (Seconds (TimeSpec s ns))
    | s >= 0 = (fromIntegral s, Seconds $ TimeSpec 0 ns)
    | otherwise = (fromIntegral (s+1), Seconds $ TimeSpec (-1) ns)
```

### Response

To fix the RealFrac Seconds instance in the provided Haskell code, you can modify the properFraction function as follows:
```
instance RealFrac Seconds where
  properFraction (Seconds (TimeSpec s ns))
    | s >= 0 || ns == 0 = (fromIntegral s, Seconds $ TimeSpec 0 ns)
    | otherwise = let (negS, negNs) = normalize $! TimeSpec (-s) (s2ns - ns)
                  in (- fromIntegral negS, Seconds $ normalize $! TimeSpec 0 negNs)
```
This modified implementation handles negative values correctly by using the normalize function to ensure that the nanoseconds component is always positive. It also uses pattern matching and let bindings to simplify the code.

I hope this helps you with your Haskell programming. Let me know if you have any further questions or if there's anything else I can assist you with.

The actual fix was just one line:
```
s >= 0 || ns == 0 = (fromIntegral s, Seconds $ TimeSpec 0 ns)
```

## Answer

Database: fdac23mp4, collection your NetID

```
language: haskell
PR: https://github.com/corsis/clock/pull/89/files
Code before: https://raw.githubusercontent.com/amesgen/clock/2ab5496a04df1d9605c46e8b17261d5c2e7890f2/System/Clock/Seconds.hs
Code after: https://raw.githubusercontent.com/amesgen/clock/f588bcb0e04063abdb67eb489d229e1a5fd2a497/System/Clock/Seconds.hs
gptIn: see above
gptOut: see above
lineFix: true
moreChanges: true
```
|id|language|
|-|-|
|afranz1|Erlang|
|afriend3|PHP|
|agreer26|Fortran|
|alay10|Java|
|amistry2|Swift|
|andlrutt|Jupyter notebook|
|asharm42|Python|
|audris|JavaScript|
|ayu5|C#|
|azeng2|Haskel|
|bhaynie|Lisp|
|bmarth|Cobol|
|bnd674|Shell|
|cfishe36|Julia|
|cgraha37|VisualBasic|
|cheadri6|Sql|
|cshubert|Go|
|dwoun|Ada|
|ebriggs4|Ruby|
|echavez2|Assembly|
|ely1|Lua|
|emoran11|Dart|
|evaugha3|Scala|
|fhill5|Perl|
|gbb823|Rust|
|gjur1|TypeScript|
|hcurl|R|
|hdehler|C/C++|
|hli102|Erlang|
|hnguye48|PHP|
|ipelton|Fortran|
|jarmiger|Java|
|jblackab|Swift|
|jbower31|Jupyter notebook|
|jbrouss2|Python|
|jchen125|JavaScript|
|jhalloy|C#|
|jhawki41|Haskel|
|jhulen|Lisp|
|jkim172|pascal|
|jking148|Cobol|
|jmcelr10|Shell|
|jmckni13|Julia|
|jrich19|VisualBasic|
|jshoffn3|Sql|
|jskeen6|Go|
|jskupien|Ada|
|jsteed|Ruby|
|kchrist|Assembly|
|kcraddoc|Lua|
|knuchol1|Dart|
|kpatel68|Scala|
|kzeligow|Perl|
|lbower10|Rust|
|lliu58|TypeScript|
|loneal7|R|
|lsmit248|C/C++|
|lswann|Erlang|
|mpatel65|PHP|
|mstott3|Fortran|
|mtiwari|Java|
|mwang43|Swift|
|naskew|Jupyter notebook|
|nshoap|Python|
|oselyuti|JavaScript|
|pgajjala|C#|
|rcarnes|Haskel|
|rgarg4|Lisp|
|rlau|pascal|
|rrosenb4|Cobol|
|san5|Shell|
|shuang24|Julia|
|sjeroute|VisualBasic|
|skerzel|Sql|
|slaughl2|Go|
|smalluri|Ada|
|smistry1|Ruby|
|sshiran1|Assembly|
|tpanumat|Lua|
|ttahmid|Dart|
|twu21|Perl|
|vpk542|Rust|
|wcuny|TypeScript|
|wfortner|R|
|wouyang2|C/C++|
|wquesinb|Erlang|
|xzl263|PHP|
|zmille10|Fortran|
|zperry4|Java|
