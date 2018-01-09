import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    page_website = "http://quotes.yourdictionary.com/theme/marriage/"
    page_open = urllib2.urlopen(page_website).read()
    soup = BS.BeautifulSoup(page_open)

    quotes = soup.findAll(attrs={"class": "quoteContent"})

    for quote in quotes:
        print "quote: %s" % (quote.string)

