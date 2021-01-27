# Amazon Review Scrapper

Using this repository, you can retrieve customer reviews from Amazon without any coding. Passing appropriate parameters, you'll be able to run the script and get all reviews with ease.

The retrieve reviews will be exported in the same directory (csv format).

| Parameter | Decription |
| ------ | ------ |
| --u | Amazon product url |
| --n | Number of pages |
| --s | Starting page number. Default will start from 1st page  (optional) |
| --i | Set interval (in secs). Default: 3  (optional) |




# Tell me how to run? 


```sh
python amazon-review-scrapper.py --u "[url]" --n 3
```
Above command will download reviews from first 3 pages starting from 1st review page.


```sh
python amazon-review-scrapper.py --u "[url]" --n 3 --s 10
```
Above command will download reviews from 3 pages starting from page 10 (i.e from pages 10, 11, 12).


```sh
python amazon-review-scrapper.py --u "[url]" --n 3 --i 7
```
Above command will download reviews from [n] pages with an interval of 7 secs. 

![alt text](https://i.ibb.co/ZKrz43s/Capture.png)

# Why is it not fetching reviews?
This script works! But there's a limit! (not set by me but Amazon). 

After running the script successfully for multiple times, Amazon revokes the privilege of reading their HTML source and thus the script won't be able to scrape it anymore. The privilge resets after a certain period (maybe 24 hours). In that case, you can try using VPN or sadly, just wait for a day.

To check if that's the case for not retrieve thet data, on running the script generates a file names 'lastcall.txt', which is basically the raw HTML file of the last request call. Check out the file for further details.

## Note
The [url] needs to be the Amazon product url, not the review page url.
