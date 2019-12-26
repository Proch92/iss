package myai

import kotlinx.coroutines.*
import kotlin.math.abs
import it.unibo.kactor.*
import myai.*

data class Node (var parent: Node?, var cell: Pair<Int, Int>)

class Planner (room: Room) {
    var room = room
    private var plan : MutableList<Pair<Int, Int>> = mutableListOf()

    fun new_plan (goal:Pair<Int, Int>) : Boolean {
        var queue : MutableList<Node> = mutableListOf()
        var visited : MutableSet<Pair<Int, Int>> = mutableSetOf()
		val start : Pair<Int, Int> = Pair(RobotState.x, RobotState.y)

        fun isValidEntry(x:Int, y:Int) : Boolean {
            if (x < 0 || y < 0)
                return false
            if (visited.contains(Pair(x, y)))
                return false
            if (room.get(x, y) in listOf(myai.Type.UNKNOWN, myai.Type.OBSTACLE, myai.Type.PLASTIC))
                return false
            return true
        }

        plan = mutableListOf()

        val root = Node(null, cell = start)
        queue.add(root)
        while (queue.isNotEmpty()) {
            var node = queue.removeAt(0)
            visited.add(node.cell)

            if (isAdjacent(node.cell, goal)) {
                plan.add(goal)
                while (node != root) {
                    plan.add(node.cell)
                    node = node.parent!!
                }
                plan = plan.reversed().toMutableList()
                
				println("plan found")
                return true
            }

            val (x, y) = node.cell
            if (isValidEntry(x-1, y)) queue.add(Node(node, Pair(x-1, y)))
            if (isValidEntry(x+1, y)) queue.add(Node(node, Pair(x+1, y)))
            if (isValidEntry(x, y-1)) queue.add(Node(node, Pair(x, y-1)))
            if (isValidEntry(x, y+1)) queue.add(Node(node, Pair(x, y+1)))
        }
        println("couldn't find a suitable plan")
        return false
    }

    fun isAdjacent(c0: Pair<Int, Int>, c1: Pair<Int, Int>) : Boolean {
        return manhattan(c0, c1) == 1
    }

    fun manhattan(c0: Pair<Int, Int>, c1: Pair<Int, Int>) : Int {
        val (x0, y0) = c0
        val (x1, y1) = c1

        return abs(x1 - x0) + abs(y1 - y0)
    }

    suspend fun executePlan(actor : ActorBasic) {
    	while (!isPlanDone()) {
			val nextc = nextCell()
			var nextmove = move(nextc)
			while (nextmove != "step") {
				println(nextmove)
				actor.forward("cmd", "cmd($nextmove)", "robotmind")
				//Thread.sleep(750)
				delay(750)
				nextmove = move(nextc)
			}
			actor.forward("step", "step(500)", "robotmind")
		}
    }

    fun nextCell() : Pair<Int, Int> {
        return plan.removeAt(0)
    }
	
	fun isPlanDone() : Boolean {
		return plan.isEmpty()
	}
}
