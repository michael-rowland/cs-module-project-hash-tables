def no_dups(s):
    output_string = ''
    log = set()
    for word in s.split():
        if word not in log:
            log.add(word)
            output_string += f'{word} '
        else:
            pass
    return output_string[:-1]

    # loop over each word
    # check if in set
    # if it is, pass
    # if it isn't, add to set, and append to ouput_string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))