#!/usr/local/bin/python3
'''
Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)

'''
def is_perm_palindrome(t_str):
	flag = {}
	for s in t_str:
		if s == " ":
			continue
		if s.lower() in flag:
			flag[s.lower()] += 1
		else:
			flag[s.lower()] = 1

	# no more than 1 character is not even number
	count = 0
	for k,v in flag.items():
		if v % 2 != 0:
			count += 1
	if count > 1: return False
		
	return True

def main():
	test = "Tact Coa"
	print(is_perm_palindrome(test))

if __name__ == "__main__":
	main()
	
