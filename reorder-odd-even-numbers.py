
def even_odd(n):
    arr = [int(x) for x in str(n)]
    even = []
    odd = []
    for i in arr:
        if (i%2 == 0):
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort(reverse=True)

    result = ''.join(map(str, odd + even))
    print(result)



# Example usage
if __name__ == "__main__":
    try:
        num = int(input("Enter a random number: "))
        even_odd(num)
    except ValueError:
        print("Invalid input.")