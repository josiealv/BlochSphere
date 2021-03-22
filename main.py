from bloch_sphere.animate_bloch import do_or_save_animation, AnimState


@do_or_save_animation('my_animation', save=False, fps=20, preview=True)
# Or
# @do_or_save_animation('my_animation', save='gif', fps=20, preview=True)
# @do_or_save_animation('my_animation', save='mp4', fps=20, preview=False)
def animate(state: AnimState):
    state.x_gate()
    state.y_gate()
    state.s_gate()
    state.s_gate()
    ...
    state.wait()  # Pause at the end


if __name__ == '__main__':
    animate(AnimState)
