# Author : Nemuel Wainaina

from colorama import init, Fore
import hashlib
import os
import sys

init()
GREEN = Fore.GREEN
RED = Fore.RED
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

def hash_string(string):
    # return SHA1 hash of the string
    return hashlib.sha1(string.encode()).hexdigest()

def is_correct(word, hash):
    # hash the word and compare it with the hash
    # returns true if they match, otherwise returns false
    if hash_string(word) == hash:
        return True
    else:
        return False

if __name__ == "__main__":
    # check that correct number of arguments are provided
    if len(sys.argv) != 3:
        print(f"{GRAY}Syntax : {sys.argv[0]} _wordlist_ _hash_ {RESET}")
        exit(1)

    # check that the supplied hash is a valid SHA1 hash
    if len(sys.argv[2]) != 40:
        print(f"{RED}[!] Invalid hash provided {RESET}")
        exit(0)
    
    # check that the wordlist file exists
    if not os.path.exists(sys.argv[1]):
        print(f"{RED}[!] The file {sys.argv[1]} does not exist {RESET}")
        exit(0)

    # check that it is actually a file, and not a directory :)
    if not os.path.isfile(sys.argv[1]):
        print(f"{RED}[!] {sys.argv[1]} is not a file {RESET}")
        exit(0)

    with open(sys.argv[1]) as f:
        for word in f.readlines():
            word = word.strip()
            if is_correct(word, sys.argv[2]):
                print(f"{GREEN}[+] Success :: {word} {RESET}")
                break
        else:
            print(f"{GRAY}[-] Correct word not found in the supplied list :( {RESET}")
