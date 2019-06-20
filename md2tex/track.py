import sys

def main(argv):
    argv = ["Hello ", argv[0], "!"]
    argv = "".join(argv)
    return argv

if __name__ == "__main__":
    print(main(sys.argv[1:]))
