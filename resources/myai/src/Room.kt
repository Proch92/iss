package myai

enum class Type {FREE, ROBOT, OBSTACLE, PLASTIC, UNKOWN}

class Room {
	private var room : SparseMatrix<Type> = SparseMatrix()

	fun get(x:Int, y:Int) : Type {
		try {
			return room.get(x, y)
		} catch (e: IllegalArgumentException) {
			return Type.UNKOWN
		}
	}

	fun put(x:Int, y:Int, type :Type) {
		room.put(x, y, type)
	}

	fun print() {
		print(" ")
		for (i in 0..room.max_x) print("_")
		println("")

		for (y in 0..room.max_y) {
			print("|")
			for (x in 0..room.max_x) {
				print(typeToString(get(x, y)))
			}
			println("")
		}
	}

	fun typeToString(type:Type) : String {
		when (type) {
			Type.OBSTACLE -> return "X"
			Type.FREE -> return " "
			Type.PLASTIC -> return "!"
			Type.ROBOT -> return "r"
			Type.UNKOWN -> return "?"
		}
	}
}