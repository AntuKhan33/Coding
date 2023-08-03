.MODEL SMALL
.STACK 100H
.CODE
main proc
    
    mov ah,1
    int 21h
    
    
cmp al,1
je odd
cmp al,3
je odd


cmp al,2
je even
cmp al,4
je even   

odd:
mov ah,2
mov dl,"o"
int 21h 
jmp exit
even:

mov ah,2
mov dl,"e"
int 21h

exit:
mov ah,4ch 
int 21h

