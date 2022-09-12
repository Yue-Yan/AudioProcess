# Annotation of voiceID
# Author: feiyue
# Date: 2022-09-10 Middle-August-Day

## About Data
#### For example, we have 5 different languages which distributed in seperate folders,in each folder there is one mp3 folder \
#### and a json file, the json file contains records of lots of records from different speakers.

## code
### 1. data_process.py
#### processing the data and get basic info: total duration, speaker number, unique speaker number etc.
## 2. call_API.py
#### call the API to get result
## 3. elasticsearch.py
#### 3.1 connect to host
#### 3.2 create index
#### 3.3 config mapping
#### 3.4 upload data
#### 3.5 query sample
#### 3.6 count of index
#### 3.8 delete one item
#### 3.9 delete index
## 4. matched_person.py
#### figure out how many speakers matched with the matched audios
## 5. version_compare.py
#### compare the results of different APIs
