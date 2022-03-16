import bs4
from mxproxy import mx
string=open('flightresult.html').read()

soup=mx.make_soup(string)

print(soup.select_one('span.price').find_next_sibling())