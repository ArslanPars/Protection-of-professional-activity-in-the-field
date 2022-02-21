import hashlib
import time


def main():
    counter = 1

    hashed_string = input('Enter a SHA256 hash: ')
    word_list = input('Enter a wordlist input file name: ')
    output_file = input('Enter output file name:')

    try:
        words = open(word_list, "r")
        output_file = open(output_file, 'w')
    except:
        print("\n File Not Found")
        quit()

    for word in words:
        calculated_hash = hashlib.sha256(word.strip().encode('utf-8')).hexdigest()

        print('Trying password %d: %s ' % (counter, word.strip()))
        output_file.write('Trying word %d: %s ' % (counter, word.strip()))
        output_file.write('\nPossible word hash: %s ' % calculated_hash)
        output_file.write('\nActual hash: %s ' % hashed_string)
        output_file.write('\n-------------------------------\n')

        counter += 1

        if calculated_hash == hashed_string:
            print('\nPassword was found - password is: %s ' % word)
            break

    else:
        print('\nPassword not found')
        print('Try another wordlist file or SHA256 hash')


if __name__ == '__main__':
    main()
