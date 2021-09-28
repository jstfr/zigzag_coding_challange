import sys

class Palindrome:  

    #Function check if string is a palindrome
    def check_palindromes(self, palindromes):
        """"Level 1 Challenge """
        #Check if not empty string
        if palindromes:

            #remove first all the white space
            palindromes = palindromes.replace(" ", "")

            #Check each letter at the same time between first letter and last letter
            #if first and last letter are the same. then check the rest start and end
            forward     = 0
            backward    = len(palindromes) - 1
            while (backward > forward):
                
                forwardChar     = palindromes[forward]
                backwardChar    = palindromes[backward]                
                forward         = forward + 1
                backward        = backward - 1

                #If any letter from the start and end that is not the same then it is not palindrome
                if forwardChar != backwardChar:
                    return "False, it's not written the same forward and backward"

            return "True, it's written the same forward and backward"

        else:
            return "Error: No palindrome entered!"
    
    # Function get the longest palindromic substrings of a given string
    def get_longest_palindrome(self, palindromes):
        """"Level 2 Challenge """

        #Check if not empty string
        if palindromes:

            #remove first all the white space
            palindromes = palindromes.replace(" ", "")

            # set an empty array to store all the palindromic substring
            array = set()
        
            for i in range(len(palindromes)):
        
                # find all odd length palindrome with palindromes[i] as a midpoint
                self.expand(palindromes, i, i, array)
        
                # find all even length palindrome with palindromes[i] and palindromes[i+1]
                # as its midpoints
                self.expand(palindromes, i, i + 1, array)
        
            
            longest_palindrome = ""
            for palindrome in array:

                #check all the store palindromic substring in array by comparing the length of each
                #once determine then store to longest_palindrome variable
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome

        else:
            return "Error: No palindrome entered!"
        
        return longest_palindrome

    # Expand in both directions of start and end to find all palindromes
    def expand(self, palindromes, start, end, array):
    
        # run till is not a palindrome
        while start >= 0 and end < len(palindromes) and palindromes[start] == palindromes[end]:
    
            # store all palindrome in array
            array.add(palindromes[start: end + 1])
    
            # Expand in both directions
            start   = start - 1
            end     = end + 1

    # Function get the minimum palindromic cuts
    def get_minimum_number_cut_palindrome(self, palindromes):
        """"Level 3 Challenge """
        return self.find_minimum_cut(palindromes, 0, (len(palindromes) -1))

    def find_minimum_cut(self, palindromes, start, end):

        #Check if value itself is already a palindrome to just return 0
        if start == end or self.is_palindrome(palindromes, start, end):
            return 0
        
        #Set min as variable for maximum size
        min = sys.maxsize

        for i in range(start, end):

            # find all odd length palindrome with palindromes[i] as a midpoint
            # find all even length palindrome with palindromes[i] and palindromes[i+1]
            # as its midpoints
            count = 1 + self.find_minimum_cut(palindromes, start, i) + self.find_minimum_cut(palindromes, i + 1, end)

            # Change the value of min if the count is less than the min 
            if count < min:
                min = count
        
        return min
    

    def is_palindrome(self, palindromes, start, end):
        
        #Check each letter at the same time between first letter and last letter
        #if first and last letter are the same. then check the rest start and end
        while start <= end:
            if palindromes[start] != palindromes[end]:
                return False
            
            start   = start + 1
            end     = end - 1
        return True