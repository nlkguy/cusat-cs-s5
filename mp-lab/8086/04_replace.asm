
; @nlkguy
; string replace
; NANDULAL KRISHNA
; 20221097
; S5 CSB


data segment
	str1 db 20 dup("$")
	str2 db 20 dup("$")
	newstr db 20 dup("$")
	
	wel db 13,10,"string replace ---- $"
	mainstr db 13,10,"str 1 : $"
	replstr db 13,10,"str rep : $"
	newstring db 13,10,"str new : $"
	outstring db 13,10,"str 1 : $"
	foundstring db 13,10,"found $"
	notstring db 13,10,"no found $"
		
data ends


code segment
	assume cs:code , ds:data
start:
      mov ax,data
      mov ds,ax
      
      lea dx,wel
      mov ah,09h
      int 21h
      
      lea dx,mainstr
      mov ah,09h
      int 21h
       
      loop0:mov ah,01h
           int 21h
           cmp al,13
           je skip
           mov [si],al
           inc si
           jmp loop0
           
      skip:mov ah,09h
           lea dx,replstr
           int 21h
     
      lea si,str2
      loop1:mov ah,01h
            int 21h
            cmp al,13
            je skip1
            mov [si],al
            inc si
            jmp loop1
            
      skip1:mov ah,09h
           lea dx,newstring
           int 21h
      
      lea si,newstr
      loop2:mov ah,01h
            int 21h
            cmp al,13
            je skip2
            mov [si],al
            inc si
            jmp loop2
      
      
      skip2: call replace
     
            
            mov ah,4ch
            int 21h
            
replace proc
       lea si,str1
       lea di,str2
       mov al,"$"
       
       
       compare:cmp al,[si]
               je nosub
               mov bl,[si]
               cmp bl,[di]
               je copy
               inc si
               jmp compare
       
       copy: mov cx,si
             lea di,newstr
             jmp loop3
             
       nosub:lea dx,notstring
             mov ah,09h
             int 21h 
             mov ah,4ch
            int 21h
          
       
              
       loop3: 
              cmp al,[di]
              jz exit
              mov bl,[di]
              mov [si],bl
              inc si
              inc di
              jmp loop3
              
       exit: mov [di],al
             lea dx,outstring
             mov ah,09h
             int 21h
             lea dx,str1
             mov ah,09h
             int 21h
             ret
replace endp
code ends
end start
            
