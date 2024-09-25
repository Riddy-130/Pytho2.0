def find_substring_occurrences(main_string, substring):
    
    indices = []
    
    start = 0

    while start < len(main_string):
        
        index = main_string.find(substring, start)
        if index == -1:
            
            break
        
        indices.append(index)
        
        start = index + 1

    return indices


main_string = "This is a test string. This test is for testing."
substring = "test"
occurrences = find_substring_occurrences(main_string, substring)
print(f'The substring "{substring}" occurs at indices: {occurrences}')
