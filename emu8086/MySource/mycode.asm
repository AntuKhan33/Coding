.model small
.stack 100h
.data

m1 db "please add code$" 
m2 db 0ah,0dh,"Mursalin Khan$"
m3 dw "0"d

.code

main proc
         
       mov ax,@data
       mov ds, ax
       
       
       lea   dx,m1
       mov ah,9
       int 21h
       
       mov ah,1
       int 21h
       mov bx,ax
       mov dx,bx
       
       
       mov ah,1
       int 21h  
       
              
              
       
       
       l:
       cmp dx,ax
       je there1
       
       jge there2
       jle there3
       
       loop l
       
       there1:
       lea dx,m2
       mov ah,9
       int 21h
       jmp exit
       
       there2:
       
       cmp dx,ax
       
       mov ah,2
   
       
       inc dx
       
       
       jmp exit
       there3:
       cmp dx,ax
       mov ah,2
       mov ax,0
       add ax,dx
       
       dec dx
       
       
       
       jmp exit
       exit:
       mov ah,4ch
       int 21h       