# Scrapy-python
Learn basic of scrapy module of python that allows to scrape data from websties and store it in csv, json format also in databases. 
The project aim was to store the parsed data of websites in database such as in mysql.



**RESOURCES SHOULD BE PRESENT FOR PROJECT TO WORK**
1. Visual Studio code or any code editor
2. Latest Python Installed
3. Scrapy module 
4. Virtual Environment module
5. ipython module
6. MYSQL installed
7. Windows OS
\n3, 4, and 5 are python modules there installation steps are given below.



**STEPS TO FOLLOW AS PER PROJECT**
1. PIP :- the PIP Installed packages that helps to install python packages.

2. MODULES :- virtualenv, Scrapy, ipython
    ipython :- an interactive shell for python. 

3. virtualenv :- virtualenv is used to manage Python packages for different projects. 
Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. 
You can install virtualenv using pip. Unix/macOS.
(to avoid any global issues while installing a packages in one packges that may or may not affect other projects)

4. To create a virtual environment use. 
    command:- python -m venv foldername

5. Activate the venv folder so that any packages install after this will be used in this folder.
    command:-  (foldername)venv\Scripts\activate (for windows)

6. After activating the virutal env install Scrapy.
    command:- pip install Scrapy



**UNDERSTAND THE SCRAPY PROJECT FOLDER**

1. create a scrapy projects
    command:- scrapy startproject projectname.

2. spider folder

3. SPIDER.PY 
    It goes to the URL given to scrape and ones it reached to the sites then it starts parsing the site based on the title, tag, css selectors like class, id, links.
    parse() function is used to parse the website and extract delails.
    Later, this details can be stored in the csv, json, xml any data storage format also in database.

4. ITEMS.py
    IN which order should all the items that will be parsed should be stored. A model to store the data. It is a model for the extracted data. You can define a custom model (like a ProductItem) that will inherit the Scrapy Item class and contain your scraped data.

5. SETTINGS.py 
   where all your project settings are contained, like activating pipelines, middlewares etc. Here you can change the delays, concurrency, and lots more things.

   5.1 ROBOTS.txt
    Tells whether the spider can crawl this site or not. Which are the user-agents allowed to access this site.
    Which sites pages are not allowed to crawl.

   5.2 It also tells how many concurrent request can be many to a particular site 32,100.. 

   5.3 It also consist spider middlewares, downloader middlewares which are implemented in middlewares.py. If design a new middlewares it should be mentioned in the settings.py file.

6. PIPLINES.py  
    where the item yielded by the spider gets passed, it’s mostly used to clean the text and connect to file outputs or databases (CSV, JSON SQL, etc).

7. MIDDLEWARES.py 
    It is useful when you want to modify how the request is made and scrapy handles the response.
    scrapy.cfg is a configuration file to change some deployment settings, etc.
    how long would you make a request to a site?
    what types of user-agent is used to make a request
    what types of request is to be made to a site.

    7.1 TYPES OF MIDDLEWARES
        Consist middlewares which are assigned in settings.py. 

**PART - 4 WORKING WITH THE SPIDERS**

1. GENERATE SPIDER
    Command:- scrapy genspider spider_name url_of_website

2. IPYTHON INTERACTIVE SHELL 
    Go to the scrapy.cfg file and type **shell = ipython** after install this package.


**STEPS TO FOLLOWED FROM THE BELOW WEBSITES TO LEARN SCRAPY**

**Part 1: Course & Scrapy Overview**

**Part 2: Setting Up Environment & Scrapy**

**Part 3: Creating Scrapy Project**

**Part 4: First Scrapy Spider**

**Part 5: Crawling With Scrapy**

**Part 6: Cleaning Data With Item Pipelines**

**Part 7: Storing Data In CSVs & Databases**

**RESOURCES :-**  https://scrapeops.io/python-scrapy-playbook/freecodecamp-beginner-course/


