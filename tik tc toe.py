print("|||||||||||||||||||||||   #TIC-TAC-TOE  ||||||||||||||||||||||")
input("Welcome Players!!!(press enter to continue)")
plr1=input("enter the name of 1st player: ")
plr2= input("enter the name of 2nd player: ")
print(":::::::::::::::PLAYERS::::::::::::::")
print("Team ×: ",plr1.upper())
print("Team o: ",plr2.upper())
print("::::::::::::::::Grid::::::::::::::::")
g1='''   |   |   
---+---+---
   |   |   
---+---+---
   |   |   '''
print(g1)
print()
print("::::::::::Position Of Blocks:::::::::")
b=''' 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 '''
print(b)
print()
print(":::::::::::::INSTRUCTIONS::::::::::::","1.ln this game the grid is provided along with some no.s, those no.s are the position of the blocks.","2.U have to enter the no. of the block where u want to place ur '×' or 'o'","3.Pls don't write anything esle than no. in position. Otherwise it will show ERROR!!","4.The rest are the normal tic tac toe game's rules","Enjoy Playing:)",sep="\n")
print()
print("::::::::LET'S START PLAYING!!::::::::")
j=1
while j<10:
	if j%2==0:
		XorO="o"
		plr=plr2
	else:
		XorO="×"
		plr=plr1
	f5=59*(j-1)
	print(plr.title(),"'s chance:",sep="")
	pst=input("Position: ")
	if (int(pst)<=9)and(int(pst)>0):
		if pst=="1":
			i=1
		elif pst=="2":
		    i=5
		elif pst=="3":
			i=9
		elif pst=="4":
			i=25
		elif pst=="5":
			i=29
		elif pst=="6":
			i=33
		elif pst=="7":
			i=49
		elif pst=="8":
			i=53
		elif pst=="9":
			i=57
		if g1[f5+i]!=" ":
			print("sorry the place is already occupied.. pls choose another position")
			continue
		else:
			print(g1[f5:f5+i],XorO,g1[f5+(i+1):],sep="")
			gn=g1[f5:f5+i]+XorO+g1[f5+(i+1):]
			g1+=gn
			if (g1[f5+60]==g1[f5+64]==g1[f5+68])and(g1[f5+60]!=" "):
				r=1
			elif (g1[f5+84]==g1[f5+88]==g1[f5+92])and(g1[f5+84]!=" "):
				r=1
			elif (g1[f5+108]==g1[f5+112]==g1[f5+116])and(g1[f5+108]!=" "):
				r=1
			elif (g1[f5+60]==g1[f5+88]==g1[f5+116])and(g1[f5+60]!=" "):
				r=1
			elif (g1[f5+68]==g1[f5+88]==g1[f5+108])and(g1[f5+68]!=" "):
				r=1
			elif (g1[f5+60]==g1[f5+84]==g1[f5+108])and(g1[f5+60]!=" "):
				r=1
			elif (g1[f5+64]==g1[f5+88]==g1[f5+112])and(g1[f5+64]!=" "):
				r=1
			elif (g1[f5+68]==g1[f5+92]==g1[f5+116])and(g1[f5+68]!=" "):
				r=1
			else:
				r=0
			if r==1:
				if XorO=="×":
					print("::::::::C-O-N-G-R-A-T-U-L-A-T-I-O-N-S!! ",plr1.upper(),"You Won!! ;):::::::::")
					break
				else:
					print("::::::::C-O-N-G-R-A-T-U-L-A-T-I-O-N-S!! ",plr2.upper(),"You Won!! ;):::::::::::")
					break
			elif (r==0)and(j==9):
					print("DRAW MATCH:(")
					print("GAME OVER")
	elif (pst.isdigit()==False)or(int(pst)<=0)or(int(pst)>=10):
		print("Invalid Position!! G-A-M-E-O-V-E-R!!")
		break
	j+=1
