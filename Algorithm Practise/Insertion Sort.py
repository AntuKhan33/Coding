

from xml.dom.minidom import Element
from pandas import array


def insertation_sort(elemnets):
    for i in range(1,len(elemnets)):
        key=elemnets[i]
        j=i-1
        
        while j>=0 and key<elemnets[j]:
            elemnets[j+1],elemnets[j]=elemnets[j],elemnets[j+1]
            
            j=j-1
            
        
        
elements=[9,5,1,4,3]
insertation_sort(elements)
print(elements)