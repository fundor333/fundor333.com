import os

def post_fc():
    year = input("Give me the Year\n")
    name = input("Give me the title\n")
    os.system(f"hugo new post/{year}/{name.replace(' ','-')}/index.md")

def quiet_fc():
    print("Make a quiet")
    name = input("Give me the title\n")
    os.system(f"hugo new quiet/{name}.md")

ANSWER= {"post": post_fc,
        "quiet":quiet_fc}

def main_checker():
    text = input("You need a new [post] or a new [quiet]\n")  # Python 3

    ANSWER.get(text, main_checker)()
    

if __name__ == "__main__":
    main_checker()

