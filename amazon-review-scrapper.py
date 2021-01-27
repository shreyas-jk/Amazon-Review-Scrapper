import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit, urlunsplit
import time
import pandas as pd 

def writeFile(data):
    file = open("lastcall.txt", "w", encoding='utf-8')
    file.write(data)
    file.close()
    
def rm_RBrackets(value):
    return value.replace("[","").replace("]","")
    
def getContent(site):
    review_set = pd.DataFrame(columns = ['title', 'body']) 
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    review_block = soup.select("body div #cm_cr-review_list > .review .review-data > span")
    soup = BeautifulSoup(rm_RBrackets(str(review_block)), "html.parser")
    
    review_span = soup.findAll(attrs={'class': None})
    
    for node in review_span:
        value = rm_RBrackets(str(node.findAll(text=True)))
        if value != "": 
            review_set = review_set.append({'reviews': str(value.lstrip("'").lstrip('"')) }, ignore_index = True)    
    reviews = review_set.copy()
    return reviews

def generateReviewEndPoints(url, start, no_pages):
    lst = []
    for i in range(start, start + no_pages):
        lst.append(url + '&pageNumber=' + str(i))
    return lst

def getReviewPageUrl(site, baseUrl):
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    writeFile(str(soup))
    url_block = soup.select("body div .a-link-emphasis")
    soup = BeautifulSoup(rm_RBrackets(str(url_block)), "html.parser").a
    return baseUrl + soup['href']

def getBaseUrl(link):
    split_url = urlsplit(link)
    valueLink = split_url.scheme + '://' + split_url.netloc
    return valueLink

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Amazon Review Scrapper")
    parser.add_argument("--u", required=True, help="Amazon product url")
    parser.add_argument("--n", required=True, type=int, help="Number of pages")
    parser.add_argument("--s", type=int, help="Starting page number. Default will start from 1st page")
    parser.add_argument("--i", type=int, help="Set interval (in secs). Default: 3")
    args = parser.parse_args()
    
    interval = args.i
    interval = 3 if interval is None else interval
    start = 1 if args.s is None else args.s
    
    print('Operation delay set {} after each fetch'.format(interval))
    review_fullset = pd.DataFrame(columns = ['reviews']) 
    baseUrl = getBaseUrl(args.u) 
    review_mainpage_url = getReviewPageUrl(args.u, baseUrl)
    reviewUrlList = generateReviewEndPoints(review_mainpage_url, start, args.n)
    
    for index, url in enumerate(reviewUrlList):
        print('Fetching reviews from page {}...'.format(start + index))
        review_fullset = pd.concat([review_fullset, getContent(url)], axis=0)
        time.sleep(interval)
    review_fullset.to_csv('reviewdata.csv', index=False)
    print("Done")
    
        
        
        
        
        
