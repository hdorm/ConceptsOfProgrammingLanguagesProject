# This program takes as input a file name with extension "scl" and scans it for keywords, operators and identifiers
# of the language.

import json


def main():
    # list of keywords that are in the scl language
    ref_keyword = ["IMPORT", "USE", "LANGB", "RANGB", "QUOTES", "IDENTIFIER", "FSHASH", "BSLASH", "SYMBOL", "STRING",
                   "UNSIGNICON", "SIGNICON", "HCON", "FCON", "FORWARD", "INTERFACE", "STRUCT", "STRUCTYPE",
                   "DEFINETYPE", "MEXTERN", "FUNCTION", "MAIN", "RETURN", "POINTER", "OF", "ARRAY", "LB", "RB", "TYPE",
                   "MVOID", "COUNT", "INTEGER", "SHORT", "REAL", "FLOAT", "DOUBLE", "TBOOL", "CHAR", "TSTRING",
                   "LENGTH", "TBYTE", "ENUM", "SPECIFICATIONS", "DESCRIPTION", "GLOBAL", "DECLARATIONS", "CONSTANTS",
                   "VARIABLES", "DEFINE", "PERSISTENT", "SHARED", "STATIC", "MFILE", "TUNSIGNED", "LONG", "VALUE",
                   "EQUOP", "COMMA", "IMPLEMENTATIONS", "IS", "PBEGIN", "ENDFUN", "PRECONDITION", "OR", "AND", "NOT",
                   "LP", "RP", "RELOP", "EQOP", "MTRUE", "MFALSE", "EQUALS", "GREATERT", "LESST", "EQUAL", "PARAMETERS",
                   "ALTERS", "PRESERVES", "PRODUCES", "CONSUMES", "PLUS", "MINUS", "BAND", "BOR", "BXOR", "STAR",
                   "DIVOP", "MOD", "LSHIFT", "RSHIFT", "ADDRESS", "DEREF", "NEGATE", "LETTER", "ADD", "TO", "SUBTRACT",
                   "FROM", "SET", "READ", "INPUT", "DISPLAY", "DISPLAYN", "MCLOSE", "MOPEN", "INCREMENT", "DECREMENT",
                   "CALL", "IF", "THEN", "ENDIF", "FOR", "DO", "ENDFOR", "REPEAT", "UNTIL", "ENDREPEAT", "WHILE",
                   "ENDWHILE", "CASE", "MENDCASE", "MBREAK", "MEXIT", "POSTCONDITION", "ELSEIF", "DOWNTO", "USING",
                   "MWHEN", "COLON", "DEFAULT", "ELSE", "OUTPUT", "WRITE", "DOT"]

    # list of operators that are in the scl language
    ref_operators = ["+", "-", "/", "*", "**", "=", ">", "<", "^= *", "Â¬= *", ">= **", "<= **", "<>", "><", "||", "&",
                     "|", "Â¬ *", "^ *", "~ *", "AND ", "OR", "NOT", "IN", ":"]

    # list of identifiers that are in the scl language

    ref_identifiers = ["identifier"]

    # lists to hold the values

    keywords = [""]

    operators = [""]

    identifiers = [""]

    complete_list = [""]

    # user inputs filename

    file_name = input("Type in the name of the file with the extension: ")

    # print space for formatting

    print("")

    # open file

    f = open(file_name, "r")

    # read it and split the lines into words

    about_me = f.read().split()

    # Scans for keywords, operators, and identifiers then adds them to the matching lists
    i = 0
    while i < len(about_me):

        if about_me[i].lower() == "description":
            keywords.append(about_me[i])
            complete_list.append(about_me[i])
            while about_me[i].lower() != "*/":
                i = i + 1
            i = i + 1

        elif about_me[i].lower() == "define":
            keywords.append(about_me[i])
            complete_list.append(about_me[i])
            identifiers.append(about_me[i + 1])
            complete_list.append(about_me[i + 1])
            i = i + 2

        elif about_me[i].upper() in ref_keyword:
            keywords.append(about_me[i])
            complete_list.append(about_me[i])
            i = i + 1

        elif about_me[i].upper() in ref_operators:
            operators.append(about_me[i])
            complete_list.append(about_me[i])
            i = i + 1

        else:
            i = i + 1

        # close the file

    f.close()

    # print the keywords to the screen

    print("______________keywords______________")

    for i in range(len(keywords)):
        print(keywords[i])
        print("")

    # print the identifiers to the screen

    print("______________identifiers______________ ")

    for i in range(len(identifiers)):
        print(identifiers[i])
        print("")

    # print the operators to the screen

    print("______________operators______________ ")

    for i in range(len(operators)):
        print(operators[i])

    print("______________complete list______________ ")

    for i in range(len(complete_list)):
        print(complete_list[i])

    keywords.extend(identifiers)
    keywords.extend(operators)

    with open(f'{file_name}' + '.json', 'w') as outfile:
        json.dump(keywords, outfile, indent=2)


if __name__ == "__main__":
    main()
