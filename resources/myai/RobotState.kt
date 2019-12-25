package myai

enum class Direction {NORTH, EAST, SOUTH, WEST}

object RobotState {
    var x : Int
    var y : Int
    var dir : Direction
	
	init {
		x = 0
		y = 0
		dir = SOUTH
	}

    fun update(move : String) {
		if (move == "step") {
			when(dir) {
				NORTH -> y -= 1
				EAST -> x += 1
				SOUTH -> y += 1
				WEST -> x -= 1
			}
		}
		else {
			when(dir) {
				NORTH -> {
					if (move == "a") dir = WEST
					if (move == "d") dir = EAST
				}
				EAST -> {
					if (move == "a") dir = NORTH
					if (move == "d") dir = SOUTH
				}
				SOUTH -> {
					if (move == "a") dir = EAST
					if (move == "d") dir = WEST
				}
				WEST -> {
					if (move == "a") dir = SOUTH
					if (move == "d") dir = NORTH
				}
			}
		}
		
	}
	
	fun print() {
		val sdir : String = when(dir) {
			NORTH -> "north"
			EAST -> "east"
			SOUTH -> "south"
			WEST -> "west"
		}
		println("x: $x, y:$y, dir: $sdir")
	}
}