import time


def bubble_sort(list_to_sort):
    cont = True
    while(cont):
        cont = False
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i]>list_to_sort[i+1]:
                list_to_sort[i],list_to_sort[i+1] = list_to_sort[i+1],list_to_sort[i]
                cont = True


if __name__ == '__main__':
    start = time.time()
    a = [8, 5, 12, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17]
    print(a)
    bubble_sort(a)
    print(a)
    end = time.time()
    print(end-start)



