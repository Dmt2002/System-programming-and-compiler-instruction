.model small
.stack
.data
m1 db 10,13, "Welcome$"
m2 db 10,13, "TCET$"
.code
disp macro xx
mov ah,09
lea dx , xx
int 21h
endm
.startup
disp m1
disp m2
.exit
end
