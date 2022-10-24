# This program takes as input a file name with extension "scl" and scans it for keywords, operators and identifiers
# of the language.

import json

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
ref_identifiers = ["define", "symbol"]
found_identifiers = []


def name_and_split():
    # user inputs filename
    file_name = input("Type in the name of the file with the extension: ")

    # print space for formatting
    print("")

    # open file
    f = open(file_name, "r")

    about_me = f.read().split()

    # read it and split the lines into words
    return about_me


def delete_comments(about_me):
    i = 0
    new_list = []
    while i < len(about_me):
        if about_me[i].lower() == "description":
            new_list.append(about_me[i])
            while about_me[i].lower() != "*/":
                i = i + 1
            i = i + 1
        else:
            new_list.append(about_me[i])
            i = i + 1
    return new_list


def next_token(i, about_me):
    next_lexeme = about_me[i].lower()
    return next_lexeme


def is_keyword(i, about_me):
    if about_me[i].upper() in ref_keyword:
        return True
    elif about_me[i].upper() not in ref_keyword:
        return False


def is_operand(i, about_me):
    if about_me[i].upper() in ref_operators:
        return True
    elif about_me[i].upper() not in ref_operators:
        return False


def is_identifier(i, about_me):
    if about_me[i].lower() in ref_identifiers:
        found_identifiers.append(about_me[i + 1].lower())
        return True
    elif about_me[i - 1].lower() in ref_identifiers:
        found_identifiers.append(about_me[i].lower())
        return True
    elif about_me[i].lower() in found_identifiers:
        return True
    elif about_me[i].lower() not in ref_identifiers:
        return False
