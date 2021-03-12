import glob
import zipfile
import csv
import os
import shutil

zippedFiles=glob.glob("*.zip")

plantData=[]

for zippedFile in zippedFiles:
  dirName, fileExt = os.path.splitext(zippedFile)
  if os.path.exists(dirName):
    shutil.rmtree(dirName)
  os.mkdir(dirName)
  with zipfile.ZipFile(zippedFile, 'r') as zip_ref:
    zip_ref.extractall(dirName)
  
  locDataFn="%s/occurrence.txt" % dirName
  
  locData = list(csv.DictReader(open(locDataFn, 'r'), delimiter='\t'))
  plantData.extend(list(locData))

try:
  fieldNames = plantData[0].keys()
except:
  exit(0)

with open('scrubCommunityPlants.csv', 'w', newline='') as csvfile:
  writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
  writer.writeheader()
  for entry in plantData:
    writer.writerow(entry)

  

