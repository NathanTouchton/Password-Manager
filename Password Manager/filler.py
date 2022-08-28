try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")