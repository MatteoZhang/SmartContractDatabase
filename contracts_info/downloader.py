import time
import reader_getter
import reader_scraper


def main():
    filename = 'verified-contractaddress.csv'
    extension = 'sol'
    mode = input('Scraper or API? [S/A]: ')
    if mode == 'S':
        start_time = time.time()
        reader_scraper.scrape_from_bigquery_csv(filename, extension)
    elif mode == 'A':
        key = '49T9ZJIGGRNUHG3SP746ZH53R9K7V4T5N1'
        start_time = time.time()
        reader_getter.get_source_code_from_bigquery_csv(filename, key, extension)
    else:
        print('Select a valid response [S/A].')
        return
    print("\nEXECUTION TIME --- %s seconds ---\n" % (time.time() - start_time))
    print('\n\nDone.')


if __name__ == '__main__':
    main()
