import random, time
from pyglet.window.key import MOTION_UP, MOTION_DOWN, MOTION_LEFT, MOTION_RIGHT
from env.snake_env import SnakeEnv

def interact():
    """
    Human interaction with the environment
    """
    env = SnakeEnv()
    done = False
    r = 0
    action = random.randrange(4)
    delay_time = 0.4

    # After the first run of the method env.render()
    # env.renderer.viewer obtains an attribute 'window'
    # which is a pyglet.window.Window object
    env.render(mode='human')

    # Let's control snake movements using window events
    # To change its direction press Left, Right, Up or Down arrows
    @env.renderer.viewer.window.event
    def on_text_motion(motion):
        nonlocal action
        if motion == MOTION_UP:
            action = 0
        elif motion == MOTION_DOWN:
            action = 2
        elif motion == MOTION_LEFT:
            action = 3
        elif motion == MOTION_RIGHT:
            action = 1

    while not done:
        time.sleep(delay_time)
        obs, reward, done, info = env.step(action)
        env.render(mode='human')
        if reward:
            r += reward
            # Let's speed up our snake after a good dinner ;-)
            delay_time -= 1/3 * delay_time
    return r

if __name__ == '__main__':
    interact()