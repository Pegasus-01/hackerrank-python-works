##Task
##The provided code stub reads and integer,n , from STDIN. Print Half pyramid pattern with number of rows <=n

n=int(input("Enter the number of rows"))
for row in range(1, n+1):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
