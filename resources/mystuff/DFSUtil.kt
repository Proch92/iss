package mystuff

object DFSUtil {
	private var visited : MutableSet<Pair> = setOf()
	private var stack : MutableList<Pair> = mutableListOf()
	
	fun movedOn(x:int, y:int) {
		visited.add(Pair(x, y))
		if (isValidEntry(x-1, y)) stack.add(Pair(x-1, y))
		if (isValidEntry(x+1, y)) stack.add(Pair(x+1, y))
		if (isValidEntry(x, y-1)) stack.add(Pair(x, y-1))
		if (isValidEntry(x, y+1)) stack.add(Pair(x, y+1))
	}
	
	fun isValidEntry(x:int, y:int) : Boolean {
		if (x < 0 || y < 0)
			return false
		if (visited.contains(Pair(x, y)))
			return false
		return true
	}
	
	fun next() : Pair {
		return stack.pop()
	}
}