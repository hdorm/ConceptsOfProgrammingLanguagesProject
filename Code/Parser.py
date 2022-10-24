from Scanner import *

i = 0
new_list = name_and_split()
no_comments_list = delete_comments(new_list)

# token codes
plus_token = 1
minus_token = 2
divide_token = 3
multiply_token = 4
equal_token = 6
greater_than_token = 7
less_than_token = 8
identifier_token = 26
keyword_token = 27
constant_token = 28


def keyword():
    global i
    print("Entering <keywords>")
    if not is_keyword(i, no_comments_list):
        identifier()
    elif is_keyword(i, no_comments_list):
        if is_identifier(i, no_comments_list):
            identifier()
        elif not is_identifier(i, no_comments_list):
            print("Next token is:", keyword_token, "Next lexeme is:", next_token(i, no_comments_list))


def identifier():
    global i
    print("Entering <identifiers>")
    if is_identifier(i, no_comments_list):
        if next_token(i, no_comments_list).lower in ref_identifiers:
            print("Next token is:", keyword_token, "Next lexeme is:", next_token(i, no_comments_list))
        else:
            print("Next token is:", identifier_token, "Next lexeme is:", next_token(i, no_comments_list))
    else:
        operator()


def operator():
    global i
    print("Entering <operators>")
    if not is_operand(i, no_comments_list):
        return
    elif is_operand(i, no_comments_list):
        print("Next token is:", ref_operators.index(next_token(i, no_comments_list)), "Next lexeme is:",
              next_token(i, no_comments_list))
        print("Next token is:", constant_token, "Next lexeme is:",
              next_token(i + 1, no_comments_list))


while i < len(no_comments_list):
    keyword()
    i = i + 1
