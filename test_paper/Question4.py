def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print("Error: The file does not exist.")
        return None

data = read_file("C:\\Users\\RCAT\\Desktop\\priyanshu singh\\test_paper\\test0001.txt")
if data is not None:
    print(data)

# output :
# my name is priyanshu singh