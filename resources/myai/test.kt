package myai

fun main() {
    val room = Room()
    val planner = Planner(room)
    planner.room.put(0,0,Type.ROBOT)
    planner.room.put(2,0,Type.OBSTACLE)
    planner.room.put(2,1,Type.OBSTACLE)
    planner.room.put(0,2,Type.OBSTACLE)
    planner.room.put(1,2,Type.OBSTACLE)
    planner.room.print()

    val dfs = DFSUtil(room)
    dfs.movedOn(Pair(0, 0))
    var pre = Pair(0, 0)
    while (!dfs.isDone()) {
        val nextcell = dfs.next()
        println(nextcell)
        dfs.movedOn(nextcell)
        val (x, y) = nextcell
        val (px, py) = pre
        room.put(px, py, Type.FREE)
        room.put(x, y, Type.ROBOT)
        pre = Pair(x, y)
        room.print()
    }
}