.model small
.data
    stringarray1 db 30 dup("$")
    message1 db 13,10, "this is a god$"
    message2 db 13,10, "you have done wrong$"
.code
.stack
start:
    mov ax,@data
    mov ds,ax

    lea dx,message1
    mov ah,09h
    int 21h

    lea dx,message2
    mov ah,09h
    int 21h

    call input_string
    call output_string

    call exit



exit proc
    mov ah,4ch
    int 21h
exit endp

input_string proc
    loopin: lea ah,01h
            int 21h
            cmp al,13
            je skip
            mov [si],al
            inc si
            jmp loopin
    skip:   call output_string

input_string endp

output_string proc
      
output_string endp


end start