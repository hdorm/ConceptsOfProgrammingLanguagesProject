from Scanner import *

# Sets i equal to 0 and calls for the scanner to ask for input and split the lines into words
# We then call another function which removes the comments from the list as we don't need them
i = 0
new_list = name_and_split()
no_comments_list = delete_comments(new_list)

# Token codes
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


# Function which checks if a lexeme is a keyword
# We go to the identifier function if the lexeme is not a keyword
# We print the lexeme and its token code if it is a keyword
def keyword():
    # Calls the global i variable, so we can use it in the function
    global i
    print("Entering <keywords>")
    if not is_keyword(i, no_comments_list):
        identifier()
    elif is_keyword(i, no_comments_list):
        if is_identifier(i, no_comments_list):
            identifier()
        elif not is_identifier(i, no_comments_list):
            print("Next token is:", keyword_token, "Next lexeme is:", next_token(i, no_comments_list))
    print("Exiting <keywords>")


# Function which checks if a lexeme is an identifier
# We go to the operator function if the lexeme is not an identifier
# We print the lexeme and its token code if it is an identifier
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
    print("Exiting <identifiers>")


# Function which checks if a lexeme is an operator
# We go back to the while loop if the lexeme is not an operator
# We print the lexeme, its token code, and the constant's lexeme and token code if it is an operator
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
    print("Exiting <operators>")


# Loop that keeps the program going until the list has gone through completely
while i < len(no_comments_list):
    keyword()
    i = i + 1
