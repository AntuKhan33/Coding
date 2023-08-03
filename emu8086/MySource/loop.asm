.model small
.stack 100h
.data

m1 db "first program $"
m2 db 0ah,0dh, "second program$"
m3 db 0ah,0dh,"enter first character $"
m4 db 0ah,0dh, "your character is $"
.code
main proc
MOV AX, @DATA
MOV DS, AX


   mov ah,2
   mov dl,"*"
   MOV CX, 10
L:
INT 21H 
LOOP L

    