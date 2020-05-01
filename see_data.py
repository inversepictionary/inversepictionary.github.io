
import json
import time

import urllib
import urllib.request
import random

def save_drawing(data_uri, filename):
  data = data_uri
  response = urllib.request.urlopen(data)
  with open(filename + '.jpg', 'wb') as f:
      f.write(response.file.read())

with open('inversepictionary-export.json') as f:
  data = json.load(f)

drawings = [key for key, val in data['Drawings'].items()]

index = random.randint(0, 1000)

save_drawing(data['Drawings'][drawings[index]]["raw_image"], "drawings/" + str(index))

rolling = False
if(rolling):
  for key, val in data['Descriptions'].items():
      print(val['user_ID'])
      print(val['description'])
      time.sleep(1)

print(len([key for key, val in data['Descriptions'].items()]))
print(len([key for key, val in data['Drawings'].items()]))