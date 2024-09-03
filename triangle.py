

def print_triangle(n):
    for i in range(n):
        spaces = " " * (n - i - 1)
        if i == 0: # first line
            print(spaces + "*")
        elif i == n - 1: # last line
            print("* " * n)
        else: # in between lines
            inner_spaces = " " * (2 * i - 1)
            print(f"{spaces}*{inner_spaces}*")

# Example usage
if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the triangle: "))
        if size <= 0:
            print("Please enter a positive integer.")
        elif size == 1: # handle if size is only 1
            print("*")
        else:
            print_triangle(size)
    except ValueError:
        print("Invalid input.")