import crimgDetector as cd
# cool highlighting stuff

def character(g):
    """
    Parameters
    ----------
    g : int
    """
    crimg = "hi {0}".format('boi.')
    return crimg*g

if __name__ == "__main__":
    cd.setInfo(r"$\vartheta$", size=20)
    res = crimg("you")