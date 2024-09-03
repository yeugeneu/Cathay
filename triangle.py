

def print_triangle(n):
    for i in range(1, n+1):
        if (i==1): # first line
            print((n-1)* " " + "*") # (n-1) x spaces + '*'
        elif (i == n): # last line
            print("* " * (n-1) + "*") # repeat '* ' n-1 times and add a last '*' at the end 
        else:
            print((n-i) * " " + "*" + ((i-2)*2+1) * " " + "*") 
        

# Example usage
if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the triangle: "))
        if size <= 0:
            print("Please enter a positive integer.")
        elif (n == 1): # if 
            print("*")
        else:
            print_triangle(size)
    except ValueError:
        print("Invalid input.")