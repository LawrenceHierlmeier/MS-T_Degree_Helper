import re
import json

#----------------------#
#Only Change These Variables:
filestring = "compscicatalogsource.html"
department = "COMP_SCI"
#----------------------#

regex = (
    r"<p class=\"courseblocktitle\" id=\".*?\"><em><strong>.*?;(\d+) +(.*?)</strong></em> \((\D*?) (.*?)\)</p>\n<p class=\"courseblockdesc\">\n(.*?)<br />\n"
    r"<hr />\n"
    r"</p>")


with open(filestring, 'r') as file:
    data = file.read()

with open("idkeeper", 'r') as file:
    global index
    index = int(file.read())

matches = re.finditer(regex, data, re.MULTILINE | re.DOTALL)

list_of_courses = []

for matchNum, match in enumerate(matches, start=1):
    index += 1
    temp = {"name":match.group(2),"coursenum":match.group(1),"internal_id":index,"department":department,"hrs":match.group(4),"type":match.group(3),"description":match.group(5), "prereqs":[],"coreqs":[]}
    list_of_courses.append(temp)

with open("mstdatabase.json", 'w') as file:
    json.dump(list_of_courses,file, indent=4)

with open("idkeeper", 'w') as file:
    file.write(str(index))