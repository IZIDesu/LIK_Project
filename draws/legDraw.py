import math
from config.generalConfig import*
from calc.angleCalc import*
import pygame

# Function to draw the robot
def draw_robot(screen, x, y, teta1, teta2, teta3, teta4):
    # Calculate leg segment end points
    x1 = x + l1 * math.cos(math.radians(teta1))
    y1 = y - l1 * math.sin(math.radians(teta1))
    x2 = x1 + l2 * math.cos(math.radians(teta1 + teta2))
    y2 = y1 - l2 * math.sin(math.radians(teta1 + teta2))

    x3 = x - l1 * math.cos(math.radians(teta3))  # mirrored direction
    x4 = x3 - l2 * math.cos(math.radians(teta3 + teta4))
    
    #x3 = x + l1 * math.cos(math.radians(teta3))
    #x4 = x3 + l2 * math.cos(math.radians(teta3 + teta4))

    # Calculate the foot's rectangle
    foot_rect = pygame.Rect(x2 - foot_width / 2, y2, foot_width, foot_height)
    foot_rect2 = pygame.Rect(x4 - foot_width / 2, y2, foot_width, foot_height)

    # Adjust the foot position if it goes below the ground
    if y2 + foot_height > ground_y:
        foot_rect.y = ground_y - foot_height
        y2 = -foot_rect.y #- foot_height/2  # Correct the end position of the leg

        # Recalculate the position of the first leg segment to ensure it aligns with the new foot position
        # This step ensures that both legs adjust to keep the foot on the ground
        x1 = x2 - l2 * math.cos(math.radians(teta1 + teta2))
        y1 = y2 + l2 * math.sin(math.radians(teta1 + teta2))

        x3 = x2 - l2 * math.cos(math.radians(teta3 + teta4))

        # Ensure the initial segment aligns correctly with the robot's body
        if y1 > ground_y:
            y1 = ground_y
            x1 = x + l1 * math.cos(math.radians(teta1))
            x3 = x + l1 * math.cos(math.radians(teta3))

    # Draw the robot
    pygame.draw.line(screen, L3Color, (x, y), (x3, y1), 5)  # Upper leg
    pygame.draw.line(screen, L4Color, (x3, y1), (x4, y2), 5)  # Lower leg
    pygame.draw.rect(screen, FootOutlineColor, foot_rect2, 2)  # Foot outline
    
    pygame.draw.circle(screen, CircleColor, (x, y), 10)  # Lower torso
    pygame.draw.line(screen, L1Color, (x, y), (x1, y1), 5)  # Upper leg
    pygame.draw.line(screen, L2Color, (x1, y1), (x2, y2), 5)  # Lower leg
    pygame.draw.rect(screen, FootColor, foot_rect)  # Foot
    pygame.draw.rect(screen, FootOutlineColor, foot_rect, 2)  # Foot outline

    # Initialize font
    font = pygame.font.SysFont(TextFont, TextSize)

    # Render the angles as text
    #angle_text = f"Angle 1: {teta1:.2f}°  Angle 2: {teta2:.2f}°"
    #text_surface = font.render(angle_text, True, TextColor)
    #screen.blit(text_surface, (10, 10))  # Draw text on screen

    # Render the angles as multiline text
    angle_text = [
        f"hip angle:  {-teta1:.2f}°",
        f"knee angle: {teta2:.2f}°",
        f"hip2 angle: {teta3:.2f}°",
        f"knee2 angle:{teta4:.2f}°",
    ]

    Y_offset = 10  # Starting vertical position for text
    colors = [RED, BLUE, YELLOW, GREEN]  # Colors for each line

    for i, line in enumerate(angle_text):
        text_surface = font.render(line, True, colors[i])
        screen.blit(text_surface, (10, Y_offset))
        Y_offset += 32  # Move down by the font size

    #if you want to put just in one color V
    #for line in angle_text:
    #    text_surface = font.render(line, True, TextColor)
    #    screen.blit(text_surface, (10, y_offset))
    #    y_offset += 36  # Move down by the font size
    
