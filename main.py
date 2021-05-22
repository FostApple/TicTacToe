import pygame
pygame.init()
wn = pygame.display.set_mode((300,300))

gamestate = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
turn = 2
gameon = True

while gameon:
  wn.fill((0,0,0))
  
  bd00=pygame.draw.rect(wn, (255,255,255), (2,2,96,96))
  bd01=pygame.draw.rect(wn, (255,255,255), (102,2,96,96))
  bd02=pygame.draw.rect(wn, (255,255,255), (202,2,96,96))
 
  bd10=pygame.draw.rect(wn, (255,255,255), (2,102,96,96))
  bd11=pygame.draw.rect(wn, (255,255,255), (102,102,96,96))
  bd12=pygame.draw.rect(wn, (255,255,255), (202,102,96,96))
  
  bd20=pygame.draw.rect(wn, (255,255,255), (2,202,96,96))
  bd21=pygame.draw.rect(wn, (255,255,255), (102,202,96,96))
  bd22=pygame.draw.rect(wn, (255,255,255), (202,202,96,96))

  bd = [
    [bd00,bd01,bd02],
    [bd10,bd11,bd12],
    [bd20,bd21,bd22]
  ]
  


  if turn == 2:
    #AIs turn
    for r in [0,1,2]:
      if gamestate[r][0] == gamestate[r][1] != 0 and gamestate[r][2]== 0:
        gamestate[r][2] = 2
        turn = 1
      elif gamestate[r][2] == gamestate[r][1] != 0 and gamestate[r][0]== 0:
        gamestate[r][0] = 2
        turn = 1
      elif gamestate[r][0] == gamestate[r][2] != 0 and gamestate[r][1]== 0:
        gamestate[r][1] = 2
        turn = 1

  if turn == 2:
    for c in [0,1,2]:
      if gamestate[0][c] == gamestate[1][c] != 0 and gamestate[2][c]== 0:
        gamestate[2][c] = 2
        turn = 1
      elif gamestate[2][c] == gamestate[1][c] != 0 and gamestate[0][c]== 0:
        gamestate[0][c] = 2
        turn = 1
      elif gamestate[0][c] == gamestate[2][c] != 0 and gamestate[1][c]== 0:
        gamestate[1][c] = 2
        turn = 1
    if gamestate[0][0] == gamestate[1][1] != 0 and gamestate[2][2]== 0:
      gamestate[2][2] = 2
      turn = 1
    if gamestate[0][2] == gamestate[1][1] != 0 and gamestate[2][0]== 0:
      gamestate[2][0] = 2
      turn = 1
    if gamestate[2][0] == gamestate[1][1] != 0 and gamestate[0][2]== 0:
      gamestate[0][2] = 2
      turn = 1
    if gamestate[1][1] == gamestate[2][2] != 0 and gamestate[0][0]== 0:
      gamestate[0][0] = 2
      turn = 1
    if gamestate[1][1] == gamestate[0][0] != 0 and gamestate[2][2]== 0:
      gamestate[2][2] = 2
      turn = 1
    if gamestate[1][1] == gamestate[0][2] != 0 and gamestate[2][0]== 0:
      gamestate[2][2] = 2
      turn = 1
    if gamestate[1][1] == gamestate[2][0] != 0 and gamestate[0][2]== 0:
      gamestate[0][2] = 2
      turn = 1


  if turn == 2:
    if gamestate [1][1] == 0:
      gamestate [1][1] = 2
    elif gamestate [2][2] == 0:
      gamestate [2][2] = 2
    elif gamestate [0][0] == 0:
      gamestate [0][0] = 2
    elif gamestate [2][0] == 0:
      gamestate [2][0] = 2
    elif gamestate [0][2] == 0:
      gamestate [0][2] = 2
    elif gamestate [1][0] == 0:
      gamestate [1][0] = 2
    elif gamestate [1][2] == 0:
      gamestate [1][2] = 2
    elif gamestate [0][1] == 0:
      gamestate [0][1] = 2
    elif gamestate [2][1] == 0:
      gamestate [2][1] = 2
    else:
      print("why")
    turn = 1

      
  if turn == 1:
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        for rownum in [0,1,2]:
          for colnum in [0,1,2]:
            if bd[rownum][colnum].collidepoint(pos) and gamestate [rownum][colnum] == 0:
              #Humans turn
              gamestate[rownum][colnum] = 1
              turn = 2

  for rownum in [0,1,2]:
    for colnum in [0,1,2]:
      square = gamestate[rownum][colnum]
      if square == 2:
        pygame.draw.line(wn,(0,0,0),(colnum*100+25,rownum*100+25),(colnum*100+75,rownum*100+75))
        pygame.draw.line(wn,(0,0,0),(colnum*100+75,rownum*100+25),(colnum*100+25,rownum*100+75))
      elif square == 1:
        pygame.draw.circle(wn,(0,0,0),(colnum*100+50,rownum*100+50),30)
        pygame.draw.circle(wn,(255,255,255),(colnum*100+50,rownum*100+50),29)


  for rownum in [0,1,2]:
    if gamestate[rownum][0] == gamestate[rownum][1] == gamestate[rownum][2] and gamestate[rownum][0] != 0:
      if gamestate[rownum][colnum] == 1:
        print("\n\n\nO has won!\n\n\n")
        gameon = False
      else:
        print("\n\n\nX has won!\n\n\n")
        gameon = False

  for colnum in [0,1,2]:
    if gamestate[0][colnum] == gamestate[1][colnum] == gamestate[2][colnum] and gamestate[0][colnum] != 0:
      if gamestate[rownum][colnum] == 1:
        print("\n\n\nO has won!\n\n\n")
        gameon = False
      else:
        print("\n\n\nX has won!\n\n\n")
        gameon = False

  if gamestate[0][0] == gamestate[1][1] == gamestate[2][2] and gamestate[0][0] != 0:
    if gamestate[0][0] == 1:
      print("\n\n\nO has won!\n\n\n")
      gameon = False
    else:
      print("\n\n\nX has won!\n\n\n")
      gameon = False

  if gamestate[0][2] == gamestate[1][1] == gamestate[2][0] and gamestate[0][2] != 0:
    if gamestate[0][2] == 1:
      print("\n\n\nO has won!\n\n\n")
      gameon = False
    else:
      print("\n\n\nX has won!\n\n\n")
      gameon = False
    
  
  if gameon == True:
    tie = True
    for rownum in [0,1,2]:
      for colnum in [0,1,2]:
        if gamestate[rownum][colnum] == 0:
          tie = False

    if tie:
      print("\n\n\nBoth of you are bad!\n\n\n")
      gameon = False


  pygame.display.update()