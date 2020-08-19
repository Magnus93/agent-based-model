

def sec_to_str(seconds):
    m = int(seconds//60)
    s = int(seconds%60)
    if m == 0:
        return "{} s".format(s)
    else:
        return "{} min {} s".format(m, s)

        