.model small
.data
m1 db "vowel$"
m2 db "constant$"
.code
  main proc
    mov ax,@data
    mov ds,ax
    
mov ah,1
int 21h

cmp al,"a"
je level1:
cmp al,"e"
je level1
cmp al,"i"
je level1

cmp al ,"o"
je level1

cmp al,"u"
je level1

jne level2:
level1: 

lea dx,m1
mov ah,9
int 21h
jmp exit

level2:

lea dx,m2
mov ah,9
int 21h
exit:
mov ah,4ch
int 21h
        MAIN ENDP
END MAIN