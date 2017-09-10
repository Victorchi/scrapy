# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import hashlib
from datetime import *
from dbtuils import MySQLHelper


class JournalPipeline(object):
    def process_item(self, item, spider):
        try:
            url = item['url']
            title = item['title'][0]
            id = item['id']
            vendor = item['vendor']
            hashValue = hashlib.md5(url).hexdigest()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "INSERT INTO `journals` (url,`title`,`id`,vendor,searchcode,insertTime) VALUES ('%s','%s','%s','%s','%s','%s')"%(url,title,id,vendor,hashValue,now)
            print sql
            MySQLHelper().insert(sql)
        except MySQLdb.Error,e:
            print 'Error %d: %s'%(e.args[0],e.args[1])
        return item
