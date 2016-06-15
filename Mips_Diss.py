import sys,time 
add = 496
Break = 0

print "\n\n##############################################"
print "Welcome to MIPS Dissambler by Abhinav Jayanthy (mim289)"
print "##############################################"
filename = raw_input('\n \nPlease enter the binary code text file name (e.g. abcdef.txt) including the .txt extension or its path: ')
text_input = open(filename,'r')
text_output = open("Mips.txt",'w')
print "\n"
print "Converting....."


def bin2dec(bin_str):
    sign = bin_str[0]
    if sign is '0':
        return int(bin_str,2)
    elif sign is '1':
        comp = int(bin_str[1:],2)
        dec = (2**(len(bin_str)-1)) - comp
        return -1*dec

def bintodec(bin_str):
    sign = bin_str[0]
    if sign is '0':
        return int(bin_str,2)
    elif sign is '1':
        comp = int(bin_str[1:],2)
        dec = (2**(len(bin_str)-2)) - comp
        return -1*dec


def opcode(special,rs,rt,rd,o,instruction):
	global Break
	if instruction == "100000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"ADD  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "001000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"ADDI 	R"+str(bin2dec(rt))+", R"+str(bin2dec(rs))+", #"+str(bin2dec(o+instruction)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100001":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"ADDU  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100010":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SUB  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100011":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SUBU  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "001001":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"ADDIU 	R"+str(bin2dec(rt))+", R"+str(bin2dec(rs))+", #"+str(bin2dec(o+instruction)))
		text_output.write("\n")
	elif special == "000000" and rs == "00000" and rt !="00000" and rd != "00000" and o != "00000" and instruction == "000000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SLL  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rt))+", R"+str(bin2dec(o)))
		text_output.write("\n")
	elif special == "000000" and rs == "00000" and instruction == "000010":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SRL  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rt))+", R"+str(bin2dec(o)))
		text_output.write("\n")
	elif special == "000000" and rs == "00000" and instruction == "000011":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SRA  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rt))+", R"+str(bin2dec(o)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100100":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"AND  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100101":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"OR  	    R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100111":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"NOR  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "100110":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"XOR  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "000000" and o == "00000" and instruction == "101010":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SLT  	R"+str(bin2dec(rd))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(rt)))
		text_output.write("\n")
	elif special == "001010":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SLTI  	R"+str(bin2dec(rt))+", R"+str(bin2dec(rs))+", R"+str(bin2dec(o+instruction)))
		text_output.write("\n")
	elif special == "000100":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BEQ  	R"+str(bin2dec(rs))+", R"+str(bin2dec(rt))+", #"+str(bin2dec((o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000101":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BNE  	R"+str(bin2dec(rs))+", R"+str(bin2dec(rt))+", #"+str(bin2dec((o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000001" and rt == "00001":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BGEZ  	R"+str(bin2dec(rs))+", #"+str(bin2dec((o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000111" and rt == "00000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BGTZ  	R"+str(bin2dec(rs))+", #"+str(bin2dec((o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000110" and rt == "00000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BLEZ  	R"+str(bin2dec(rs))+", #"+str(bin2dec((o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000001" and rt == "00000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BLTZ  	R"+str(bin2dec(rs))+", #"+str(bin2dec((o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000010":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"J"+"	"+"#"+str(bin2dec((rs+rt+rd+o+instruction+"00"))))
		text_output.write("\n")
	elif special == "000000" and rs != "00000" and rt == "00000" and rd == "00000" and instruction == "001000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"JR"+"	"+"#"+str(bin2dec(rs)))
		text_output.write("\n")
	elif special == "100011":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"LW 	R"+str(bin2dec(rt))+", "+str(bin2dec(o+instruction))+"(R"+str(bin2dec(rs))+")")
		text_output.write("\n")
	elif special == "101011":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"SW 	R"+str(bin2dec(rt))+", "+str(bin2dec(o+instruction))+"(R"+str(bin2dec(rs))+")")
		text_output.write("\n")
	elif instruction == "001101":
		Break = 1
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"BREAK")
		text_output.write("\n")
	elif Break == 1:
		conv = bintodec(line)
		text_output.write(special+""+rs+""+rt+""+rd+""+o+""+instruction+"	"+str(add)+"	"+str(conv))
		text_output.write("\n")
	elif special == "000000" and rs == "00000" and rt == "00000" and rd == "00000" and o == "00000" and instruction == "000000":
		text_output.write(special+" "+rs+" "+rt+" "+rd+" "+o+" "+instruction+"	"+str(add)+"	"+"NOP")
		text_output.write("\n")



for line in text_input:
	special = line[0:6]
	rs = line[6:11]
	rt = line[11:16]
	rd= line[16:21]
	o = line[21:26]
	instruction = line[26:32]
	opcode(special,rs,rt,rd,o,instruction)
	add = add + 4

time.sleep(2)
print "\nDone\n\n"
print "#################################################################################################"
print "Please check the working folder for the output it will be a text file with output as Mips.txt"
print "#################################################################################################\n\n"
text_output.close()
text_input.close()