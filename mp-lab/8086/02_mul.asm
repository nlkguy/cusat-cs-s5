; @nlkguy
; multiplication
; NANDULAL KRISHNA
; 20221097
; S5 CSB

.model small
.data
	ms1 db 13, 10, "num1 : $"
	ms2 db 13, 10, "num2 : $"
	prod db 13, 10, "product :  $"

.code
.stack

start:

	mov ax, @data
	mov ds, ax

	lea dx, ms1
	mov ah, 09h
	int 21h

	call input
	mov bh, dl


	lea dx, ms2
	mov ah, 09h
	int 21h

	call input
	mov bl, dl


	mov al, bl
	mul bh
	mov bx, ax


	mov ah, 09h
	lea dx, prod
	int 21h


	call output
	mov bh, bl
	call output


	mov ah, 4ch
	int 21h
	
;---------------------------------

input proc

	call inputnum
	mov cl, 04h
	rol dl, cl
	and dl, 00f0h
	mov ch, dl


	call inputnum
	and dl, 000fh
	add dl, ch

	ret
input endp
;---------------------------------
inputnum proc
	mov ah, 01h
	int 21h

	cmp al, 'A'
	jc  inputnum_is_dec
	jmp inputnum_is_hex
inputnum_is_hex:
	sub al, 'A'
	add al, 0ah
	mov dl, al
	ret
inputnum_is_dec:
	sub al, '0'
	mov dl, al
	ret
inputnum endp

;---------------------------------
output proc
	mov al, bh
	and al, 00f0h
	mov cl, 04h
	ror al, cl
	mov dl, al
	call outputnum

	mov dl, bh
	and dl, 000fh
	call outputnum

	ret
output endp
;---------------------------------
outputnum proc
	mov ah, 02h

	cmp dl, 0ah
	jc  outputnum_is_dec
	jmp outputnum_is_hex
outputnum_is_hex:
	add dl, 'A'
	sub dl, 0ah
	int 21h
	ret
outputnum_is_dec:
	add dl, '0'
	int 21h
	ret
outputnum endp
;---------------------------------

end start
