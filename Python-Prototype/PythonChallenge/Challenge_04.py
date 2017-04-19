from test.test_decimal import file

if __name__ == '__main__':
    pass

inputFileName = 'Challenge_04_Text.txt'
result = 'this is a test'

lineList = []
        
with open(inputFileName) as f:
    for line in f:
            lineList.append(line)
            
#print(lineList[5], ' - ', len(lineList))

for lineNum in range(len(lineList)):
    for charNum in (range(len(lineList[lineNum]))):
        currChar = lineList[lineNum][charNum]
                
        if(currChar.islower()):
            #print('Lower case character')
             
            n,s,e,w = 0,0,0,0
            
            # Check to the North of the current character 
            # Check that the current character is not in the first row
            if(lineNum - 1 >= 0 and lineList[lineNum - 1][charNum].isupper()):
                n = 1
            
            # Check to the South
            if(lineNum + 1 < len(lineList) and lineList[lineNum + 1][charNum].isupper()):
                s = 1
        
            # Check to the East
            if(charNum + 1 <= 80 and lineList[lineNum][charNum + 1].isupper()):
                e = 1
                              
            # Check to the West
            if(charNum - 1 >= 0 and lineList[lineNum][charNum - 1].isupper()):
                w = 1
            
            # Print the checks                                    
            #print(n,s,e,w)  
                                                
            # Check if 3/4 checks have been successful 
            if(n + s + e + w == 3):   
                # Append the character to the results string
                result = result + currChar
                print(currChar)
                   
# Print the result
print('Length: ',len(result), 'Result: ', result)

outfile = open('outfile.txt','w')
outfile.write(result)
outfile.close()



