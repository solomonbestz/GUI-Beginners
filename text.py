
def solution(string):
    if len(string) == 0: 
        return ''
    print(len(string))

    return string[-1] + solution(string[0:-1])


if __name__=='__main__':
    string = 'solomon'
    print(solution(string))
    # n + solomo
    # no + solom
    # nom + solo
    # nomo + sol
    # nomol + so
    # nomolo + s
    # nomolos
