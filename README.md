# bingScraper
A simple web-scraper using the Bing Image Search API <br>

Link your [Bing Search API-Key](https://azure.microsoft.com/en-us/try/cognitive-services/?api=bing-image-search-api) 
```bash
touch api.key && echo "<API_KEY>" > api.key
```
Make a folder inside the datasets folder for your subclass 
```bash
cd datasets/ && mkdir <subclass_name>
```
Run the python script in terminal with the required arguments
```bash
python3 scraper.py -q "<relevant keywords>" -n <integer value> -o /datasets/<subclass_name> 
```
For help
```bash
python3 scraper.py -h
```

| Arguments  | Description      |
| ---------- | -----------------|
| -h         | help message     |
| -q         | query            |
| -n         | number of results|
| -o         | output directory |


Credits: [Adrian Rosebrock](https://github.com/jrosebr1) 🥳

