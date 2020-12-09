import tokenizers
import os

if __name__ == '__main__':
    directory = "smart_contracts"
    for filename in os.listdir(directory):
        if filename.endswith(".sol"):
            print(os.path.join(directory, filename))
            continue
        else:
            continue
