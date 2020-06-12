import pygame
pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:

            # Left Joy Stick
            # TODO: Fine tune
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and event.value > 0 and event.value < .34:
                    print('Left-Stick: Low-Right')
                elif event.axis == 0 and event.value > .34 and event.value < .66:
                    print('Left-Stick: Mid-Right')
                elif event.axis == 0 and event.value > .99:
                    print('Left-Stick: Far-Right')

                elif event.axis == 1 and event.value < 0 and event.value > -.34:
                    print('Left-Stick: Low-Up')
                elif event.axis == 1 and event.value < -.34 and event.value > -.66:
                    print('Left-Stick: Mid-Up')
                elif event.axis == 1 and event.value < -.99:
                    print('Left-Stick: Far-Up')

                elif event.axis == 0 and event.value < 0 and event.value > -.34:
                    print('Left-Stick: Low-Left')
                elif event.axis == 0 and event.value < -.34 and event.value > -.66:
                    print('Left-Stick: Mid-Left')
                elif event.axis == 0 and event.value < -.99:
                    print('Left-Stick: Far-Left')

                elif event.axis == 1 and event.value > 0 and event.value < .34:
                    print('Left-Stick: Low-Down')
                elif event.axis == 1 and event.value > .34 and event.value < .66:
                    print('Left-Stick: Mid-Down')
                elif event.axis == 1 and event.value > .99:
                    print('Left-Stick: Far-Down')

            # Right Joy Stick
            # TODO: Fine tune
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 3 and event.value > 0 and event.value < .34:
                    print('Right-Stick: Low-Right')
                elif event.axis == 3 and event.value > .34 and event.value < .66:
                    print('Right-Stick: Mid-Right')
                elif event.axis == 3 and event.value > .99:
                    print('Right-Stick: Far-Right')

                elif event.axis == 4 and event.value < 0 and event.value > -.34:
                    print('Right-Stick: Low-Up')
                elif event.axis == 4 and event.value < -.34 and event.value > -.66:
                    print('Right-Stick: Mid-Up')
                elif event.axis == 4 and event.value < -.99:
                    print('Right-Stick: Far-Up')

                elif event.axis == 3 and event.value < 0 and event.value > -.34:
                    print('Right-Stick: Low-Left')
                elif event.axis == 3 and event.value < -.34 and event.value > -.66:
                    print('Right-Stick: Mid-Left')
                elif event.axis == 3 and event.value < -.99:
                    print('Right-Stick: Far-Left')

                elif event.axis == 4 and event.value > 0 and event.value < .34:
                    print('Right-Stick: Low-Down')
                elif event.axis == 4 and event.value > .34 and event.value < .66:
                    print('Right-Stick: Mid-Down')
                elif event.axis == 4 and event.value > .99:
                    print('Right-Stick: Far-Down')

            # L3 and R3
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(11):
                    print('L3 Pressed')
                if j.get_button(12):
                    print('R3 Pressed')

            # L2 and R2
            # Note: You can also use these without the POT values and just use the button value
            # TODO: Fine tune
            if event.type == pygame.JOYAXISMOTION:
                # print(event.dict, event.joy, event.axis)
                if event.axis == 2 and event.value > -1 and event.value < .01:
                    print('L2 Low-Pressed')
                elif event.axis == 2 and event.value > 0 and event.value < .99:
                    print('L2 Mid-Pressed')
                elif event.axis == 2 and event.value == 1:
                    print('L2 Max-Pressed')



                if event.axis == 5 and event.value > -1 and event.value < .01:
                    print('R2 Low-Pressed')
                elif event.axis == 5 and event.value > 0 and event.value < .99:
                    print('R2 Mid-Pressed')
                elif event.axis == 5 and event.value == 1:
                    print('R2 Max-Pressed')
                
            
            # L1 and R1
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(4):
                    print('L1 Pressed')
                elif j.get_button(5):
                    print('R1 Pressed')

            # Action Buttons
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(0):
                    print('X Pressed')
                elif j.get_button(3):
                    print('Square Pressed')
                elif j.get_button(1):
                    print('Circle Pressed')
                elif j.get_button(2):
                    print('Triangle Pressed')

            # Directional Pad
            if event.type == pygame.JOYHATMOTION:
                # print(event.dict, event.joy, event.hat, event.value)
                if event.hat == 0 and event.value == (-1,0):
                    print('D-Pad Left')
                elif event.hat == 0 and event.value == (1,0):
                    print('D-Pad Right')
                elif event.hat == 0 and event.value == (0,1):
                    print('D-Pad Up')
                elif event.hat == 0 and event.value == (0,-1):
                    print('D-Pad Down')

            # Share and Options / Start and Select Buttons
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(8):
                    print('Share/Select Pressed')
                if j.get_button(9):
                    print('Options/Start Pressed')

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()