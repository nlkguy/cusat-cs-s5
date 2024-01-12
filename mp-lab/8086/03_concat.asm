
; @nlkguy
; string concat
; NANDULAL KRISHNA
; 20221097
; S5 CSB


data segment
	str1 db 30 dup("  $")
	str2 db 30 dup("$")
	m1 db 13,10,"str 1 : $"
	m2 db 13,10,"str 1 : $"
	outp db 13,10,"str 1 : $"
	wel db 13,10,"string concat ---- $"
data ends

code segment
assume cs:code , ds:data
start:
      mov ax,data
      mov ds,ax
      mov cl,04
      
      lea dx,wel
      mov ah,09h
      int 21h
      
      lea dx,m1
      mov ah,09h
      int 21h
      
      lea si,str1
      loop0:mov ah,01h
           int 21h
           cmp al,13
           je skip
           mov [si],al
           inc si
           jmp loop0
           
      skip:mov ah,09h
           lea dx,m2
           int 21h
     
      lea si,str2
      loop1:mov ah,01h
            int 21h
            cmp al,13
            je skip1
            mov [si],al
            inc si
            jmp loop1
            
      skip1:call concat
            
            mov ah,4ch
            int 21h
            
concat proc
       lea si,str1
       lea di,str2
       mov al,"$"
       
       loop2: cmp al,[si]
              jz loop3
              inc si
              jmp loop2
              
       loop3: 
              cmp al,[di]
              jz exit
              mov bl,[di]
              mov [si],bl
              inc si
              inc di
              jmp loop3
              
       exit: mov [di],al
             lea dx,outp
             mov ah,09h
             int 21h
             lea dx,str1
             mov ah,09h
             int 21h
             ret
concat endp
code ends
end start
            
            
      

