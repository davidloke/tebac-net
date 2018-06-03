# TeBaC-NET 
Text Based Custom Named Entity Tagger
Written in Python3.6

In v0.1, do note the following:

* Entities are case sensitive (e.g. singapore != Singapore)
* For now, all occurrences of the word(s) will be tagged with the same custom type (e.g. 'Singapore' in 'Singaporean' will also be tagged)
* All custom types will be capitalized for disambiguity (e.g. 'Capital' becomes 'CAPITAL')
* Each entity-tag pair is unique for every line

# Blog Post
https://luppeng.wordpress.com/2018/05/29/text-based-named-entity-tagger-tebac-net/

# How to Use
To begin, simple clone this repository onto your local machine. 

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
>> _
```

If you wish to change these values, simply follow the steps in this section again.


## Custom Named Entity Tagging
### Defining and Tagging Custom Named Entities 
Once you have set up the session's input and output files, you can begin tagging by pressing `2`, followed by `Enter/Return` at the main menu screen.

The first line (with offset) to be tagged will appear in the subsequent screen. It will look something like this: 

```
    Line 1


    Singapore is much more than Gardens by the Bay and Sentosa. If you are coming to Singapore, don't forget to try the
    local food - just ask any Singaporean where is the nearest hawker center!

    Entities: No entities saved

    New Entity >> _
```

To tag a custom named entity, simply type the word(s) that appear in the sentence. You will then be asked to specify the custom type for it: 

```
New Entity >> Gardens by the Bay
Entity Type>> attraction
```
Your tagged entities, together with its starting and ending indexes, will appear below the line in the input file:
```
    Line 1

    Singapore is much more than Gardens by the Bay and Sentosa. If you are coming to Singapore, don't forget to try the
    local food - just ask any Singaporean where is the nearest hawker center!

    Entities: (28, 46, 'ATTRACTION')

    Added 1 counts of 'Gardens by the Bay' successfully

    New Entity >> _
```

All occurrences of the words (even substrings) will be tagged with the same custom type. For example, if we add 'Singapore' as the 'CAPITAL':

``` 
    Line 1


    Singapore is much more than Gardens by the Bay and Sentosa. If you are coming to Singapore, don't forget to try the
    local food - just ask any Singaporean where is the nearest hawker center!

    Entities: (28, 46, 'ATTRACTION'), (51, 58, 'ATTRACTION'), (0, 9, 'CAPITAL'), (81, 90, 'CAPITAL'),
              (142, 151, 'CAPITAL')

    Added 3 counts of 'Singapore' successfully

    New Entity >> _
```
You can remove unwanted tags - please refer to the corresponding section below. 

Once you are satisified with your named entities, use the `:nn` command to go to save the current line and move on to the next. If the next line contains occurrences of previous custom entities, they will be automatically tagged as well. 

If there are no more lines to be tagged (i.e. end of file), you will be presented with the main menu.


### Toggling Detailed View
To make it more intuitive, you can use `:aa` command to toggle between showing/hiding the tagged entity string.  

For example, after typing `:aa` and pressing enter, the list of custom entities will be similar to the following:

```
    Line 1


    Singapore is much more than Gardens by the Bay and Sentosa. If you are coming to Singapore, don't forget to try the local food - just ask any Singaporean where is
    the nearest hawker center!

    Entities: Gardens by the Bay->(28, 46, 'ATTRACTION'), Sentosa->(51, 58, 'ATTRACTION'), Singapore->(0, 9, 'CAPITAL'), Singapore->(81, 90, 'CAPITAL'),
              Singapore->(142, 151, 'CAPITAL')

    Toggle detailed entity list

    New Entity >> _
```


### Removing Tags
It is possible to remove entities from the list. In the example above, we notice that 'Singapore' in 'Singaporean' is tagged as well. This may not be an ideal case - let's remove it.

To remove an entity from the list, use the `:dd` command. You will then be prompted to enter the 0-based index of the entity list that you wish to remove. 

```
    New Entity >> :dd
    Entity Index to Remove (0-based index) >> 4
```

If removal is successful, the entity list will reflect the change:
```
    Line 1


    Singapore is much more than Gardens by the Bay and Sentosa. If you are coming to Singapore, don't forget to try the local food - just ask any Singaporean where is
    the nearest hawker center!

    Entities: Gardens by the Bay->(28, 46, 'ATTRACTION'), Sentosa->(51, 58, 'ATTRACTION'), Singapore->(0, 9, 'CAPITAL'), Singapore->(81, 90, 'CAPITAL')

    Removed index 4

    New Entity >> _
```

### End Tagging 
If you wish to stop tagging, you can use the `:qq` command to save your current progress into the output file. You will then be presented the main menu again. 

Do remember the line number at the top of the tagging screen - this is the offset of the input file should you wish to continue in another session.


## Save/Load Custom Entity List
If you wish to save your custom entity list (with its corresponding tags), press `3`, followed by `Enter/Return` in the main menu. You will be presented with the following submenu
```
Manage Entity List

 1) Load Entity List
 2) Save Entity List
 3) Print Current Entity List
 4) Clear Current Entity List
 5) Back

```

If you choose to Load/Save your entity list, you will need to provide the file path. Currently, saving to a file overwrites it completely. 


## More About TeBaC-NET
To find out more about TeBaC-NET, press `4`, followed by `Enter/Return` in the main menu. 


## Quitting TeBaC-NET
To quit TeBaC-NET, press `5`, followed by `Enter/Return` in the main menu. 


## Contact
If you have any questions, feature requests, credits, please feel free to reach out to me either via my TeBaC-NET blog post, linkedin, or here on GitHub.

Thank you - hope you find TeBaC-NET useful! :)
