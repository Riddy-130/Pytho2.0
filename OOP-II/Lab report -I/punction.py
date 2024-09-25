import string

def remove_punctuation(input_string):
   
    translator = str.maketrans('', '', string.punctuation)
   
    return input_string.translate(translator)

my_string = "Hello!!!, he said ---and went."
clean_string = remove_punctuation(my_string)
print(clean_string)
