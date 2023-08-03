

.model small
.stack 100h
.data
.code

main proc
 



   mov ah,1
   int 21h
   
   cmp al,"A"
   je then
   cmp al,"a"
   je then
   jmp else_
   then:
   mov ah,2
   mov dl,al
   int 21h
   jmp end_if
   else_:
   mov ah,4ch
   int 21h
   
   end_if:
   mov ah,4ch
    int 21h