# **Tooltip functionality  for Tableau**



Datafiles used in  `[metadata csv file]` and `[data csv file]`. Data file contains data about the metadata.

`Data CSV`- Is the source file which need to be updated with tooltips.For XML format of data csv -Open in tableau and save it as
tds file`(source.tds).`

**Metadata CSV file contains three fields :**

1. **Field** - This column has all the field names, which are available in Heidi plus.


2. **Description** - This column has the descriptions of all the fields.


3. **Additional details** - This column has additional changes, which happened in datasources. E.g. fixed data details,  column name changes etc.



## **Detail of the codes**

Module used in `tooltip.py`- import `CSV`, import `OS(operating system)`, import` Element tree`(To read and manipulate XMLs)
We have used etree module in Python to generate formatted  XML to present text in Tooltip.

1. A variable `(metadata`), of type data dictionary, is created to store and manipulate the content of metadata.csv.

2. Function Get_Metadata-This function opens the data.csv file and the metadata.csv file and puts the fields from metadata.csv in this dictionary.
  ` [Field]` column is set as a key and `[description]` ,`[additional details]` columns are values. 
3. Function Replace_None-Removing all the none fields available in Additional details with the text. 
4. Function Generate_XML-Opens data file(csv) and `source.tds`( WRITTEN IN XML) file. The root to get the columns which we need to update.
   First loop finds the root of the XML, picks the two columns `[name]` and `[role]`. 
  ` [name]` field gets populated with values from  metadata.csv  and `[role]` has 'Dimension' and 'Measure'.
   `[desc]` is the node in source xml and inside this node we have SubElements.



example :
  ` <desc>`
        `<formatted-text>`
                      ` <run>`


   Second loop adds subelements in xml for formatted text, after removing desc if `[desc]` as not none.
   Inside the `(formatted text)` is added the `(run)`Subelement.
   In `(run)` is added further elements e.g. labels , formatting, and the column name which are required for  Tooltip.
   
   The final output is the new xml file ` [tooltip.tds]`  with the expected outcome.



