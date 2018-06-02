import os 
import platform

def printWelcomeMessage(newLine):
  print(newLine,newLine,'Welcome to Text Based Custom Named Entity Tagger (TeBaC-NET) v0.1',sep='')

def clearScreenCmd(): 
  if (platform.system() == 'Windows'):
    os.system('cls')
  else: 
    os.system('clear')

def printMainMenu(newLine):
  print(newLine,'Main Menu',newLine,'=========',newLine,'1) Setup Session',newLine,'2) Begin Tagging',newLine,'3) Save/Load Custom Entity List',newLine,'4) About TeBaC-NET',newLine,'5) Quit',newLine, sep='')

def printAcceptInput(newLine):
  return input(">> ")

def processUserChoice(userChoice):
  print ('you selected', userChoice)

def findAllEntities(searchTerm, inputString, entityTag): 

  if len(searchTerm) < 1 or len(inputString) < 1 or len(entityTag) < 1:
    return []
    
  workingString = inputString
  entityList = []
  startIndex = 0 
  findResult = workingString.find(searchTerm, startIndex, len(inputString))
  while findResult != -1: 
    entityList.append((findResult, findResult + len(searchTerm), entityTag.upper()))
    startIndex = findResult + len(searchTerm)
    findResult = workingString.find(searchTerm, startIndex, len(inputString))
  
  return entityList


def setupSession(newLine):
  print (newLine + 'Setting up TeBaC-NET Session')
  rawInputFile = input('Data File Path: ')
  if rawInputFile == '': 
    rawInputFile = None
    return None, None, None
    
  rawOffset = input('Data File Offset(default = 0): ')
  inputOffset = 0
  if rawOffset.isdigit() and int(rawOffset) > 0:
    inputOffset = int(rawOffset)
    
  rawOutputFile = input('Output File Path(default = ' + rawInputFile + '.out): ')
  if rawOutputFile == '': 
    rawOutputFile = rawInputFile + '.out'
  
  return rawInputFile, rawOutputFile, inputOffset

def quitApp(newLine): 
  print ('Thank you for using TeBaC-NET.')
  exit();
  
def printSimpleEntityList(entityList): 
  outputEntityString = ''
  entityListNewLinePadding = ' ' * 14
  entityDelimiter = ', '
  
  terminalLength = os.get_terminal_size()[0] - len(entityListNewLinePadding)
  if len(entityList) == 0: 
    outputEntityString = 'No entities saved'
    
  elif len(entityList) == 1: 
    outputEntityString = str(entityList[0])
    
  elif len(entityList) > 1:
    for e in entityList[:-1]:
      if (terminalLength - len(str(e))) > 0:
        outputEntityString = outputEntityString + str(e) + entityDelimiter
        terminalLength = terminalLength - len(str(e)) - 2
      else:
        outputEntityString = outputEntityString + "\n" + entityListNewLinePadding + str(e) + entityDelimiter
        terminalLength = os.get_terminal_size()[0] - len(entityListNewLinePadding) - len(str(e)) - len(entityDelimiter)
    else: 
      e = str(entityList[-1])
      if (terminalLength - len(e)) < 0:
        outputEntityString = outputEntityString + "\n" + entityListNewLinePadding
      outputEntityString += e
      
  return outputEntityString
  
def printDetailedEntityList(entityList, rawLine): 
  outputEntityString = ''
  entityListNewLinePadding = ' ' * 14
  entityDelimiter = ', '
  entityArrow = '->'
  
  terminalLength = os.get_terminal_size()[0] - len(entityListNewLinePadding)
  if len(entityList) == 0: 
    outputEntityString = 'No entities saved'
    
  elif len(entityList) == 1: 
    outputEntityString = rawLine[entityList[0][0]:entityList[0][1]] + entityArrow + str(entityList[0])
    
  elif len(entityList) > 1:
    for e in entityList[:-1]:
      detailedEntity = rawLine[e[0]:e[1]] + entityArrow + str(e)
      if (terminalLength - len(detailedEntity)) > 0:
        outputEntityString = outputEntityString + detailedEntity + entityDelimiter
        terminalLength = terminalLength - len(detailedEntity) - 2
      else:
        outputEntityString = outputEntityString + "\n" + entityListNewLinePadding + detailedEntity + entityDelimiter
        terminalLength = os.get_terminal_size()[0] - len(entityListNewLinePadding) - len(detailedEntity) - len(entityDelimiter)
    else: 
      e = entityList[-1]
      detailedEntity = rawLine[e[0]:e[1]] + entityArrow + str(e)
      if (terminalLength - len(detailedEntity)) < 0:
        outputEntityString = outputEntityString + "\n" + entityListNewLinePadding
      outputEntityString += detailedEntity
      
  return outputEntityString

  
def beginTagging(inputFile, inputFileOffset, outputFile, sessionEntityList):
  rawLineCounter = 0
  previousEntities = sessionEntityList
  showDetailed = False
  rawLineDisplayPadding = ' ' * 4

  with open(inputFile,"r") as dataFile, open(outputFile,"w") as taggedFile:
    for rawLine in dataFile:
      rawLineCounter += 1
      if rawLineCounter < inputFileOffset or "######" in rawLine:
        continue
      else:
        rawLine = rawLine.strip().split("|")[0] ##Special split for data file
        userInput = ""
        feedbackMessage = ""
        entities = []
        
        # Previous entities found
        if len(previousEntities) > 0:
          for prevEntity, prevEntityType in previousEntities:
            prevEntityTuples = findAllEntities(prevEntity, rawLine, prevEntityType)
            if len(prevEntityTuples) > 0:
              for singleTuple in prevEntityTuples:
                entities.append(singleTuple)
        
        rawLineTokens = rawLine.split(" ")
        
        while userInput != "nextline":
          clearScreenCmd()
          print("\n    Line " + str(rawLineCounter))
          print("\n" + rawLineDisplayPadding)
          
          formattedOutputLine = rawLineDisplayPadding
          terminalLength = os.get_terminal_size()[0] - len(rawLineDisplayPadding)
          
          for token in rawLineTokens:
            if (terminalLength - len(token) > 0): 
              formattedOutputLine = formattedOutputLine + token + " "
              terminalLength = terminalLength - len(token) - 1
            else: 
              formattedOutputLine = formattedOutputLine + "\n    " + token + " "
              terminalLength = os.get_terminal_size()[0] - len(rawLineDisplayPadding) - len(token) - 1
          
          print(formattedOutputLine)
            
          
          
          if showDetailed:
            outputEntityString = printDetailedEntityList(entities, rawLine)
            print("\n    Entities: {}".format(outputEntityString))
          else: 
            outputEntityString = printSimpleEntityList(entities)
            print("\n    Entities: {}".format(outputEntityString))
          
          if userInput == "help":
            print("\n    Special Commands are :dd, :nn, :qq")
          elif len(feedbackMessage) > 0:
            print("\n    " + feedbackMessage)
          
          userInput = input("\n    New Entity >> ")
          
          if userInput == ":nn":
            break
          
          elif userInput == ":qq":
            return 
          
          elif userInput == ":dd": 
            indexToRemove = input("    Entity Index to Remove (0-based index) >> ")
            if indexToRemove.isdigit() and len(entities) > 0 and int(indexToRemove) >= 0 and int(indexToRemove) < len(entities):
              entities.pop(int(indexToRemove))
              feedbackMessage = "Removed index " + indexToRemove
            elif indexToRemove == "all": 
              entities = []
            else: 
              feedbackMessage = "Removal attempt failed at index " + indexToRemove
          
          elif userInput == ":aa": 
            showDetailed = not showDetailed
            feedbackMessage = "Toggle detailed entity list"
          
          elif userInput in rawLine:
            userEntityType = input("    Entity Type>> ")
            newTuples = findAllEntities(userInput, rawLine, userEntityType.upper())
            
            if len(newTuples) > 0:
              for tuple in newTuples: 
                if tuple not in entities: 
                  entities.append(tuple)
                  feedbackMessage = "Added {} counts of '{}' successfully".format(len(newTuples), userInput)
                else: 
                  feedbackMessage = "Record '{}' already exists".format(userInput)
                  
                if (userInput, userEntityType.upper()) not in previousEntities:
                  previousEntities.append((userInput, userEntityType.upper()))
            
          else: 
            feedbackMessage = "Could not find entity '{}'".format(userInput)
          
        #print('writing to file')
        # when :nn is entered and break out of the while loop
        taggedFile.write(rawLine + "|" + str(entities) + "\n")
        continue
        
    return previousEntities
          
def manageSessionEntityList(sessionEntityList): 
  userAction = -1
  exitAction = '5'
  entityList = sessionEntityList
  feedbackMessage = ''
  while userAction != exitAction: 
    clearScreenCmd()
    print('\n\nManage Entity List\n\n 1) Load Entity List\n 2) Save Entity List\n 3) Print Current Entity List\n 4) Clear Current Entity List\n 5) Back\n')
    if len(feedbackMessage) > 0:
      print(feedbackMessage)
    userAction = input('\nSelection >>')
    if userAction.isdigit():
      if int(userAction) == 1:
        entityInputFile = input('Load from file (absolute path): ')
        with open(entityInputFile,"r") as inputFile: 
          for line in inputFile: # for each line in the input file 
            newTupleList = eval(line)
            for tuple in newTupleList: # for each tuple in the line
              if tuple not in entityList:
                entityList.append(tuple)
        feedbackMessage = 'Entities loaded successfully'
        
      elif int(userAction) == 2: 
        if len(sessionEntityList) <= 0:
          feedbackMessage = 'No entity to save'
        else: 
          entityOutputFile = input('Save to file (absolute path): ')
          with open(entityOutputFile,"w") as outputFile: 
            outputFile.write(str(entityList))
            feedbackMessage = 'Entities saved successfully!'
      elif int(userAction) == 3:
        feedbackMessage = 'Current Entity List: ' + str(entityList)
      elif int(userAction) == 4:
        if input('This step is irreversible. Are you sure? (yes/no) ').strip() in ['yes', 'Yes']:
          entityList = []
          feedbackMessage = 'Deleted all entities.'
        else:
          feedbackMessage = 'No changes made.'
      
    else: 
      feedbackMessage = "Invalid Choice"
        
  return entityList
        
  
  
def aboutTeBaCNET(newLine):
  clearScreenCmd()
  print("{0}    TeBaC-NET is a free Text Based Named Entity Tagger created by Lup Peng. {0}{0}    GitHub: {1}{0}{0}    Linkedin: {2}".format(newLine, "https://github.com/davidloke/tebac-net", "https://sg.linkedin.com/in/lup-peng-loke"))
  input("{0}    Press enter to continue...".format(newLine))

switchCase = { 1: setupSession,
               2: beginTagging,
               4: aboutTeBaCNET,
               5: quitApp
             }

newLine = "\n"
exitChoice = 5
userChoice = -1 
errorMessage = None
acceptableRange = list(range(1,exitChoice+1))
inputFile = None
outputFile = None
inputFileOffset = 0
sessionEntityList = []

while True:  
  clearScreenCmd()
  printWelcomeMessage(newLine)
  printMainMenu(newLine)
  
  if (errorMessage != None ):
    print('Error:',errorMessage)
  
  if (inputFile != None):
    print('Input:',inputFile,'(offset:'+str(inputFileOffset)+')')

  if (outputFile != None):
    print('Output:',outputFile)
  
  userChoice = printAcceptInput(newLine)
  if userChoice.isdigit() and int(userChoice)in acceptableRange:
    # processUserChoice(userChoice)
    if int(userChoice) == 1: 
      inputFile, outputFile, inputFileOffset = setupSession(newLine)
      errorMessage = None
    elif int(userChoice) == 2: 
      if inputFile is None or outputFile is None: 
        print('Please setup the session first!')
        inputFile, outputFile, inputFileOffset = setupSession(newLine)
        if inputFile is None or outputFile is None: 
          continue # Don't attempt to begin tagging 
      sessionEntityList = beginTagging(inputFile, inputFileOffset, outputFile, sessionEntityList)
      errorMessage = None
    elif int(userChoice) == 3: 
      sessionEntityList = manageSessionEntityList(sessionEntityList)
    else: 
      switchCase[int(userChoice)](newLine)
    
  else:
    if len(userChoice) > 0: 
      errorMessage = userChoice + ' is not a valid choice'
    else: 
      errorMessage = "Please select an option between " + str(acceptableRange)
    userChoice = -1
    
