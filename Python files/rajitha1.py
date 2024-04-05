n = int(input()) # take user input 

if n > 0 and (n & (n - 1)) == 0:  # it checks the if n is pow of two.
    print("True")
else:
    print("False")
