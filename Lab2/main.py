import hashlib
from joblib import Parallel, delayed

is_word_found = False

def main():
    hashed_string = input('Enter a SHA-256 hash: ')
    word_list = input('Enter a wordlist location: ')
    threads_count = int(input('Enter a count of processes: '))

    try:
        words = open(word_list, "r")
    except:
        print("\n File Not Found")
        quit()

    Parallel(n_jobs=threads_count)(delayed(search_hash)(hashed_string, words, threads_count, i) for i in range(0, threads_count))
    if not is_word_found:
        print('\nPassword Not Found\nTry Another Dictionary')


def search_hash(hashed_string, words, threads_count, value):
    count_words = len(words)/threads_count

    for word in words[value:value+count_words]:
        calculated_hash = hashlib.sha256(word.strip().encode('utf-8')).hexdigest()
        if calculated_hash == hashed_string:
            print('\nPassword Found & Password Is: %s ' % word)
            is_word_found = True
            break
        
        
if __name__ == '__main__':
    main()
