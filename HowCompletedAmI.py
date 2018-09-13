# How much reading did I complete? - Python Code #
# Step 1: copy/paste your text into chaptertext.txt
# Step 2: paste a string of where you are in the variable: where_am_i
# Step 3: Run code

# What you should know: 
# reading file_object breaks at end of Book 5!

# Please input where you are in the chapter
where_am_i = "(which in this case includes the implied value of it as an actual function) " 

# Add in your filename (grandscheme.txt or chapter.txt)
filename = 'grandscheme.txt'

file_text = ''

print("\n \n")
with open(filename) as file_object:
    for line in file_object:
        file_text = file_text + line
        # if statement below is used to stop grandscheme.txt
        # when it reaches the end of Book 5
        if "clean async flow control abstraction" in line:
            break    

file_text_length = len(file_text)
reader_location_length = file_text.index(where_am_i)

# Below prints the full text file
# print(file_text)

# Below prints length of text (with spaces)
# FULL BOOK = 1,541,863 characters
# FULL BOOK without ES6 & Beyond = 1,161,791 characters
print("{:,}".format(file_text_length), " characters")

# Below prints the index of where the reader is in the text file
# print(reader_location_length)

percentage_thru = (reader_location_length / file_text_length) * 100
percentage_thru_round = round(percentage_thru,2)

print("")
print(percentage_thru_round, "% of chapter completed")