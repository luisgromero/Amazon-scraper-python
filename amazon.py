
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Luis"
__date__ ="$Feb 22, 2014 10:39:34 PM$"

#Create a command line application called amazon.py.  
#The application accepts a couple of flags and an user
#query, and then prints out the first page of amazon store
#results based on the user supplied information.

import sys
import getopt

from bs4 import BeautifulSoup
from urllib2 import urlopen

#Amazon Products class
class Product:

    def __init__(self, title="", price="", rating="", reviews="", url=""):
        self.title=title
        self.price=price
        self.rating=rating
        self.reviews=reviews
        self.url=url

    def __repr__(self):
        return repr((self.title, self.price, self.rating,self.reviews,self.url))
    
    def printer(self):
        print self.title
        print self.price
        print self.rating
        print self.reviews
        print self.url

#Amazon product list (stores Products)
class AmazonResultList:
    def __init__(self,list=[]):
        self.list=list
        
    def __repr__(self):
        return repr((self.list))
    
    def add_product(self,Product):
        self.list.append(Product)
    
    def printer(self):
        for product in self.list:
            print product.title
            print "Price: " + product.price
            print "Rating: " + product.rating + " ("+product.reviews+" reviews)"
            print "Url: " + product.url
            print ("")
            
    def get_list(self):
        return self.list
    
    def set_list(self,list):
        self.list=list
    
    def count(self):
        print len(self.list)
        
#This function scrapes the information from the amazon search page result and returns a product list            
def scrapper(search):
    query="http://www.amazon.com/s/?field-keywords=" + search
    html= urlopen(query).read()
    urlopen(query).close()
    soup=BeautifulSoup(html.decode('utf-8', 'ignore'))
    results=AmazonResultList()
    
    for a in soup.find_all('div','productData'):
        pTitle=((a.findNext('a').text).lstrip())
        pPrice=(a.findNext('div','newPrice').span.text)
        pRating=(a.findNext('div','starsAndPrime').img['alt'])
        pUrl=(a.findNext('div','newPrice').a['href'])
        pReview=(a.findNext('img',{'width':'11'}).find_next('a').text)
        p=Product(pTitle, pPrice, pRating, pReview, pUrl)
        results.add_product(p)
    return results
        
def main(argv):
    sort_by=""
    sort_type=0
    pList=AmazonResultList()
    #print str(sys.argv)
    try:
        opts, args = getopt.getopt(argv, "h", ["sort=","asc=","desc=","prime=","limit="])
        
    except getopt.GetoptError:
        print "Wrong use of command line arguments e.g ./amazon.py --sort price --desc \"office chairs\""
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print "e.g ./amazon.py --sort price --desc office chairs"
            sys.exit()
        elif opt in ("--sort"):
            #rating, price, name
            
            sort_by=str(arg)
            if(sort_by=="rating"):
                sort_type=2
            elif(sort_by=="price"): 
                sort_type=1
            elif(sort_by=="name"): 
                sort_type=0
                
        elif opt in ("--asc"):
            #ascending order option
            
            search=(str(arg)).replace(" ","%20")
            pList=scrapper(search)
        
            newList=pList.get_list()
            if(sort_type==2):
               nList=sorted(newList, key=lambda x: x.rating) 
            elif(sort_type==1): 
               nList=sorted(newList, key=lambda x: float((x.price).replace("$","")))  
            elif(sort_type==0):
                nList=sorted(newList, key=lambda x: x.title) 
         
            pList.set_list(nList)
            pList.printer()
            
        elif opt in ("--desc"):
            #descending order option

            search=(str(arg)).replace(" ","%20")
            pList=scrapper(search)
            pList.printer()
      
            newList=pList.get_list()
            if(sort_type==2):
               nList=sorted(newList, key=lambda x: x.rating, reverse=True) 
            elif(sort_type==1): 
               nList=sorted(newList, key=lambda x: float((x.price).replace("$","")),reverse=True)  
            elif(sort_type==0):
                nList=sorted(newList, key=lambda x: x.title, reverse=True) 

            pList.set_list(nList)
            pList.printer()
            
        elif opt in ("--prime"):
            print "Prime: BONUS "
            
        elif opt in ("--limit"):
            print "Limit: BONUS ", str(arg)
   
        else:
            assert False, "unhandled option"
                  
if __name__ == "__main__":
    main(sys.argv[1:])

