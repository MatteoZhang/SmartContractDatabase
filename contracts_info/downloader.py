import time
import reader_getter


def main():
    filename = 'verified-contractaddress_3.csv'
    extension = 'sol'
    print('Using API: ')

    key = '49T9ZJIGGRNUHG3SP746ZH53R9K7V4T5N1'
    start_time = time.time()
    reader_getter.get_source_code_from_csv(filename, key, extension)

    print("\nEXECUTION TIME --- %s seconds ---\n" % (time.time() - start_time))
    print('\n\nDone.')


if __name__ == '__main__':
    main()
