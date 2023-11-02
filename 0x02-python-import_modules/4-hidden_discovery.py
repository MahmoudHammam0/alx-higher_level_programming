#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    g = dir(hidden_4)
    for x in g:
        for h in x:
            if h == '_':
                break
            else:
                print(x)
                break
