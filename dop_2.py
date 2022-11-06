import re

fileXML = open('tableXML.xml', 'r', encoding='windows-1251')
fileJSON = open('dop2_JSON.json', 'w')

orderHeaders = ['']
newHeader = ''
fileJSON.write('{\n')
linesXML = fileXML.readlines()
for i in range(1, len(linesXML)):
    temp = re.split(r'[<>]', linesXML[i])
    fileJSON.write('\t' + temp[0])
    if len(temp) == 3:
        if orderHeaders[len(orderHeaders) - 1] == temp[1]:
            orderHeaders.pop()
            fileJSON.write('}')
            if (i < len(linesXML) - 1) and not(re.fullmatch(r'\t*</.*>\n?', linesXML[i + 1])):
                fileJSON.write(',')
            fileJSON.write('\n')

        else:
            fileJSON.write(f'"{temp[1]}": ' + '{\n')
            orderHeaders.append('/' + temp[1])
    else:
        fileJSON.write(f'"{temp[1]}": "{temp[2]}"')
        if not re.fullmatch(r'\t*</.*\n', linesXML[i + 1]):
            fileJSON.write(',')
        fileJSON.write('\n')

fileJSON.write('}')

fileJSON.close()