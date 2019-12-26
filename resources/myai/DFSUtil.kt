package myai

class DFSUtil (room: Room) {
	private var visited : MutableSet<Pair<Int, Int>> = mutableSetOf()
	private var stack : MutableList<Pair<Int, Int>> = mutableListOf()
	var room = room
	
	fun movedOn(cell : Pair<Int, Int>) {
		visited.add(cell)
		val (x, y) = cell
		room.put(x, y, Type.FREE)
		if (isValidEntry(x-1, y)) stack.add(Pair(x-1, y))
		if (isValidEntry(x+1, y)) stack.add(Pair(x+1, y))
		if (isValidEntry(x, y-1)) stack.add(Pair(x, y-1))
		if (isValidEntry(x, y+1)) stack.add(Pair(x, y+1))
	}
	
	fun isValidEntry(x:Int, y:Int) : Boolean {
		if (x < 0 || y < 0)
			return false
		if (visited.contains(Pair(x, y)))
			return false
		if (room.get(x, y) == Type.OBSTACLE)
			return false
		return true
	}
	
	fun next() : Pair<Int, Int> {
		return stack.removeAt(stack.lastIndex)
	}

	fun isDone() : Boolean {
		return stack.isEmpty()
	}
}