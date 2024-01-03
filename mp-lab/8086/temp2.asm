.model small
.stack 100h

print macro  msg
    mov dx,offset msg
    mov ah,9h
    int 21h
endm

print_num macro num
     mov dl,num
     add dl,"0"
     mov ah,2
     int 21h
endm


input_str macro string,len
    local loop1,skip
    mov si,0
    loop1:
        call input
        cmp al,13
        je skip
        mov string[si],al
        inc si
        jmp loop1
        skip:
            mov string[si],"$"
        mov len,si
endm

data segment
    msg1 db 10,13,"Enter the string 1",10,13,"$"
    msg2 db 10,13,"Enter the string 2","$"
    no_equal db 10,13,"strings are not equal","$"
    equal db 10,13,"strings are equal","$"

    str1 db 10,?,10 dup("$")
    str2 db 10,?,10 dup("$")
    len1 db 0
    len2 db 0
data ends

code segment
    assume ds:data,cs:code
    start:
        mov ax,data
        mov ds,ax

        print msg1

        input_str str1,len1

        print_num len1

         print msg2

        input_str str2,len2

        mov al,len1
        cmp al,len2
        jne not_equal
        mov si,0
        loop1:
            mov al,str1[si]
            cmp al,"$"
            je print_equal
            cmp al,str2[si]
            jne not_equal
            inc si
            jmp  loop1

        print_equal:
            print equal
            jmp exit
        not_equal:
            print no_equal


    exit:
        mov ah,4ch
        int 21h

    input:
        mov ah,01h
        int 21h
        ret

code ends
end start