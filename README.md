|Base |   Title                | Description       |
|-------------------|------------------------|-------------------|
| Home | Non-Unique Elements    | You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3]. 
| --- | Median                 | A median is a numerical value separating the upper half of a sorted array of numbers from the lower half. In a list where there are an odd number of entities, the median is the number found in the middle of the array. If the array contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle. For this mission, you are given a non-empty array of natural numbers (X). With it, you must separate the upper half of the numbers from the lower half and find the median. 
| --- | House Password | Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits |
| --- | Count-Neighbours      |   You are given a state for a rectangular board game grid with chips in a binary matrix, where 1 is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell in the form of row and column numbers (starting from 0). You should determine how many chips are close to this cell. Every cell interacts with its eight neighbours; those cells that are horizontally, vertically, or diagonally adjacent. |
| --- | The Most Wanted Letter |  You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case. While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters. If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e". |
| Elementary | Fizz-Buzz | You should write a function that will receive a positive integer and return: "Fizz Buzz" if the number is divisible by 3 and by 5; "Fizz" if the number is divisible by 3; "Buzz" if the number is divisible by 5; The number as a string for other cases.|
| --- | Index Power | You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0. |
| --- | Even Last | You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0. |
| --- | Monkey Typing | You are given some text potentially including sensible words. You should count how many words are included in the given text. A word should be whole and may be a part of other word. Text letter case does not matter. Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be counted only once. |
| --- | Secret Message |  Ever tried to send a secret message to someone without using the postal service? You could use newspapers to tell your secret. Even if someone finds your message, it’s easy to brush them off and that its paranoia and a bogus conspiracy theory. One of the simplest ways to hide a secret message is to use capital letters. Let's find some of these secret messages. You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text. |
| --- | Three Words | You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession. |
| --- |  Most Numbers |You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0. |
| --- | Boolean Algebra | <ul> <li>conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise. </li> <li> "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise. </li> <li> "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true. </li> <li> "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0. </li> <li> "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value. </li></ul> |
| --- | Digits Multiplication |  You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes. For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes). |
| --- | Count Inversions |  In computer science and discrete mathematics, an inversion is a pair of places in a sequence where the elements in these places are out of their natural order. So, if we use ascending order for a group of numbers, then an inversion is when larger numbers appear before lower number in a sequence. Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions - 5 and 3; - 5 and 4; - 7 and 6. |
| --- | Days Between |  How old are you in number of days? It's easy to calculate - just subtract your birthday from today. We could make this a real challenge though and count the difference between any dates. You are given two dates as tuples with three numbers - year, month and day. For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about absolute value. |
| --- | Pangram | A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a sentence using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram "The quick brown fox jumps over the lazy dog". |
| --- | Binary Count |  You are given a number (a positive integer). You should convert it to the binary format and count how many unities (1) are in the number spelling. For example: 5 = 0b101 contains two unities, so the answer is 2. |
| --- | Common Words |  Let's continue examining words. You are given two string with words separated by commas. Try to find what is common between these strings. The words are not repeated in the same string. Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order. |
| --- | Absolute Sorting | The array (a tuple) has various numbers. You should sort it, but sort it by absolute value in ascending order. For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20). Your function should return the sorted list or tuple. |
| Electronic Station | Brackets | You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands. |
| --- | Weak Point | The durability map is represented as a matrix with digits. Each number is the durability measurement for the cell. To find the weakest point we should find the weakest row and column. The weakest point is placed in the intersection of these rows and columns. Row (column) durability is a sum of cell durability in that row (column). You should find coordinates of the weakest point (row and column). The first row (column) is 0th row (column). If a section has several equal weak points, then choose the top left point. |
| --- | The Hamming Distance |  The Hamming distance between two binary integers is the number of bit positions that differs. You are given two positive numbers (N, M) in decimal form. You should calculate the Hamming distance between these two numbers in binary form. |
| --- | Restricted Sum | Our new calculator is censored and as such it does not accept certain words. You should try to trick by writing a program to calculate the sum of numbers. Given a list of numbers, you should find the sum of these numbers. Your solution should not contain any of the banned words, even as a part of another word. The list of banned words are as follows: sum, import, for, while, reduce |
| --- | Find Sequence | You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals). |
| --- | Vigenere Cipher |  The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution. In the Vigenère cipher each letter of a message is shifted along some number of places with different shift values. To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square, or Vigenère table. It consists of the alphabet written out 26 times in different rows, each version of the alphabet is shifted cyclically to the left compared to the previous alphabet. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword. |
| Scientific Expedition | Verify Anagrams | An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Two words are anagrams to each other if we can get one from another by rearranging the letters. Anagrams are case-insensitive and don't take account whitespaces. For example: "Gram Ring Mop" and "Programming" are anagrams. But "Hello" and "Ole Oh" are not. |
| --- | Matrix Transpose | You have been given a matrix as a 2D list with integers. Your task is to return a transposed matrix based on input. |
| --- | Morse Code | Help Stephen to create a module for converting a normal time string to a morse time string. As you can see in the illustration, a gray circle means on, while a white circle means off. Every digit in the time string contains a different number of slots. The first digit for the hours has a length of 2 while the second digit for the hour has a length of 4. The first digits for the minutes and seconds have a length of 3 while the second digits for the minutes and seconds have a length of 4. Every digit in the time is converted to binary representation. You will convert every on (or 1) signal to dash ("-") and every off (or 0) signal to dot ("."). |
| Ice Base | Funny Addition | We have an array of two positive integers. Add these two numbers together. |
| --- | Simple Areas | You should write a function to calculate the area of simple figures: circles, rectangles and triangles. You are give an arbitrary number of arguments and depending on this, the function calculates area for the different figures. |
| --- | The Greates Common Divisor | You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers. |
| Incinerator | Bird Langauge | You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable. |
















