import pygame

button_layout_rect = pygame.Rect(30, 20, 100, 20)

UIButton(relative_rect=button_layout_rect,
        text='Hello',
        manager=manager,
        container=ui_window)