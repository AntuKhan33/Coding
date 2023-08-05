# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements)

    for j in range(size-1):
        
        if elements[j] > elements[j+1]:
            tmp = elements[j]
            print(tmp)
            elements[j] = elements[j+1]
            print(elements[j])
            elements[j+1] = tmp
            
                

        


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    

    bubble_sort(elements) 
    print(elements)