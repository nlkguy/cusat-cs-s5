data segment
    arr1 dw 10 dup(?)
    arr2 dw 1,2,3,4,5,6,7,8,9,10
    newline db 13,10,"$"
    wel db 13,10,"sagar , what a sudden surprise!!$"

data ends

code segment
    assume cs:code,ds:data
start:
        mov ax,data
        mov ds,ax

        lea dx,wel
        mov ah,09h
        int 21h
        ; trivial shiz ends here

        lea si,arr2
        mov cx,10
        mov bx,0

    display_sum:
        mov ax,[si]
        add bx,ax

        lea dx,newline
        mov ah,09h
        int 21h

        ; Convert the array element to ASCII before printing
        add ax, '0'
        mov dl, al
        mov ah, 02h
        int 21h

        lea dx,newline
        mov ah,09h
        int 21h

        add si,2  ; Move to the next element (2 bytes per element)
        loop display_sum ; loop based on cx

        lea dx,newline
        mov ah,09h
        int 21h

        ; Display the sum
        mov dx,bx
        mov ah,09H
        int 21H

        ; exiting
        mov ah,4ch
        int 21h

code ends
end start
