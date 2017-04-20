from test.test_decimal import file

if __name__ == '__main__':
    pass

inputFileName = 'Challenge_04_Text.txt'
result = ''

lineList = []
        
with open(inputFileName) as f:
    for line in f:
            lineList.append(line.strip('\n'))
            
#print(lineList[5], ' - ', len(lineList))

for lineNum in range(len(lineList)):
    
    # The below statements print the same substring
    #print('To end',lineList[lineNum][74:])
    #print('Neg c',lineList[lineNum][-6:-1],' ')
    
    for charNum in (range(len(lineList[lineNum]))):
        currChar = lineList[lineNum][charNum]
                
        if(currChar.islower()):
            #print('Lower case character')
             
            n,s,e,w = 0,0,0,0
            
            # Check to the North of the current character 
            # Check that the current character is not in the first row
            if(lineNum > 2 
               and lineList[lineNum - 1][charNum].isupper()
               and lineList[lineNum - 2][charNum].isupper()
               and lineList[lineNum - 3][charNum].isupper()):
                n = 1
            
            # Check to the South
            if(lineNum < len(lineList) - 4 
               and lineList[lineNum + 1][charNum].isupper()
               and lineList[lineNum + 2][charNum].isupper()
               and lineList[lineNum + 3][charNum].isupper()):            
                s = 1         
            
            # Check to the East
            if(charNum < 76 and charNum > 3):            
               #and lineList[lineNum][charNum:charNum + 3].isupper()):
                e = 1
                print(lineList[lineNum][charNum - 4],lineList[lineNum][charNum - 3:charNum], lineList[lineNum][charNum],lineList[lineNum][charNum + 1:charNum + 4],lineList[lineNum][charNum + 4])
                              
            # Check to the West
            if(charNum > 2 
               and lineList[lineNum][charNum - 1].isupper()
               and lineList[lineNum][charNum - 2].isupper()
               and lineList[lineNum][charNum - 3].isupper()):
                w = 1
            
            # Print the checks                                    
            #print(n,s,e,w)  
                                                
            # Check if 3/4 checks have been successful 
            if(n + s + e + w == 4): 
                # Append the character to the results string
                result = result + currChar
                print(n,s,e,w)  
                #print(currChar,lineList[lineNum][charNum - 1],lineList[lineNum][charNum - 3],lineList[lineNum][charNum - 3])                   
# Print the result
print('Length: ',len(result), 'Result: ', result)

outfile = open('outfile.txt','w')
outfile.write(result)
outfile.close()



