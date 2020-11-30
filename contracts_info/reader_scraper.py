import requests
import os
import csv
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup


_fold=os.getcwd()+os.sep+'reader_scraper_data'


def scrape_from_bigquery_csv(filename, extension):
    global _fold
    address_li=[]
    line_count = 0
    if not os.path.isdir(_fold):
            os.makedirs(_fold)
    with open(filename) as csv_file:
        csvr = csv.reader(csv_file)
        for row in csvr:
            if line_count == 0: #the first line is a note
                print(f'\nStarting to read {filename}')
            else:
                filename=row[0]+"."+extension
                loc=_fold+os.sep+filename
                if os.path.isfile(loc):
                    continue
                else:
                    address_li.append(row[0])
                    if len(address_li)==100:
                        scrape_threader(address_li, extension)
                        address_li=[]
            line_count += 1
            print("\rContracts analyzed - {:.8f}%".format((line_count / 20467002) * 100), end=" ")
    print(f'Processed {line_count-1} contracts.')    


def scrape_threader(address_list, extension):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for addr in address_list:
            executor.submit(scrape_code, addr, extension)


def scrape_code(addr, extension):
    url='https://etherscan.io/address/'+addr+'#code'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, timeout = 50, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, "lxml")
    demo = soup.findAll("span", {"class":"font-weight-normal text-secondary"})
    if len(demo)==0: #check if source code is available
        return
    if str(demo).find("Multiple") != -1: #checks if source code is cointained in multiple files
        return
    pre = soup.find("pre", id="editor")
    text = str(pre)
    begin = text.find("/**")
    end = text.find("</pre>")
    source_code=text[begin : end]
    filename=addr+"."+extension
    loc=_fold+os.sep+filename
    f = open(loc, "w", encoding = "utf-8")
    f.write(source_code)
    f.close
