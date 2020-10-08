from had import State
import pyglet

green_image = pyglet.image.load('green.png')
red_image = pyglet.image.load('apple.png')

state = State()

TILE_SIZE = 64

window = pyglet.window.Window()

state.width = window.width // TILE_SIZE
state.height = window.height // TILE_SIZE

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

    for x, y in state.snake:
        green_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)

    for x, y in state.food:
        red_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)   

@window.event
def on_key_press(symbol, mod):
    if symbol == pyglet.window.key.LEFT:
        state.snake_direction = -1, 0
    if symbol == pyglet.window.key.RIGHT:
        state.snake_direction = 1, 0
    if symbol == pyglet.window.key.DOWN:
        state.snake_direction = 0, -1
    if symbol == pyglet.window.key.UP:
        state.snake_direction = 0, 1
        
def move(dt):
    state.move()

pyglet.clock.schedule_interval(move, 1/5)

pyglet.app.run()