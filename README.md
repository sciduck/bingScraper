# bingScraper
A simple web-scraper using the Bing Image Search API <br>

<br>
<b>Usage:</b>
Make a folder inside the datasets folder for your subclass 
```
cd datasets/ && mkdir <subclass_name>
```
Run the python script in terminal with the required arguments
```
python3 scraper.py -q "<relevant keywords>" -o /datasets/<subclass_name>
```
For help
```
python3 scraper.py -h
```

| Arguments  | Description      |
| ---------- | -----------------|
| -h         | help message     |
| -q         | query            |
| -o         | output directory |


Credits: [Adrian Rosebrock](https://github.com/jrosebr1)
