import sys
import argparse
from Palindrome import Palindrome

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--palindrome", type=str, required=True, help="Challenge 1 input")
    parser.add_argument("-l", "--longest_palindrome", type=str, required=True, help="Challenge 2 input")
    parser.add_argument("-m", "--min_cut_palindrome", type=str, required=True, help="Challenge 3 input")

    return parser.parse_args()


def main():
    palindrome = Palindrome()
    args        = parse_arguments()

    print(palindrome.check_palindromes(args.palindrome))
    print(palindrome.get_longest_palindrome(args.longest_palindrome))
    print(palindrome.get_minimum_number_cut_palindrome(args.min_cut_palindrome))
    

if __name__ == "__main__":
    sys.exit(main())



