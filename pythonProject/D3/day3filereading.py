longest_words = []

infile = open("day3input.txt")
for line in infile:
    line = line.rstrip(".\n")

    line_words = line.split() #crrates a list of words in seperate ""
    word_count = len(line_words)

    longest_word = ""
    for word in line_words:
        if len(word) > len(longest_word):
            longest_word = word

    longest_words.append(longest_word)
    print(f"{line} - {word_count} words - longest word is {longest_word}")

longest_words.sort()
print(longest_words)
infile.close()

s = "pack my box boy"
s_words = s.split()
# splits sentence into seperate words.
print(s_words)

outfile = open("output.txt", "w")

for word in longest_words:
    print(word, file=outfile)
    # prints out one word per line

outfile.close() #creates file called output.txt

                        ### tutors method ###

# create an empty list to hold the longest words
longest_words = []

# open the input file
infile = open("input.txt")

# read each line from the file
for line in infile:
    # take the carriage returns and full stops from the ends of the lines
    line = line.rstrip(".\n")

    # split the line into separate words
    line_words = line.split()
    # find out how many words are in the line
    word_count = len(line_words)

    # find the longest word
    longest_word = ""
    for word in line_words:
        if len(word) > len(longest_word):
            longest_word = word

    # add the longest word to the list
    longest_words.append(longest_word)

    # display output
    print(f"{line} - {word_count} words - longest word is {longest_word}")

# sort the list of longest words and display it
longest_words.sort()
print(longest_words)

# close the input file
infile.close()

# open the output file for writing
outfile = open("output.txt", "w")

# write the longest words out to the file
for word in longest_words:
    print(word, file=outfile)

# close the output file
outfile.close()
