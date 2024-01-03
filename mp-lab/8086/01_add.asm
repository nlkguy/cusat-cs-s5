; @nlkguy
; addition
; NANDULAL KRISHNA
; 20221097
; S5 CSB

.model small
.data
	msg1 db 13, 10, "num1 : $"
	msg2 db 13, 10, "num2 : $"
	sum db 13, 10, "sum : $"

.code
.stack

start:

	mov ax, @data
	mov ds, ax

	lea dx, msg1
	mov ah, 09h
	int 21h

	call input
	mov bh, dl


	lea dx, msg2
	mov ah, 09h
	int 21h

	call input
	mov bl, dl


	; add
	mov ax, 0000h
	mov al, bl
	mov cx, 0000h
	mov cl, bh
	add ax, cx
	mov bx, ax


	mov ah, 09h
	lea dx, sum
	int 21h


	call output
	mov bh, bl
	call output


	mov ah, 4ch
	int 21h

;-----------------------------
input proc

	call inputnum	; get 1st digit
	mov cl, 04h	; cl = 4
	rol dl, cl	; rotate DL 4 times left(shift first digit to left nibble)
	and dl, 00f0h 	; clear lower nibble
	mov ch, dl	; move to CH


	call inputnum	; get 2nd digit to DL
	and dl, 000fh	; AND -
	add dl, ch	; add to DL

	ret
input endp
;-----------------------------
inputnum proc
	mov ah, 01h
	int 21h

	cmp al, 'A'	; compare with character A
	jc  inputnum_is_dec	; if lessthan A , it is decimal
	jmp inputnum_is_hex	; or hex
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
;-----------------------------
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
;-----------------------------
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
;-----------------------------
end start
