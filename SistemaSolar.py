import pygame
import math

pygame.init()

# Cores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Sol
BLUE = (100, 100, 255)   # Terra
RED = (255, 0, 0)        # Marte
GREEN = (0, 255, 0)      # Mercúrio
BLACK = (0, 0, 0)

# Dimensões da tela
WIDTH, HEIGHT = 800, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador do Sistema Solar")

# Centro da tela (posição do Sol)
center = (WIDTH // 2, HEIGHT // 2)

# FPS (quadros por segundo)
FPS = 120
clock = pygame.time.Clock()

# Classe Planeta
class Planet:
    def __init__(self, radius, speed, size, texture):
        self.radius = radius  # Distância do Sol
        self.speed = speed  # Velocidade orbital
        self.size = size  # Tamanho do planeta
        self.angle = 0  # Ângulo inicial
        self.texture = texture  # Textura (imagem) do planeta

    def draw(self, window, center):
        # Calculando a posição do planeta em coordenadas cartesianas
        x = center[0] + self.radius * math.cos(self.angle)
        y = center[1] + self.radius * math.sin(self.angle)
        
        # Carregando e desenhando a imagem se houver textura
        planet_image = pygame.transform.scale(self.texture, (self.size * 2, self.size * 2))  # Escalando a imagem
        window.blit(planet_image, (x - self.size, y - self.size))  # Desenhando a imagem
        
        # Atualizando o ângulo para mover o planeta
        self.angle += self.speed

# Carregando as texturas dos planetas
mercury_texture = pygame.image.load('imagens/mercurio.png').convert_alpha()
earth_texture = pygame.image.load('imagens/terra.png').convert_alpha()
mars_texture = pygame.image.load('imagens/marte.png').convert_alpha()
jupiter_texture = pygame.image.load('imagens/jupiter.png').convert_alpha()

# Criando os planetas com as texturas
mercury = Planet(100, 0.03, 10, mercury_texture)  # Mercúrio
earth = Planet(200, 0.02, 20, earth_texture)        # Terra
mars = Planet(300, 0.015, 15, mars_texture)         # Marte
jupiter = Planet(400, 0.017, 18, jupiter_texture)    # Júpiter

planets = [mercury, earth, mars, jupiter]  # Adicionando Júpiter à lista de planetas

# Loop principal
running = True
while running:
    window.fill(BLACK)  # Cor de fundo
    
    # Desenhando o Sol
    pygame.draw.circle(window, YELLOW, center, 30)  # Sol

    # Desenhando e movimentando os planetas
    for planet in planets:
        planet.draw(window, center)
    
    # Verificando eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
