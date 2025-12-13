import time

valid_chars = {"g", "y", "n"}
wordlist_file = ['valid-wordle-words.txt']
days = 0

# options
while True:
    print(
        """
        OPTIONS

        [1] Input 3 days worth of Wordle scores (default)
        [2] Input custom amount of days for Wordle scores

        """
    )
    option_input = int(input(": "))
    if (option_input) != 1 and (option_input) != 2:
        continue
    break

if (option_input) == 1:
    days = 3
elif (option_input) == 2:
    days = input("days: ")

for day in range(days):

    # word loader
    def load_wordlist(words):
        if day < 1:
            with open(words, 'rt') as wfile:
                return set(line.strip().lower() for line in wfile)
        else:
            return set(wordlist_file[0])

    # Enter the colored pattern
    while True:
        print(f'\n---- DAY #{day + 1} ----\n')
        your_sw_colored_pattern = input("Enter the colored pattern for the starter word (g = green, y = yellow, n = none): ").lower()
        # your_sw_colored_pattern = "ggggn"
        if len(your_sw_colored_pattern) != 5:
            print("Input must be exactly 5 characters.")
            continue

        if not all(c in valid_chars for c in your_sw_colored_pattern):
            print("Only g, y, or n allowed.")
            continue

        break

    # Enter today's word
    while True:
        todays_word = input("Enter today's word: ").lower()
        # todays_word = "guess"
        if len(todays_word) != 5:
            print("Input must be exactly 5 characters.")
            continue
        break

    # wordle color matching and sorter
    def find_match(colored_spaces, solved_word):
        starter_words = load_wordlist(wordlist_file[0])
        unique_words = sorted(starter_words)
        print(f"\nWordlist({len(unique_words)}): {unique_words}")
        todays_word_letters = list(solved_word)

        for starter_word in starter_words:
            iSpattern = ""
            # print("\n" + starter_word + "\n")
            for iS, iSletter in enumerate(starter_word):
                if iSletter in todays_word_letters:
                    if iSletter == todays_word_letters[iS]:
                        iSpattern += "g"
                        # print(f"GREEN: {iSletter}")
                    elif iSletter != todays_word_letters[iS]:
                        iSpattern += "y"
                        # print(f"YELLOW: {iSletter}")
                else:
                    iSpattern += "n"
                    # print(f"GREY: {iSletter}")
            # print('PATTERN: ' + iSpattern)
            # if iSpattern == colored_spaces:
            #     pass
            # else:
            #     unique_words.remove(starter_word)
            if iSpattern != colored_spaces:
                unique_words.remove(starter_word)
        print(f"\nResult({len(unique_words)}): {unique_words}")
        return unique_words

    current_matches = find_match(your_sw_colored_pattern, todays_word)
    wordlist_file.append(current_matches)
    wordlist_file.pop(0)
    
    time.sleep(1)
print(f'\n possible matches({len(current_matches)}): {current_matches}\n')
        # nsfile.write(f"\n used word list from {wordlist_file}\n pattern is ${your_sw_colored_pattern}")