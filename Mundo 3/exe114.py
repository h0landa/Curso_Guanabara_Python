import urllib
import urllib.request


try:
    site = 'https://www.youtube.com'
    urllib.request.urlopen(site)
except urllib.error.URLError:
    print('O site está inacessivel no momento.')
else:
    print('O site está acessivel.')
