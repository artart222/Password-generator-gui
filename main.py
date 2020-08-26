import pygame , random , csv


#These are lists of characters that program can use to generate password
smlLetters = ["a", "b",  "c", "d", "e", "f", "g", "h", "i", "j", "k",
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
"z"]
capLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
"Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+"]


#genpass function generate password.
def genpass(smlLetters, capLetters, numbers, symbols, useSmlLetters, useCapLetters, useNumbers, useSymbols, lenOfPassword, nameOfPassword):
    #This is password. every time program choose character for password program add character to password string.
    password = ""

    #This is list of characters that program can use
    liOfChars = []
    if useSmlLetters == True:
        liOfChars.append(smlLetters)
    if useCapLetters == True:
        liOfChars.append(capLetters)
    if useNumbers == True:
        liOfChars.append(numbers)
    if useSymbols == True:
        liOfChars.append(symbols)

    #check that if user doesn't use any option then program dont generate password
    if useNumbers != False and useSymbols != False and useCapLetters != False and useSmlLetters != False:
        for char in range(int(lenOfPassword)):
            #choose characters
            choosingList = liOfChars[(random.randrange(0, (liOfChars.index(liOfChars[-1]) + 1)))]
            choosingChar = choosingList[(random.randrange(0, (choosingList.index(choosingList[-1]) + 1)))]
            password += choosingChar

        #write password in file.txt
        with open("./file.csv", "a") as csvFile:
            csvReader = csv.reader(csvFile)
            csvWriter = csv.writer(csvFile)
            password = [nameOfPassword, password]
            csvWriter.writerow(password)


pygame.init()
pygame.font.init()
font = pygame.font.Font("./Font/Inter-VariableFont_slnt,wght.ttf", 15)


#length and width of gui display
winx  , winy = 800, 800
win = pygame.display.set_mode((winx , winy))


#values of color that used in background
bcColor = [100, 100, 100]


fpsClock = pygame.time.Clock()
fpsValue = 60


appIcon = pygame.image.load("./Pictures/icon.jpeg")
pygame.display.set_icon(appIcon)
pygame.display.set_caption("Password Generator")

#load image of green tick that program use in option boxs
tick = pygame.image.load("./Pictures/tick.png")


def optionBox(text, posx, posy, lenx, leny, condition):
    pygame.draw.rect(win, (220, 220, 220), (posx, posy, lenx, leny))

    #check if option of password is enable draw tick in box
    if condition == True:
        win.blit(tick, (posx + 1, posy + 1))

    #write text in front of box
    text = font.render(text, True, (255, 255, 255))
    win.blit(text, (posx + 41, posy + 1))


#checking for clicking on options boxs
def checkClick(posx, posy, lenx, leny, condition):
    if mx >= posx and mx <= posx + lenx - 2 and my >= posy and my <= posy + leny - 2:
        if condition == True:
            condition = False
        else:
            condition = True

    return condition


#this function is for receiving len of password from user
def inputBox(posx, posy, lenx, leny, cActive, cPassive, condition, input, bText, fText, fPosX, fPosY):
    #draw bText before input box
    text = font.render(bText, True, (255, 255, 255))
    win.blit(text, (posx - 127, posy))

    #choose color of input box
    if condition == True:
        color = cActive
    else:
        color = cPassive

    #draw box that contain user input
    pygame.draw.rect(win, color, (posx, posy, lenx, leny), 2)

    #draw user input in input box
    text = font.render(input, True, (255, 255, 255))
    win.blit(text, (posx + 4, posy + 2))

    #draw fText in front of input box
    text = font.render(fText, True, (255, 255, 255))
    win.blit(text, (fPosX, fPosY))


useSmlLetters = False
useCapLetters = False
useNumbers = False
useSymbols = False


lenOfPassword = ""
nameOfPassword = ""
"""
lenActive is variable that used in inputBox function if it was False it means that user dosen't select input box
and set color of input box to dark color(gray15) else change to light color(lightskyblue3). nameActive do same thing.
"""
lenActive = False
nameActive = False


"""
posOfGenBut values are values that used in drawing and checking for clicking on generate button. posOfLenInput values are values that
used in drawing and checking for clicking on input box of len password and posOfNameInput values are values that used in drawing and
checking for clicking on input box of name password.
"""
posOfGenBut = [249 , 499 , 302 , 102]
posOfLenInput = [150 , 98 , 43 , 22]
posOfNameInput = [150, 128, 220, 22]
running = True
while running:
    fpsClock.tick(fpsValue)
    win.fill(bcColor)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #get position of where user click
                mx , my = pygame.mouse.get_pos()
                #checking for generate button
                if mx >= posOfGenBut[0] and mx <= posOfGenBut[0] + posOfGenBut[2] and my >= posOfGenBut[1] and my <= posOfGenBut[1] + posOfGenBut[3]:
                    genpass(smlLetters, capLetters, numbers, symbols, useSmlLetters, useCapLetters, useNumbers, useSymbols, lenOfPassword, nameOfPassword)
                #checking for use number button
                useNumbers = checkClick(30 , 200 , 22 , 22 , useNumbers)
                #checking for use symbols button
                useSymbols = checkClick(30 , 250 , 22 , 22 , useSymbols)
                #checking for use capital letters button
                useCapLetters = checkClick(30 , 300 , 22 , 22 , useCapLetters)
                #checking for use small letters button
                useSmlLetters = checkClick(30 , 350 , 22 , 22 , useSmlLetters)
                if mx >= posOfLenInput[0] and mx <= posOfLenInput[0] + posOfLenInput[2] and my > posOfLenInput[1] and my < posOfLenInput[1] + posOfLenInput[3]:
                    lenActive = True
                else:
                    lenActive = False
                if mx >= posOfNameInput[0] and mx <= posOfNameInput[0] + posOfNameInput[2] and my > posOfNameInput[1] and my < posOfNameInput[1] + posOfNameInput[3]:
                    nameActive = True
                else:
                    nameActive = False


        if event.type == pygame.KEYDOWN:
            if lenActive:
                if event.key == pygame.K_BACKSPACE:
                    lenOfPassword = lenOfPassword[:-1]
                else:
                    try:
                        newchar = ""
                        newchar = int(event.unicode)
                        newchar = str(newchar)
                        if len(lenOfPassword) < 4:
                            lenOfPassword += newchar
                        if int(lenOfPassword) > 4096:
                            lenOfPassword = "4096"
                    except ValueError:
                        pass
            if nameActive:
                if event.key == pygame.K_BACKSPACE:
                    nameOfPassword = nameOfPassword[:-1]
                else:
                    newchar = event.unicode
                    if len(nameOfPassword) < 30:
                        nameOfPassword += newchar


    #drawing generate button
    pygame.draw.rect(win , (220 , 220 , 220) , (posOfGenBut[0] , posOfGenBut[1] , posOfGenBut[2] , posOfGenBut[3]))

    #draw text inside of generator button
    text = font.render("Generate password" , True , (0 , 0 , 0))
    win.blit(text , (posOfGenBut[0] + posOfGenBut[2] / 2 - 60  , posOfGenBut[1] + posOfGenBut[3] / 2))

    #draw option boxes
    optionBox("Use numbers" , 30 ,  200 , 22 , 22 , useNumbers)
    optionBox("Use symbols" , 30 ,  250 , 22 , 22 , useSymbols)
    optionBox("Use capital letters" , 30 , 300 , 22 , 22 , useCapLetters)
    optionBox("Use small letters" , 30 , 350 , 22 , 22 , useSmlLetters)

    #draw input boxes
    inputBox(posOfLenInput[0] , posOfLenInput[1] , posOfLenInput[2] , posOfLenInput[3] , pygame.Color("lightskyblue3") , pygame.Color("gray15") , lenActive , lenOfPassword, "password length: ", "Maximum number is 4096", posOfLenInput[0] + 47, posOfLenInput[1] + 2)
    inputBox(posOfNameInput[0], posOfNameInput[1], posOfNameInput[2], posOfNameInput[3], pygame.Color("lightskyblue3"), pygame.Color("gray15"), nameActive, nameOfPassword, "Password name: ", "Maximum length of name of password is 30 charchter", posOfNameInput[0] + 230, posOfNameInput[1] + 2)


    pygame.display.update()


pygame.quit()
