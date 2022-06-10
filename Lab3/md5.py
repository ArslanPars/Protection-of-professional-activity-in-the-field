import hashlib

global result


def crack_md5(wordlist, pass_hash):
    flag = 0
    attempts = 0

    try:
        pass_file = open(wordlist, 'r')
    except Exception as e:
        print("No File Found!")
        quit()

    print("Attempting to Crack Password Hash...")
    print("Please wait for a while!")

    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()

        attempts += 1

        if digest == pass_hash:
            global result
            result = word
            print(f"Password Found : {word}")
            print(f"Total Attempts to Crack MD5 Hash: {attempts}")
            flag = 1
            break

    if flag == 0:
        print("[-] Sorry! Unable to find correct password :(")
        print(f"Total Attempts to Crack MD5 Hash: {attempts}\n")


def save_result(pass_hash, result, file_name):
    if result == "":
        failed_result = f"MD5 Hash : {pass_hash}\nResult : Password Not Found in Wordlist"
        with open(file_name, 'w') as f:
            f.write(failed_result)

    else:
        cracked_result = f"MD5 Hash : {pass_hash}\nCracked Password : " + result
        with open(file_name, 'w') as f:
            f.write(cracked_result)


if __name__ == '__main__':
    pass_hash = input('Enter a MD5 hash: ')
    word_list = input('Enter a wordlist location: ')
    output_file_name = input('Enter output file location: ')

    words = open(word_list, "r")
    output_file = open(output_file_name, 'w')

    crack_md5(word_list, pass_hash)
    save_result(pass_hash, result, output_file_name)
