package myai

enum class Direction {NORTH, EAST, SOUTH, WEST}

object RobotState {
    var x : Int
    var y : Int
    var dir : Direction
	
	init {
		x = 0
		y = 0
		dir = Direction.SOUTH
	}

    fun update(move : String) {
		if (move == "step") {
			when(dir) {
				Direction.NORTH -> y -= 1
				Direction.EAST -> x += 1
				Direction.SOUTH -> y += 1
				Direction.WEST -> x -= 1
			}
		}
		else {
			when(dir) {
				Direction.NORTH -> {
					if (move == "a") dir = Direction.WEST
					if (move == "d") dir = Direction.EAST
				}
				Direction.EAST -> {
					if (move == "a") dir = Direction.NORTH
					if (move == "d") dir = Direction.SOUTH
				}
				Direction.SOUTH -> {
					if (move == "a") dir = Direction.EAST
					if (move == "d") dir = Direction.WEST
				}
				Direction.WEST -> {
					if (move == "a") dir = Direction.SOUTH
					if (move == "d") dir = Direction.NORTH
				}
			}
		}
		
	}
	
	fun print() {
		val sdir : String = when(dir) {
			Direction.NORTH -> "north"
			Direction.EAST -> "east"
			Direction.SOUTH -> "south"
			Direction.WEST -> "west"
		}
		println("x: $x, y:$y, dir: $sdir")
	}
}