package myai

data class Node (var parent: Node?, var cell: Pair<Int, Int>)

class Planner (room: Room) {
    var room = room
    private var plan : MutableList<Pair<Int, Int>> = mutableListOf()

    fun new_plan (start:Pair<Int, Int>, goal:Pair<Int, Int>) : Boolean {
        var queue : MutableList<Node> = mutableListOf()
        var visited : MutableSet<Pair<Int, Int>> = mutableSetOf()

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

            if (node.cell == goal) {
                while (node != root) {
                    plan.add(node.cell)
                    node = node.parent!!
                }
                plan = plan.reversed().toMutableList()

                return true
            }

            val (x, y) = node.cell
            if (isValidEntry(x-1, y)) queue.add(Node(node, Pair(x-1, y)))
            if (isValidEntry(x+1, y)) queue.add(Node(node, Pair(x+1, y)))
            if (isValidEntry(x, y-1)) queue.add(Node(node, Pair(x, y-1)))
            if (isValidEntry(x, y+1)) queue.add(Node(node, Pair(x, y+1)))
        }

        return false
    }

    fun nextMove() : Pair<Int, Int> {
        return plan.removeAt(0)
    }
}
