''' WAP to read a file and
a. Print the total number of characters, words and lines in the file.
b. Calculate the frequency of each character in the file. Use a variable of dictionary
type to maintain the count.
c. Print the words in reverse order.
d. Copy even lines of the file to a file named ‘File1’ and odd lines to another file
named ‘File2’.'''

# a.Print the total number of characters, words and lines in the file.

def count_char_word_line(file):
    with open(file,'r') as f:
        text = f.read()
        #total number of characters 
        print(f'Total number of characters : {len(text)}')
        
        #total number of words
        print(f'Total number of words : {len(text.split())}')
        
        #total number of lines
        print(len(text.split('\n')))
        
count_char_word_line('ques9.txt')

'''b. Calculate the frequency of each character in the file. Use a variable of dictionary
type to maintain the count.'''

def count_char_frequency(file):
    frequency = {}
    
    with open(file,'r') as f:
        text = f.read()
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
                
    return frequency

frequency = count_char_frequency('ques9.txt')
print(frequency)

def reverse_word(file):
    with open(file,'r') as f:
        text = f.read()
        words = text.split()
        reverse = [word[::-1] for word in words]
        print("Reversed words:", " ".join(reverse))
reverse_word('ques9.txt')

'''d. Copy even lines of the file to a file named ‘File1’ and odd lines to another file
named ‘File2’'''

def copy_lines(file):
    with open(file,'r') as f:
        lines = f.readlines()
        
    with open('File1.txt','w') as f1,open('File2.txt','w') as f2:
        for i,line in enumerate(lines,start = 1):
            if i%2 == 0:   
                f1.write(line)
            else:
                f2.write(line)
            
copy_lines('ques9.txt')