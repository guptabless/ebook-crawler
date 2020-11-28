import requests
from bs4 import BeautifulSoup
import urllib.parse
import bcolors
import sys, argparse

def banner():
    print("""


        ███████╗██████╗░░█████╗░░█████╗░██╗░░██╗░░░░░░░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
        ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
        █████╗░░██████╦╝██║░░██║██║░░██║█████═╝░█████╗██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
        ██╔══╝░░██╔══██╗██║░░██║██║░░██║██╔═██╗░╚════╝██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
        ███████╗██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗░░░░░░╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
        ╚══════╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝                                                                                                                              
                                                                                                        Code By: NG
              """)

if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 't'):
        try:
            input_term = sys.argv[2]
            parser = argparse.ArgumentParser()
            parser.add_argument("-t", required=True)
            print(bcolors.BITALIC + "Testing for available book on pdfdrive.com")
            try:
                Search_term = urllib.parse.quote(input_term)
                print(bcolors.BOLD + 'Entered term for search',Search_term)
                url = 'https://www.pdfdrive.com/search?q=' + Search_term +'&pagecount=&pubyear=&searchin=&em=/'

                input_term_status = requests.get(url,allow_redirects=False).status_code
                print(bcolors.BOLD + 'Status Code of URL after entering serach term',input_term_status)
                if(input_term_status == 200):
                    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
                    source_code_url_ = soup.findAll("div", attrs={"class": "files-new"})
                    for a_href_tag in source_code_url_:
                        fetch_href = a_href_tag.a['href']
                        fetch_url = 'https://pdfdrive.com' + fetch_href
                        print(bcolors.OKMSG + "Most search book on searched term", fetch_url)
                elif (input_term_status == 301):
                    print(bcolors.BOLD + "URL redirected for this term")
                    print(bcolors.BOLD + 'Redirected url', requests.get(url).url)
                    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
                    source_code_url_redirect = soup.findAll("div", attrs={"class": "files-new"})
                    for a_href_tag_redirect in source_code_url_redirect:
                        fetch_href_redirect = a_href_tag_redirect.a['href']
                        fetch_url_redirect = 'https://pdfdrive.com' + fetch_href_redirect
                    print(bcolors.OKMSG + "Most search book on searched term", fetch_url_redirect)
            except:
                print('Try to modify your search as no result found for this search term')
        except:
                print(bcolors.OKMSG + 'Please enter python pdfTerm.py -t < valid search term> ')
    elif (sys.argv[1] != '-t'):
        print(bcolors.OKMSG + 'Please enter -t < valid search term >')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -t ')

