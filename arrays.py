# Array Reverse

A = [1, 2, 3, 4, 5]
N = 5

for k in range(N // 2):
  A[k], A[N-1-k] = A[N-1-k], A[k]
  
print(A)


# Cyclic shift

## left
tmp = A[0]

for k in range(N - 1):
  A[k] = A[k+1]
  
A[N-1] = tmp

## right
tmp = A[N-1]

for k in range(N - 2, -1, -1):
  A[k+1] = A[k]
  
A[0] = tmp


# List comprehensions

A = [x**2 for x in range(10)]
# >> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Create an array B with even elements of A squared:

A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

B = [x**2 for x in A if x%2 == 0]
# >> [4, 16, 36, 64]

## if negative, write 0
B = [(0 if x <0 else x**2) for x in A if x%2 == 0]
# >> [0, 16, 36, 64]

# Array Sorting

def insert_sort(A):
    ''' сортировка списка А вставками '''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    ''' сортировка списка А выбором '''
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    ''' сортировка списка А пузырьковым методом '''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
            
def test_sort(sort_algorithm):
    print ("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print ("Ok" if A == A_sorted else "Fail")
    
    print ("testcase #2: ", end="") 
    A = list(range(10, 20)) + list(range (0, 10))
    A_sorted = list(range(20)) 
    sort_algorithm(A) 
    print("Ok" if A == A_sorted else "Fail")
    
    print ("testcase #3: ", end="") 
    A = [4, 2, 4, 2, 1] 
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A) 
    print("Ok\n" if A == A_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)

