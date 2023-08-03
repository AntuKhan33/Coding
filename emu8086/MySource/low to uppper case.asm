.MODEL SMALL
.STACK 100H
.DATA


MSG1 DB 'ENTER A LOWER CASE LETTER $'
MSG2 DB 0DH,0AH, 'IN UPPER CASE ITS IS: '
CHAR DB ?,'$'

.CODE

MAIN PROC
    
     mov ax,@data
     mov ds,ax
     
     lea dx,msg1
     mov ah,9h 
     int 21h
     
     
     mov ah,1
     int 21h
     sub al,20h
     mov char,al
     
     lea dx,msg2
     mov ah,9
     int 21h
    
    
    
    
    
    
    
    
    
MAIN ENDP
    END MAIN