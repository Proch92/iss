package myai

import myai.Direction.*

fun move(goal : Pair<Int, Int>) : String {
	val state = myai.RobotState
    val direction = when(goal) {
        Pair(state.x+1, state.y) -> EAST
        Pair(state.x-1, state.y) -> WEST
        Pair(state.x, state.y+1) -> SOUTH
        Pair(state.x, state.y-1) -> NORTH
        else -> SOUTH
    }
    if (state.dir == direction) return "step"
    if (state.dir == NORTH) {
        if (direction == EAST) return "d"
        if (direction == WEST) return "a"
    }
    if (state.dir == EAST) {
        if (direction == SOUTH) return "d"
        if (direction == NORTH) return "a"
    }
    if (state.dir == SOUTH) {
        if (direction == WEST) return "d"
        if (direction == EAST) return "a"
    }
    if (state.dir == WEST) {
        if (direction == NORTH) return "d"
        if (direction == SOUTH) return "a"
    }
    return "a"
}