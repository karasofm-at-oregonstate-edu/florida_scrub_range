This directory holds tools to download data from gbif and create a table.  These are simple scripts.  It is advised to run these out of an empty directory.

#gbif_query.py downloads data from gbif given a species list. 

SYNTAX:

gbif_query.py <csv file> [bounding box]

The csv file must have species in a column labled 'Scientific Name'.  The script will query GBIF for each species name in the 'Scientific Name' column in the csv file. Species names should be recognized scientific names. 

The optional bounding box is for coordinates in decimal degrees forat:  'West, South, East, North'.  If no bounding box is provided, the search will be global.

The script first queries GBIF for the species in the csv file, and queues the download.  It waits for download ready or query failed (see gbif docs for why it may fail) before going to the next item on the list.  Each query can take a couple minutes.  After all items have been quearied, it downloads all succesful queries in the directory the script is run in.  This script may take a while to run if there are a lot of files.  

In order for this script to work, one must set the following environment variables

GBIF_USER
GBIF_PWD
GBIF_EMAIL


#gbif_tbl.py Creates a table from heterogenous GBIF download files.

SYNTAX:

gbif_tbl.py

This script processes a set of GBIF zipped download files for a species query, opens them, and create a single table for all the downloads.  The script must be run in the same directory as the zipped files, and all the zipped files must be valid GBIF data (otherwise bad things happen...)

#Future features:
Output directory for download
Input directory for gbif_tbl.
