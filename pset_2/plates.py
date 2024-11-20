def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers)
    # and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # all vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # numbers cannot be used in the middle of a plate; they must come at the end.
    # for example, AAA222 would be an acceptable _ vanity plate; AAA22A would not be acceptable.
    # the first number used cannot be a '0'
    i = 0 
    while i < len(s):
        if s[1].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    # no periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.', '', '!', '?']:
            return False

    # if we pass all the tests, return true
    return True


main()