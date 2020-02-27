import xml.etree.ElementTree as ET


filename = 'mondial-3.0.xml'
path  = 'C:/Users/vic/Python/Python_Homework_6/mondial-3.0.xml'


def parse_and_remove(filename, path):
   path_parts = path.split('/')
   data = ET.iterparse(filename, ('start', 'end'))
   # Skip header
   next(data)
   
   tags = []
   elements = []
   for event, item in data:
    if event == 'start':
      tags.append(item.tag)
      elements.append(item)
    elif event == 'end':
                if tags == path_parts:
                    yield elements
                try: tags.pop()
                     elements.pop()
                except IndexError: pass


country_gov = {}

raw_data = parse_and_remove('mondial-3.0.xml', 'country')
for item in raw_data:
    print(item)
    print(dir(item))
    country_name = item.attrib['name']
    gov_name = item.attrib['government']
    country_gov[country_namen] = gov_name
