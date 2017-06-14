import urllib2

def read_file():
    quotes = open("/Users/aubuchcl/desktop/movie_quotes.txt")

    contents_of_file = quotes.read()
    print(contents_of_file)
    #close the file
    quotes.close()
    #do something to check the file
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    url = urllib2.urlencode 'http://www.wdylike.appspot.com/?q='+text_to_check
    connection = urllib2.urlopen(url)
    output = connection.read()
    print(output)
    connection.close()



read_file()
