data segment
    array db 01h,02h,03h,04h,05h
    newline db 13,10,"$"
    wel db 13,10,"sagar , what a sudden suppaise!!$"
data ends
code segment
    assume cs:code,ds:data
start:
        mov ax,data
        mov ds,ax

        lea dx,wel
        mov ah,09h
        int 21h
        ; trivial shiz end here

        mov cx,0005h;counter
        mov ax,0000h
        mov si,0001h
        ;lea si,array

        sum:add al,array[si]

            mov dl,al
            mov ah,09h
            int 21h

            inc si
            loop sum
            hlt


        

        mov ah,4ch
        int 21h


code ends
end start
