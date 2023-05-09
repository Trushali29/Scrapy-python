# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class BookscraperPipeline:
    def process_item(self, item, spider):
        return item

class SaveToMySQLPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            database = 'books'
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS books(
        id int NOT NULL auto_increment,
        name text,
        price VARCHAR(255),
        url VARCHAR(255),
        PRIMARY KEY (id)
        )
        
        """)

    def process_item(self,item,spider):
        self.cur.execute(""" 
         INSERT INTO books(
         name,price,url
         )  VALUES(%s,%s,%s)""",(item["name"],item["price"],item["url"]))
        
        self.conn.commit()



    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()