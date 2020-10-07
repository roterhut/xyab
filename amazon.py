#from bs4 import BeautifulSoup
#import requests
import sys
import re

if not len(sys.argv) == 2:
    usage = """
usage: amazon.py <Product URL from amazon website>

Example: amazon.py https://www.amazon/dp/B07D4NBPBC
     or: amazon.py www.amazon.de/dp/B07D4NBPBC
    """
    print(usage)
    exit()
amazon_url = "https://www.amazon.de/dp/B07D4NBPBC/?coliid=I319WKCKA7BBFQ&colid=1XEYCRQZQ0TJB&psc=1"
# Extract the Product ID form the amazon based URL
def product_id_extractor(url):
    return re.search(r'dp/(.+)\/', url).group(1)


# m = re.search(r'dp/(.+)\/', amazon_url)
# print(m.group(1))



# CamelCamelCamel Parser

