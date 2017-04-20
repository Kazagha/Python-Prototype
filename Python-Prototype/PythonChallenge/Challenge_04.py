from test.test_decimal import file

if __name__ == '__main__':
    pass

inputFileName = 'Challenge_04_Text.txt'
result = ''

lineList = []

# Load the file into a list        
with open(inputFileName) as f:
    for line in f:
            # Append the line onto the list
            # Strip the tailing carriage return / new line character
            lineList.append(line.strip('\n'))

for lineNum in range(len(lineList)):
    for charNum in (range(len(lineList[lineNum]))):
        currChar = lineList[lineNum][charNum]
                
        if(currChar.islower()):    
            
            # Check to the East
            if(charNum < 76 and charNum > 3
               and lineList[lineNum][charNum - 4].islower()
               and lineList[lineNum][charNum - 3:charNum].isupper()
               and lineList[lineNum][charNum].islower()
               and lineList[lineNum][charNum + 1:charNum + 4].isupper()
               and lineList[lineNum][charNum + 4].islower()
               ):            
                # Print the result to check that it is correct
                print(lineList[lineNum][charNum - 4],lineList[lineNum][charNum - 3:charNum], lineList[lineNum][charNum],lineList[lineNum][charNum + 1:charNum + 4],lineList[lineNum][charNum + 4])
                # Add the character to the result string
                result = result + currChar           
  
                  
# Print the result 
print('Length: ',len(result), 'Result: ', result)




