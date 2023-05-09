# Scrapy-python
Learn basic of scrapy that allows to scrape data from websties and store it in csv, json format also in databases
LEARNING HOW TO USE SCRAPY 

https://scrapeops.io/python-scrapy-playbook/freecodecamp-beginner-course/


1. PIP :- the PIP Installed packages that helps to install python packages

2. MODULES :- virtualenv, Scrapy, ipython
    ipython :- an interactive shell for python 

3. virtualenv :- virtualenv is used to manage Python packages for different projects. 
Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. 
You can install virtualenv using pip. Unix/macOS.
(to avoid any global issues while installing a packages in one packges that may or may not affect other projects)

4. To create a virtual environment use 
    command:- python -m venv foldername

5. Activate the venv folder so that any packages install after this will be used in this folder 
    command:-  (foldername)venv\Scripts\activate (for windows)

6. After activating the virutal env install Scrapy
    command:- pip install Scrapy

------------------------------------ PART - 3 UNDERSTAND THE SCRAPY PROJECT FOLDER  ------------------------------------
1. create a scrapy projects
    command:- scrapy startproject projectname

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

------------------------------------- PART - 4 WORKING WITH THE SPIDERS -------------------------------------

1. GENERATE SPIDER
    Command:- scrapy genspider spider_name url_of_website

2. IPYTHON INTERACTIVE SHELL 
    Go to the scrapy.cfg file and type shell = ipython after install this package

3. fetch('URL OF SITE')
    It scrapes whole stie and stores it's response in the variable. This will help to work on the (copy) site.

   ''' In [1]: fetch('https://books.toscrape.com/')'''
  

4.  command --> response
    This will tell a html variable in which whole  site is scraped and stored.
    #In [2]: response
    #Out[2]: <200 https://books.toscrape.com/>

5. To look for specific tag.
command --> response.css() --> can be class,id tag.

    '''In [6]: response.css('article.product_pod')
    Out[6]: 
    [<Selector xpath="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]" data='<article class="product_pod">\n       ...'>,
    <Selector xpath="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]" data='<article class="product_pod">\n       ...'>,
    <Selector xpath="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]" data='<article class="product_pod">\n       ...'>,'''

6. get only initial article code
    command --> response.css('').get()

        '''In [7]: response.css('article.product_pod').get()
        Out[7]: '<article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n
        <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n
        <p class="star-rating Three">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n
        <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£51.77</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n
    \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>' '''


7. get the len of total books shown on a single pages

    In [8]: books = response.css('article.product_pod')
    
    In [10]: len(books)
    Out[10]: 20


--------------------  REST THROUGH WEBSITE GIVEN ABOVE -----------------
