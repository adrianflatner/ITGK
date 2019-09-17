def write_to_file(data):
    f = open('default_file.txt','w')
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename,'r')
    innhold = f.read()
    f.close()
    return innhold

def main():
    r_or_w = 0
    while r_or_w != 'done':
        r_or_w = input("Do you want to read or write? ")
        if r_or_w == 'write':
            write_to_file(input("What do you want to write? "))
        elif r_or_w == 'read':
            print(read_from_file('default_file.txt'))

main()
