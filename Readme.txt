First Unzip the folder in Drive ( C drive Suggested)

---------------------------------------------------------------------------------------------
It was expected that following two APIs should be build:
---------------------------------------------------------------------------------------------

Task 1  Question :- 
api/newslist (provides news list in the form of json objects).
Following are the attributes of each json object:
 publishedDate
 title
 summary
 source
 authors
-----------------------------------------------------
Steps to Execute Task 1 

Unzipped your file  in c drive
open command prompt

step 1 :  cd C:

step 2 :  cd internship 

step 3 :  cd api1

step 4 :  python file1.py

copy that api  looking like  " http:/127.0.0.1:5000/ "  on postmen or URL of Browser

If you only enter  " http:/127.0.0.1:5000/  "  , You will get Text that api has created.

next ,

To provide news list in the form of json objects with filtered date , type below
http:/127.0.0.1:5000/newslist 

you will get newslist  n the form of json objects  with filtered date


Also task to search keywords in title as parameters , type below

http:/127.0.0.1:5000/newslist/title/'<title-name>'
for example :
http:/127.0.0.1:5000/newslist/title/'Popoy'


See json object and give title accordingly and give title in single quotes

---------------------------------------------------------------------------------------------------------------------------------------

Task 2 Question :- 
api/news/id (provides details json object for given news id). It
should contain following attributes for single json object:
 publishedDate
 title
 description
 source
 author
 imageurl
 summary

-----------------------------------------------------
Steps to Execute Task 2

ctrl + c to come out of api from command prompt

step 1 : cd internship

step 2 :  cd api2

step 3 :  python file2.py

copy that api  looking like  " http:/127.0.0.1:5000/ "  on postmen or URL of Browser

If you only enter  " http:/127.0.0.1:5000/  "  , You will get Text that api has created.

next ,

First see data, type below
http:/127.0.0.1:5000/news

To provide details of json object for given news id, type below
http:/127.0.0.1:5000/news/id/<your id> 
for example
http:/127.0.0.1:5000/news/id/4

you will get details of json object for given news id

---------------------------------------------------------------------------------------

each python file has different  database file
















