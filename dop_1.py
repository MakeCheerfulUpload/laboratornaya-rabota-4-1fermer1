import xmltodict
import json

with open('tableXML.xml') as fd:
    doc = xmltodict.parse(fd.read())
text = json.dumps(doc)

tableJSON = u'{\n\t'
numberTubs = 1
for i in range(1, len(text)):
    if text[i] == '{':
        tableJSON += '{\n'
        numberTubs += 1
        tableJSON += ('\t' * numberTubs)
    elif (i < len(text) - 1) and (i > 0) and (text[i - 1] + text[i] + text[i + 1] == ', "'):
        continue
    elif (i < len(text) - 2) and (text[i] + text[i + 1] + text[i + 2] == ', "'):
        tableJSON += ',\n'
        tableJSON += ('\t' * numberTubs)
    elif text[i] == '}':
        tableJSON += '\n'
        numberTubs -= 1
        tableJSON += ('\t' * numberTubs + '}')
    else:
        tableJSON += text[i]

fileNew = open('dop1_JSON.json', 'w')
fileNew.write(tableJSON)
fileNew.close()
