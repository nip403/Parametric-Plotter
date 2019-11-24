import pygame
import numpy as np

pygame.init()

class Grapher:
    def __init__(self, winsize, axis):
        self.s = winsize
        self.surf = pygame.display.set_mode([self.s]*2, 0, 32)
        self.axis = axis

        self.grapher = _graphics(self.surf, self.axis)
        self.clock = pygame.time.Clock()

        self.surf.fill((255, 255, 255))
        pygame.display.flip()

    def set_time_constraints(self, t0, step, fps): # add params stop, loop
        self.t0 = t0
        self.t = t0
        self.ts = step
        self.fps = fps

    def init_x_eq(self, x):
        self.x = x

    def init_y_eq(self, y):
        self.y = y

    def begin(self):
        point0 = self.grapher.translate(self.x(self.t), self.y(self.t))
        self.t += self.ts

        self.grapher.draw_axes()

        while True:
            pygame.display.set_caption(f"t = {round(self.t, 2)}")
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            if self.t <= self.axis//2:
                point1 = self.grapher.translate(self.x(self.t), self.y(self.t))
                pygame.draw.aaline(self.surf, (0, 0, 255), point0, point1)

                self.t += self.ts
                point0 = point1

            pygame.display.flip()

class _graphics:
    def __init__(self, surf, axis):
        self.surf = surf
        self.axis = axis
        self.s = self.surf.get_size()[0]
        self.f = pygame.font.SysFont("Arial", 10)

    def draw_axes(self):
        self.surf.fill((255, 255, 255))
        
        for p, i in enumerate(range(0, self.axis+1, self.axis//self.s * 10)):
            relative = int(i - self.axis/2)

            if not p % 5 and relative:
                num = self.f.render(str(relative), True, (255, 0, 0))
                self.surf.blit(num, num.get_rect(center=[self.s/2 + 20, self.axis - (i * self.axis/self.s)]))
                self.surf.blit(num, num.get_rect(center=[i * self.axis/self.s, self.s/2 + 20]))
            
            if not p % 5:
                pygame.draw.line(self.surf, (0, 0, 0), (0, i * self.axis/self.s), (self.s, i * self.axis/self.s), 4 if not relative else 1)
                pygame.draw.line(self.surf, (0, 0, 0), (i * self.axis/self.s, 0), (i * self.axis/self.s, self.s), 4 if not relative else 1)

    def translate(self, x, y):
        return x + (self.axis)/2, self.axis/2 - y # clarify scale adjustment where axis != screensize***
