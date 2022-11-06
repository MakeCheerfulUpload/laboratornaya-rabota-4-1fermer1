import re

fileXML = open('tableXML.xml', 'r', encoding='windows-1251')

orderHeaders = []
newHeader = ''
linesXML = fileXML.readlines()
fileXML.close()

firstStr = ''
secondStr = ''

for i in range(1, len(linesXML) - 1):
    temp0 = re.split(r'<|>', linesXML[i])
    temp1 = re.split(r'<|>', linesXML[i + 1])
    if len(temp0[0]) < len(temp1[0]):
        orderHeaders.append(temp0[1])
    elif len(temp0) == 5:
        if firstStr != '':
            firstStr += ','
            secondStr += ','
        firstStr += str(orderHeaders).replace("', '", '/')[2:-2] + f'/{temp0[1]}'
        if temp0[2].__contains__(','):
            secondStr += f'"{temp0[2]}"'
        else:
            secondStr += temp0[2]
    if len(temp0[0]) > len(temp1[0]):
        orderHeaders.pop()


fileCSV = open('dop_4CSV.csv', 'w', encoding='utf-8')
fileCSV.write(firstStr)
fileCSV.write('\n')
fileCSV.write(secondStr)
fileCSV.close()
