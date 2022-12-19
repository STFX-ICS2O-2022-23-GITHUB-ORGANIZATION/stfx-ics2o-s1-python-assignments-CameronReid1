import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
bg_color = (0, 0, 0)

# Create a list to store the objects
objects = []

# Define a class for the objects
class Object:
  def __init__(self, x, y, width, height, color, x_velocity, y_velocity):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.x_velocity = x_velocity
    self.y_velocity = y_velocity
 
  def update(self):
    # Update the object's position
    self.x += self.x_velocity
    self.y += self.y_velocity
   
    # Keep the object on the screen
    if self.x < 0 or self.x + self.width > screen_width:
      self.x_velocity = -self.x_velocity
    if self.y < 0 or self.y + self.height > screen_height:
      self.y_velocity = -self.y_velocity
 
  def draw(self):
    # Draw the object on the screen
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Create some objects and add them to the list
for i in range(5):
  x = random.randint(0, screen_width - 50)
  y = random.randint(0, screen_height - 50)
  width = 50
  height = 50
  color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  x_velocity = random.randint(-5, 5)
  y_velocity = random.randint(-5, 5)
  objects.append(Object(x, y, width, height, color, x_velocity, y_velocity))

# Set the game loop to run at 60 FPS
clock = pygame.time.Clock()

# Run the game loop
while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
 
  # Update the objects
  for obj in objects:
    obj.update()
 
  # Clear the screen
  screen.fill(bg_color)
 
  # Draw the objects
  for obj in objects:
    obj.draw()
 
  # Update the display
  pygame.display.flip()
 
  # Limit the frame rate
  clock.tick(60)
