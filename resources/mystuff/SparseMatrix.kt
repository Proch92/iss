package mystuff

class SparseMatrix<T> {
	private var mat : MutableMap<Pair, T> = mutableMapOf()
	var max_x = 0
	var max_y = 0

	fun get(x, y) : T {
		coord = Pair(x, y)
		if (mat.keys.contains(coord)) {
			return mat.get(coord)
		}
		else {
			throw IllegalArgumentException("accessing a non existing key")
		}
	}

	fun put(x:int, y:int, v:T) {
		if (x > max_x) max_x = x
		if (y > max_y) max_y = y
		coord = Pair(x, y)
		mat.put(coord, v)
	}
}