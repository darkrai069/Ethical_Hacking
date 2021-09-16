def tictactoe(field):
    for row in range(11):
        if row %2 == 0:
            practicalrow=int(row/2)
            
            for collumn in range(13):
                if collumn %2 == 0:
                    practicalcollumn=int(collumn/2)
                    
                    if collumn!=12:
                        print(field[practicalcollumn][practicalrow],end="")
                           
                    else:
                        print(field[practicalcollumn][practicalrow]+"     r"+str(practicalrow))
                        
                else:
                    print("|", end="")
        else:
            print("-------------")


player=1
currentfield=[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

tictactoe(currentfield)
moverow=range(5,-1,-1)


while True:
  
    print("Players turn :",player)
    
    movecollumn=int(input("Enter the collumn :"))
    print()
    Rcounter=0
    Ccounter=0
    Dcounter=0

    if player==1:
        for therow in moverow:

            if currentfield[movecollumn][therow]== " ":
                currentfield[movecollumn][therow] = "X"
                
                player=2
                break
            else:
                continue
        
        if player != 2:
            print("The collumn is filled choose another collumn")
            continue

    else:
        for therow in moverow:

            if currentfield[movecollumn][therow]==" ":
                currentfield[movecollumn][therow] = "O"
                
                player=1
                break
            else:
                continue
        if player != 1:
            print("The collumn is filled choose another collumn")
            continue

    
    tictactoe(currentfield)

    def Xwinchech():
        checkrow=range(5,-1,-1)
        checkcollumn=range(0,7,1)
        checkrowinc=5
        checkcollumninc=0
        Rcounter=0
        Ccounter=0
        Dcounter=0
       
#Row check for win !!!!
        for r in checkrow:
            
            checkcollumninc=0
            while checkcollumninc < 6:
                
                
                if currentfield[checkcollumninc][r] == "X":
                    Rcounter += 1
                    
                    checkcollumninc+=1
                    if Rcounter==4:
                        print("player",player, "Won!!!!")
                        exit()
                    continue
                    
                else:
                    checkcollumninc+=1
                    Rcounter=0
                    continue
                

#Collumn check for win !!!!
        for c in checkcollumn:
            
            checkrowinc=5
            while checkrowinc >= 0 :
                
                
                if currentfield[c][checkrowinc] == "X":
                    Ccounter+=1
                    
                    checkrowinc-=1
                    if Ccounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                                    
                else:
                    checkrowinc-=1
                    Ccounter=0
                    continue


#Diagonal check for win (i)!!!!
        for dc in range(4):
            Co=dc
            Ro=0
            while Co<7 and Ro<6:
                
                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Co+=1
                    Ro+=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Co+=1
                    Ro+=1
                    continue
        Dcounter=0

#Diagonal check for win (ii)!!!!                    
        for dr in range(1,3,1):
            Ro=dr
            Co=0
            while Ro<=5:
                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Ro+=1
                    Co+=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Ro+=1
                    Co+=1
                    continue
        Dcounter=0
#Diagonal check for win (iii)!!!!
        for dc in range(4):
            Co=dc
            Ro=5
            while Co<=6 and Ro>=0:

                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Co+=1
                    Ro-=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Co+=1
                    Ro-=1
                    continue
        Dcounter=0

#Diagonal check for win (iv)!!!!                    
        for dr in range(4,2,-1):
            Ro=dr
            Co=0
            while Ro<=0:
                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Ro-=1
                    Co+=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Ro-=1
                    Co+=1
                    continue
        Dcounter=0               


    def Owinchech():
        checkrow=range(5,-1,-1)
        checkcollumn=range(0,7,1)
        checkrowinc=6
        checkcollumninc=0
        Rcounter=0
        Ccounter=0
        Dcounter=0
        
#Row check for win !!!!
        for r in checkrow:
            
            checkcollumninc=0
            while checkcollumninc < 6:
                
                
                if currentfield[checkcollumninc][r] == "X":
                    Rcounter += 1
                    
                    checkcollumninc+=1
                    if Rcounter==4:
                        print("player",player, "Won!!!!")
                        exit()
                    continue
                    
                else:
                    checkcollumninc+=1
                    Rcounter=0
                    continue
                

#Collumn check for win !!!!
        for c in checkcollumn:
            
            checkrowinc=5
            while checkrowinc >= 0 :
                
                
                if currentfield[c][checkrowinc] == "X":
                    Ccounter+=1
                    
                    
                    checkrowinc-=1
                    if Ccounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                                    
                else:
                    checkrowinc-=1
                    Ccounter=0
                    continue


#Diagonal check for win (i)!!!!
        for dc in range(4):
            Co=dc
            Ro=0
            while Co<7 and Ro<6:
                
                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Co+=1
                    Ro+=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Co+=1
                    Ro+=1
                    continue
        Dcounter=0

#Diagonal check for win (ii)!!!!                    
        for dr in range(1,3,1):
            Ro=dr
            Co=0
            while Ro<=5:
                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Ro+=1
                    Co+=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Ro+=1
                    Co+=1
                    continue
        Dcounter=0
#Diagonal check for win (iii)!!!!
        for dc in range(4):
            Co=dc
            Ro=5
            while Co<=6 and Ro>=0:

                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Co+=1
                    Ro-=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Co+=1
                    Ro-=1
                    continue
        Dcounter=0

#Diagonal check for win (iv)!!!!                    
        for dr in range(4,2,-1):
            Ro=dr
            Co=0
            while Ro<=0:
                
                if currentfield[Co][Ro] == "X":
                    Dcounter+=1
                    
                    Ro-=1
                    Co+=1
                    if Dcounter==4:
                        print("player",player,"Won!!!!")
                        exit()
                else:
                    Dcounter=0
                    Ro-=1
                    Co+=1
                    continue
        Dcounter=0

    Xwinchech()
    Owinchech()