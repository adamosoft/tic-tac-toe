
def load_config(path: str):
    """
    Returns dict of game attributes
    """
    with open(path, "r") as conf:
        config = {}
        for line in conf.read().split("\n"):
            attr = line.split(":")
            config[attr[0]] = attr[1]

    return config
