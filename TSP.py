import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

class OpenGLTSPSolver:
    def __init__(self):
        self.cities = []
        self.route = []
        self.running = True
        self.width, self.height = 800, 600

    def run(self):
        pygame.init()
        pygame.display.set_mode((self.width, self.height), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("TSP Solver (Nearest Neighbor) - OpenGL")

        gluOrtho2D(0, 100, 0, 100)  # Coordinate system (0,0 to 100,100)

        while self.running:
            self.handle_events()
            self.render()
            pygame.display.flip()
            pygame.time.wait(10)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                gl_x = x / self.width * 100
                gl_y = (self.height - y) / self.height * 100
                self.cities.append((gl_x, gl_y))

            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if len(self.cities) >= 2:
                        self.solve_tsp()
                elif event.key == K_c:
                    self.cities.clear()
                    self.route.clear()

    def solve_tsp(self):
        start_time = time.time()
        unvisited = self.cities.copy()
        path = [unvisited.pop(0)]
        while unvisited:
            last = path[-1]
            nearest = min(unvisited, key=lambda city: np.hypot(city[0] - last[0], city[1] - last[1]))
            path.append(nearest)
            unvisited.remove(nearest)
        path.append(path[0])
        self.route = path
        total_distance = self.calculate_distance(path)
        elapsed = (time.time() - start_time) * 1000
        label_path = self.get_label_path()
        print(f"\nShortest Route: {label_path}")
        print(f"Total Distance: {total_distance:.2f}")
        print(f"Computation Time: {elapsed:.2f} ms")

    def calculate_distance(self, path):
        return sum(np.hypot(path[i][0] - path[i+1][0], path[i][1] - path[i+1][1])
                   for i in range(len(path) - 1))

    def get_label_path(self):
        labels = []
        for city in self.route[:-1]:
            for i, c in enumerate(self.cities):
                if city == c:
                    labels.append(chr(65 + i))
                    break
        return " → ".join(labels + [labels[0]])

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 0.0, 0.0)

        # Draw enhanced cities
        for i, (x, y) in enumerate(self.cities):
            # Outer circle (highlight)
            glColor3f(1.0, 0.5, 0.0)  # Orange
            self.draw_circle(x, y, 1.5, segments=20)

            # Inner point
            glPointSize(10)
            glColor3f(1.0, 0.0, 0.0)  # Red
            glBegin(GL_POINTS)
            glVertex2f(x, y)
            glEnd()

            # Label (A, B, C...)
            self.draw_text(x + 1.5, y + 1.5, chr(65 + i))

        # Draw TSP Route
        if self.route:
            glColor3f(0.0, 0.0, 1.0)  # Blue lines
            glLineWidth(2)
            glBegin(GL_LINE_STRIP)
            for x, y in self.route:
                glVertex2f(x, y)
            glEnd()

            # Order numbers
            for idx, (x, y) in enumerate(self.route[:-1]):
                self.draw_text(x - 1, y - 3, str(idx + 1))

    def draw_circle(self, x, y, radius, segments=20):
        glLineWidth(1)
        glBegin(GL_LINE_LOOP)
        for i in range(segments):
            angle = 2 * np.pi * i / segments
            glVertex2f(x + np.cos(angle) * radius, y + np.sin(angle) * radius)
        glEnd()

    def draw_text(self, x, y, text):
        font = pygame.font.SysFont('Arial', 14)
        text_surface = font.render(text, True, (0, 0, 0), (255, 255, 255))
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        glRasterPos2f(x, y)
        glDrawPixels(text_surface.get_width(), text_surface.get_height(),
                     GL_RGBA, GL_UNSIGNED_BYTE, text_data)

if __name__ == "__main__":
    OpenGLTSPSolver().run()
