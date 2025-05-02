import pygame
from config.generalConfig import*
from view.legDraw import*
from calc.angleCalc import*

#iniciar o pygame
pygame.init()

#variavel para controlar o time
StopTime = False

#change cordinates with predifinition
FocusCords = False
#variable to stablize the focus with the new one without changing the state...
AlreadyFocus = False

x_key_held = False
a = 1

#configurações do ecran
Ecran = pygame.display.set_mode((X_ECRAN,Y_ECRAN))
pygame.display.set_caption("IK test")
clock = pygame.time.Clock()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        # Check for q key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                 StopTime = not StopTime
            if event.key == pygame.K_s:
                 target_x, target_y = 0, -200
                 if AlreadyFocus == False:
                    FocusCords = not FocusCords
                 else:
                    AlreadyFocus = not AlreadyFocus

            if event.key == pygame.K_z:
                FocusCords = not FocusCords



            if event.key == pygame.K_x and not x_key_held: #press Z first
                if a <= 100:
                    a -= 1
                    target_x = 0 + a*10  # or just a, depending on your logic
                    target_y = -200 - a*10
                x_key_held = True
        # When key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                x_key_held = False
            
            if event.key == pygame.K_c and not x_key_held: #press Z first
                if a <= 100:
                    a += 1
                    target_x = 0 + a*10  # or just a, depending on your logic
                    target_y = -200 - a*10
                x_key_held = True
        # When key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_c:
                x_key_held = False


            if event.key == pygame.K_d:
                 target_x, target_y = -50, -190
                 if AlreadyFocus == False:
                    FocusCords = not FocusCords
                 else:
                    AlreadyFocus = not AlreadyFocus
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
                StopTime = not StopTime
                #print("Button pressed!")


        # Check for quit event
        elif event.type == pygame.QUIT:
            running = False

    # Get mouse position~
    if StopTime == False | FocusCords == False:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        target_x, target_y = mouse_x - robot_x, robot_y - mouse_y

    # Calculate angles
    teta1, teta2 = calculate_angles(target_x, target_y, l1, l2)
    teta3, teta4 = calculate_angles(target_x, target_y, l1, l2)
    if teta3 is not 0:
        teta3 = -teta3

    # preenche o Ecran
    Ecran.fill(BLACK)

    # Draw ground
    pygame.draw.rect(Ecran, GREEN, (0, ground_y, 800, 10))

    # Draw robot if angles are valid
    if teta1 is not None and teta2 is not None:
        draw_robot(Ecran, robot_x, robot_y, teta1, teta2, teta3, teta4)
    
    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
