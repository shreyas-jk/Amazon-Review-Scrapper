# Amazon Review Scrapper

Using this repository, you can retrieve customer review from Amazon without any coding. Passing approriates parameters, you'll be able to run the script and get all reviews with ease.

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

## Note
The [url] needs to be the Amazon product url, not the review page url.
