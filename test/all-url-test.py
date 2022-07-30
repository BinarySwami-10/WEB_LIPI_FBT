import requests
import requests.exceptions

if __name__ == '__main__':
    domain = 'crayonpapers'
    tld = ['.com', '.in']
    subdomains = ['www.', '']
    schemas = ['http://', 'https://']

    urls = [sch + sub + domain +
            t for sch in schemas for sub in subdomains for t in tld]

    # [print(x) for x in urls]

    for u in urls:
        try:
            r = requests.get(u)
            print(r, "=>", r.url)
        except Exception as e:
            print('FAILED', u)
            print('might be due to SSL')

'''
[ 'args', 'characters_written', 'errno', 'filename', 'filename2', 'request', 'response', 'strerror', 'winerror', 'with_traceback']
'''
