#One must set the following environment variables:
#GBIF_USER
#GBIF_PWD
#GBIF_EMAIL

from pygbif import occurrences as occ
from pygbif import species
import csv
import time
import sys

args = sys.argv
fn = args[1]

print(args)

print("reading", fn)

boundBox='-87.9, 24.2, -79.9, 31.1' 

csvfile = open(fn)
plantData = csv.DictReader(csvfile)
dlList = []

for row in plantData:
  sp_name="%s" % row['Scientific Name'] 
  print(sp_name)
  gbifSpcInfo=species.name_backbone(name = sp_name)
  print(gbifSpcInfo['usageKey'])
  taxonKeySel="taxonKey = %s" % gbifSpcInfo['usageKey']
  print(taxonKeySel)
  dl = occ.download( [ taxonKeySel, 'basisOfRecord = HUMAN_OBSERVATION', 'hasCoordinate = True', 'decimalLongitude > -87.9', 'decimalLongitude < -79.9', 'decimalLatitude > 24.2', 'decimalLatitude < 31.1' ])
  dlMeta = occ.download_meta(dl[0])
  print(dlMeta)
  while dlMeta['status'] != 'SUCCEEDED' and dlMeta['status'] != 'KILLED':
      time.sleep(30)
      dlMeta = occ.download_meta(dl[0])
      print(dlMeta)
  
  if dlMeta['status'] == 'SUCCEEDED':
    dlList.append(dl)


for dl in dlList:
    try:
        occ.download_get(dl[0])
    except:
        pass
