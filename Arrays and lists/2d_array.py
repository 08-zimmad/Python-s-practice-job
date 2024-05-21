arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def Initialize_array():

    rows= int(input("Enter Number of rows"))
    cols=int(input("Enter Number of columns"))

    arr=[]
    for i in range(cols): # int object not t
        row=list(map(int,input("Enter values with giving space").split()))
        if len(row)!=cols:
            print("Error")
        arr.append(row)
    print(arr)


def init_0_in_2d():
    return [[0 for _ in range(3)] for _ in range(3)]



def sum_of_each_row():
    for row in range(len(arr)):
        print(sum(arr[row]))



if __name__=="__main__":
    sum_of_each_row()