package myai

import it.unibo.kactor.ActorBasic

enum class Type {FREE, ROBOT, OBSTACLE, PLASTIC, UNKNOWN}

class Room {
	private var room : SparseMatrix<Type> = SparseMatrix()

	fun get(x:Int, y:Int) : Type {
		return try {
			room.get(x, y)
		} catch (e: IllegalArgumentException) {
			Type.UNKNOWN
		}
	}

	fun put(x:Int, y:Int, type :Type) {
		room.put(x, y, type)
	}

	fun coapPublish(actor:ActorBasic) {
		var serialized = ""
		for (y in 0..room.max_y) {
			for (x in 0..room.max_x) {
				serialized += typeToString(get(x, y))
			}
			serialized += "|"
		}

		kotlincode.coapSupport.updateResource(actor, "env/map", serialized)
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

	private fun typeToString(type:Type) : String {
		return when (type) {
			Type.OBSTACLE -> "X"
			Type.FREE -> "."
			Type.PLASTIC -> "!"
			Type.ROBOT -> "r"
			Type.UNKNOWN -> "?"
		}
	}
}