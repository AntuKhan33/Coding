.MODEL SMALL
.STACK 100H
.DATA
 A DW 2
 B DW 5

.CODE
MAIN PROC

 mov ah,1
 int 21h
  
 
 mov ah,2  
 
 
 
 
 mov dl,al
 int 21h
        
    
     
     
     
     
     
     
     
     
MAIN ENDP 


END MAIN