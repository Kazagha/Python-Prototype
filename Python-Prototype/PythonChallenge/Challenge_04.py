from test.test_decimal import file

if __name__ == '__main__':
    pass

inputFileName = 'Challenge_04_Text.txt'

lineList = []
        
with open(inputFileName) as f:
    for line in f:
            lineList.append(line)
            
#print(lineList[5], ' - ', len(lineList))

for lineNum in range(len(lineList)):
    for charNum in (range(len(lineList[lineNum]))):
        currChar = lineList[lineNum][charNum]
        
        if(currChar.islower()):
            print('Lower case character')
             
            n,s,e,w = 0,0,0,0
            
            # Check to the North of the current character 
            # Check that the current character is not in the first row
            if(lineNum - 1 >= 0 and lineList[lineNum - 1][charNum].islower()):
                n = 1
            
            # Check to the South
            
            # Check to the East
            
            # Check to the West
            
            # Check if 3/4 checks have been successful 
            
                # Append the character to the results string
          