def print_framed_word(word):
    frame_width = 30
    word_length = len(word)
    
    
    left_padding = (frame_width - word_length) // 2
    
 
    print("*" * frame_width)  # Top border
    print("*" + " " * (frame_width - 2) + "*")  # Empty line with borders
    print("*" + " " * left_padding + word + " " * (frame_width - left_padding - word_length - 2) + "*")  # Line with the word in the center
    print("*" + " " * (frame_width - 2) + "*")  # Empty line with borders
    print("*" * frame_width)  # Bottom border


word = input("Word: ")
print_framed_word(word)
