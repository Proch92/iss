package mystuff

import mystuff.SparseMatrix

enum class Type {
	FREE, ROBOT, OBSTACLE, PLASTIC, UNKOWN
}

enum class TypeStr {
	" ", "r", "X", "!", "?"
}

object Map {
	private map : SparseMatrix<Type> = SparseMatrix()

	fun get(x, y) : Type {
		try {
			return map.get(x, y)
		} catch (e: IllegalArgumentException) {
			return Type.UNKOWN
		}
	}

	fun put(x, y, type :Type) {
		map.put(x, y, type)
	}

	fun print() {
		for (_ in 0..map.max_y) print("_")
		println("")

		for (x in 0..map.max_x) {
			print("|")
			for (y in 0..map.max_y) {
				print(get(x, y) as TypeStr)
			}
			println("")
		}
	}
}