from mxproxy import mx

url = 'https://www.holidify.com/collections/tourist-places-in-india'
iter_class = 'div.row.no-gutters.d-flex > div.col-12.col-md-6.pr-md-3'
filename = url.split('/')[-1]
i = 0

parse_table = {
    'title': 'h3',
    'known_for': '.card-body > p:nth-child(1)',
    'desc': '.card-body > p:nth-child(2)',
    'best_time': '.card-body > p:nth-child(3)',
    }

json_derulo = {'data': []}

for x in mx.get_page_soup(url).select(iter_class):
    i += 1
    title = x.select_one('h3')
    json_derulo['data']
    # print(x.prettify())

print(i)
