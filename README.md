# TeBaC-NET 
Text Based Custom Named Entity Tagger
Written in Python3.6

# How to Use

## Starting TeBaC-NET
Run TeBaC-NET.py in the command line with the python command - you will be presented with the main menu as follows:

```$ python TeBaC-NET.p

Welcome to Text Based Custom Named Entity Tagger (TeBaC-NET) v0.1

Main Menu
=========
1) Setup Session
2) Begin Tagging
3) Save/Load Custom Entity List
4) About TeBaC-NET
5) Quit

>> _
```

## Setup Tagging Session
TeBaC-NET does not carry forward its state from one session to another (yet). When beginning a new session, you will need to provide: 
* Input File Path
* Input File Offset
* Output File Path

To provide this values, press `1`, followed by `Enter/Return` at the main menu screen. Follow the instructions to provide the values: 

```
Setting up TeBaC-NET Session
Data File Path: /home/demo/dataFile
Data File Offset(default = 0): 0
Output File Path(default = /home/demo/dataFile.out): /home/demo/customOutputfilePath
```

After providing these values, you will be returned to the main menu with the session details shown just above the prompt.

```
Welcome to Text Based Custom Named Entity Tagger (TeBaC-NET) v0.1

Main Menu
=========
1) Setup Session
2) Begin Tagging
3) Save/Load Custom Entity List
4) About TeBaC-NET
5) Quit

Input: /home/demo/dataFile (offset:0)
Output: /home/demo/customOutputfilePath
>>
```

If you wish to change these values, simply follow the steps in this section again.

## Custom Named Entity Tagging
Once you have set up the session's input and output files, you can begin tagging by pressing `2`, followed by `Enter/Return` at the main menu screen.

You will see something similar to the following: 

```
    Line 1


    Singapore is much more than Gardens by the Bay and Sentosa. If you are coming to Singapore, don't forget to try the
    local food!

    Entities: No entities saved

    New Entity >>
```

To tag a custom named entity, simply type the word(s) that appear in the sentence. You will then be asked to specify the custom type for it: 

```
New Entity >> Gardens by the Bay
Entity Type>> attraction
```

All occurrences of the word(s) will be tagged with the same custom type.

# Blog Post
https://luppeng.wordpress.com/2018/05/29/text-based-named-entity-tagger-tebac-net/
