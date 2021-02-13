##### Question 1
##### Write a program that prints the following pattern for a given input n containing numbers from 1 to n.

# Step 1: Declare input number
n = int(input('Please input number: '))
print('')

# Step 2: Define function to create given matrix contains number from 1 to n
def MatrixN(n):
    ln = 2*n - 1 #number of rows of expected matrix
    ar = [0]*ln #ar is an array of zeros at the beginning
    x = 0
    for i in range(ln): #loop ln times to print ln lines
        string = ''
        if x < n:
            for j in range(x, ln - x): #to navigate what component will be updated in ar
                ar[j] = ar[j] + 1 #update each component of ar in given range by adding 1 unit
        if x >= n:
            for j in range(ln - x, x):
                ar[j] = ar[j] - 1 #update each component of ar in given range by subtracting 1 unit

        for k in range(ln):
            if k != ln-1:
                string = string + str(ar[k]) + ' ' #create string to concatenate components of ar in each loop
            else:
                string = string + str(ar[k]) + ''

        x = x + 1 #increase x value by 1 in each loop

        print(string) #print string in each loop

# Step 3: Test
MatrixN(n)



