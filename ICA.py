#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:05:34 2024

@author: Mogi
"""
class AuthoredResourse(object):
    def __init__ (self, authorlast, authorfirst , title, total_inventory):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.total_inventory = total_inventory

class Book(AuthoredResourse):
    def __init__(self, authorlast, authorfirst, title, total_inventory, place, publisher, year):
        super().__init__(authorlast, authorfirst, title, total_inventory)
        self.place = place
        self.publisher = publisher
        self.year = year
    
    def title_year(self):
        return self.title + " (" + self.year + ")"

    def set_total_inventory(self, total_inventory):
        self.total_inventory = total_inventory
        
    def get_total_inventory(self):
        return self.total_inventory
    
    def sold_one(self):
        if self.total_inventory == 0:
            print("there are no items left to sell")
        else:
            self.total_inventory -= 1
            print("Book's total_inventory: ", self.total_inventory)
        
    def write_bib_entry(self):
        return self.authorlast \
            + ' ,' + self.authorfirst \
            + ' ,' + self.title \
            + ' ,' + self.place \
            + ' ,' + self.publisher \
    
class Article(AuthoredResourse):
    def __init__(self, authorlast, authorfirst, articletitle, total_inventory, journaltitle, volume, pages, year):
        super().__init__(authorlast, authorfirst, articletitle, total_inventory )
        self.journaltitle = journaltitle
        self.volume = volume
        self.pages = pages
        self.year = year

    def set_total_inventory(self, total_inventory):
        self.total_inventory = total_inventory
    
    def get_total_inventory(self):
        return self.total_inventory
    
    def title_year(self):
        return self.title + " (" + self.year + ")"

    def sold_one(self):
        if self.total_inventory == 0:
            print("there are no items left to sell")
        else:
            self.total_inventory -= 1
            print("Article's total_inventory: ", self.total_inventory)
    
    def write_bib_entry(self):
        
    # title = [article1]
    # for 
        return self.authorlast \
            + ' ,' + self.authorfirst \
            + ' (' + self.year + '):' \
            + ' "' + self.title +' , " ' \
            + ' ,' + self.journaltitle + ' , ' \
            + self.volume + ' ,' \
            + self.pages + '.'
            

book1 = Book('John', 'Smith', 'CSS for beginner', 5 ,'London', 'a', '2006')

article1 = Article("Ellen", "Val", "Understanding CSS", 3, "", "", "", "2005")

titles = [book1, article1]

for title in titles:
    print(title.title_year(), ": ",  title.get_total_inventory())

totalInventory = 0
for title  in titles:
    totalInventory += title.get_total_inventory();
print("Total inventory: ", totalInventory)

book1.sold_one()
book1.sold_one()

article1.sold_one()
article1.sold_one()
