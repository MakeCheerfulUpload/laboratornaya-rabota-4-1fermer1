fileXML = open('tableXML.xml', 'r', encoding='windows-1251')
fileJSON = open('tableJSON.json', 'w')

orderHeaders = ['']
newHeader = ''
fileJSON.write('{\n')
linesXML = fileXML.readlines()
fileXML.close()
for i in range(1, len(linesXML)):
    temp = linesXML[i].split('<')
    a = '\t' + temp[0]
    fileJSON.write(a)
    if len(temp) == 2:
        for j in temp[1]:
            if j == '>': break
            newHeader += j
        if newHeader == ('/' + orderHeaders[len(orderHeaders) - 1]):
            fileJSON.write('}')
            orderHeaders.pop()
            if (i < len(linesXML) - 1) and not(linesXML[i + 1].__contains__(orderHeaders[len(orderHeaders) - 1])):
                fileJSON.write(',')
            newHeader = ''
        else:
            orderHeaders.append(newHeader)
            fileJSON.write('"' + newHeader + '": {')
            newHeader = ''
    else:
        for j in temp[1]:
            if j == '>': break
            newHeader += j
        fileJSON.write('"' + newHeader + '": "' + temp[1].split('>')[1] + '"')
        if not(linesXML[i + 1].__contains__(orderHeaders[len(orderHeaders) - 1])): fileJSON.write(',')
        newHeader = ''
    fileJSON.write('\n')
fileJSON.write('}')

fileJSON.close()
