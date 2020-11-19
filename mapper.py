import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    file = open("input.txt", "r", encoding="utf-8")
    f = open("output.txt", "w", encoding="utf-8")
    data = read_input(file)

    for words in data:
        for word in words:
            f.write(f'{word}'+f'{separator}'+'1')
    f.close()

if __name__ == "__main__":
    main()
