import requests
from bs4 import BeautifulSoup
    
def get_citations_needed_count(soup):
    # https://www.pluralsight.com/guides/web-scraping-with-beautiful-soup
    citation_needed = soup.find_all('a', { "title" : "Wikipedia:Citation needed"})
    return len(citation_needed)

def get_citations_needed_report(soup):
    p_c_n = soup.find_all('p')

    all_pargrapgh=[]
    for every_p in p_c_n:
        p_c = every_p.find('a', { "title" : "Wikipedia:Citation needed"})
        if p_c:
            all_pargrapgh.append(every_p.text)
    return all_pargrapgh
    
    

if __name__ == "__main__":
    
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

    # store the response of page pbject 
    page = requests.get(URL)

    # parsing the html using BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    
    print(get_citations_needed_count(soup))
    print(len(get_citations_needed_report(soup)))