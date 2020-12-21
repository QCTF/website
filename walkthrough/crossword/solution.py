def read_all_words():
    with open('words.txt') as file:
        return [
            line.strip()
            for line in file
        ]

words = read_all_words()

def word_matches_schema(schema, word):
    '''
    schema looks like '##ah'
    word looks like 'yeah'
    '''
    return (
        len(schema)==len(word) and
        all(
            schema_character in ['#', word_character]
            for schema_character,word_character in zip(schema,word)
        )
    )

def possible_words(schema):
    return (
        word
        for word in words
        if word_matches_schema(schema,word)
    )

'''
    #a#######
s   #  #  # #
##s##  r  # #
#   ##########
#   #  #  # #
###t##i######
    s  #  t g
    e  #
       #

one_across: #a#######
one_down: ######se
two_down: ##r######
three_down: ######t
four_down: ######g
five_down: s####
six_across: ##s##
seven_across: ##########
eight_across: ###t##i######
'''

def solve():
    for eight_across in possible_words('###t##i######'):
        for one_down in possible_words(f'#####{eight_across[4]}se'):
            for two_down in possible_words(f'##r##{eight_across[7]}###'):
                for one_across in possible_words(f'{one_down[0]}a#{two_down[0]}#####'):
                    for seven_across in possible_words(f'{one_down[3]}##{two_down[3]}######'):
                        for three_down in possible_words(f'{one_across[-3]}##{seven_across[-4]}#{eight_across[-3]}t'):
                            for four_down in possible_words(f'{one_across[-1]}##{seven_across[-2]}#{eight_across[-1]}g'):
                                for six_across in possible_words(f'##s#{one_down[2]}'):
                                    for five_down in possible_words(f's{six_across[0]}##{eight_across[0]}'):
                                        return [
                                            one_across, one_down,
                                            two_down, three_down,
                                            four_down, five_down,
                                            six_across, seven_across, eight_across
                                        ]

solution = solve()
print(solution)

