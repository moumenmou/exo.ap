
unique_words = set()

while True:
    word = input("Enter a word (or type 'exit' to quit): ").strip()


    if word.lower() == 'exit':
        print("Exiting program.")
        break


    if word in unique_words:
        print(f"Duplicate word entered: '{word}'")
        print(f"Count of unique words: {len(unique_words)}")
        break
    else:
       
        unique_words.add(word)

    print(f"Unique words so far: {unique_words}")

