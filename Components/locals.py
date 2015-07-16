
# General things:
RIGHT = 1
LEFT = 2
TOP = 3
BOTTOM = 4

# Names of layers
class Layers:
	game_actors = 4
	main = 3
	sticky_background = 2
	background = 1
	background_color = 0

# Message names: (MSGNs)
class MSGN:
	COLLISION_SIDES = 0
	VELOCITY = 1

	WARIO_STATE = 100
	WARIO_LOOKDIRECTION = 101
	WARIO_STATESTACK = 102


# Warios states:
class WarioStates:
	UPRIGHT_STAY = 0
	UPRIGHT_MOVE = 1

	CROUCH_STAY = 2
	CROUCH_MOVE = 3

	JUMP_STAY = 4
	JUMP_MOVE = 5

	FALL_STAY = 6
	FALL_MOVE = 7

	GOTO_SLEEP = 8
	WAKE_UP = 9
	SLEEP = 10

	TURN = 11
