import re
import string

if __name__ == '__main__':
    pass

def translate(inputStr):

    outputStr = ""
    
    list = [char for char in string.ascii_lowercase[2:] + string.ascii_lowercase[:2]]
    
    for char in inputStr:    
        if(re.findall('[a-z]',char)):
            charNum = list.index(char) + 2  
            
            if(charNum >= 26):
                    charNum = charNum - 26
                
            outputStr = outputStr + list[charNum]
            #print('{0} - {1}'.format(list.index(char),list.index(char) + 2))
        else:
            outputStr = outputStr + char
            
    #print (outputStr)
    return outputStr

#str.maketrans
print(translate("""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""))
print(translate("map"))