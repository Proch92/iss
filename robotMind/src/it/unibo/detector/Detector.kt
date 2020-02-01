/* Generated by AN DISI Unibo */ 
package it.unibo.detector

import it.unibo.kactor.*
import alice.tuprolog.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
	
class Detector ( name: String, scope: CoroutineScope ) : ActorBasicFsm( name, scope){
 	
	override fun getInitialState() : String{
		return "init"
	}
		
	override fun getBody() : (ActorBasicFsm.() -> Unit){
		
			val WithResource = true
			val MaxTrash = 2
			var CurrentTrash = 0
			val room = myai.Room()
			val dfs = myai.DFSUtil(room)
			val planner = myai.Planner(room)
			val StepDuration = 650
			var Goal : Pair<Int, Int> = Pair(0, 0)
			var Suspended = false
			var planexists = true
		return { //this:ActionBasciFsm
				state("init") { //this:State
					action { //it:State
					}
					 transition( edgeName="goto",targetState="init2", cond=doswitch() )
				}	 
				state("init2") { //this:State
					action { //it:State
						println("detector | init2")
						
								dfs.movedOn(Pair(0, 0))
								room.print()
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("idle") { //this:State
					action { //it:State
						println("detector | idle")
						
								if (WithResource) room.coapPublish(myself)
								room.print()
					}
					 transition(edgeName="t011",targetState="explore",cond=whenDispatch("explore"))
					transition(edgeName="t012",targetState="ssuspend",cond=whenDispatch("suspend"))
				}	 
				state("sleep") { //this:State
					action { //it:State
						println("detector | sleep")
					}
					 transition(edgeName="tsleep13",targetState="idle",cond=whenDispatch("wakeup"))
				}	 
				state("discharge") { //this:State
					action { //it:State
						println("detector | discharge")
						request("canDump", "canDump($CurrentTrash)" ,"plasticbox" )  
					}
					 transition(edgeName="twaitAccept14",targetState="goHome",cond=whenReply("dumpAccept"))
					transition(edgeName="twaitAccept15",targetState="notifyDumpFull",cond=whenReply("dumpFull"))
				}	 
				state("notifyDumpFull") { //this:State
					action { //it:State
						println("detector | notifyDumpFull")
						emit("boxCannotAccept", "boxCannotAccept(X)" ) 
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("goHome") { //this:State
					action { //it:State
						println("detector | goHome")
						
								Goal = Pair(0, 0)
								planexists = planner.new_plan(Goal)
								if (planexists) planner.executePlan(myself)
					}
					 transition( edgeName="goto",targetState="waitPlanCompletion", cond=doswitchGuarded({(planexists)}) )
					transition( edgeName="goto",targetState="idle", cond=doswitchGuarded({! (planexists)}) )
				}	 
				state("ssuspend") { //this:State
					action { //it:State
						println("detector | ssuspend")
						Suspended = true
						if((WithResource)){ kotlincode.coapSupport.updateResource(myself ,"robot/status", "status(suspended)" )
						 }
					}
					 transition( edgeName="goto",targetState="goHome", cond=doswitch() )
				}	 
				state("explore") { //this:State
					action { //it:State
						println("detector | explore")
						
								Suspended = false
								Goal = dfs.next()
								println(Goal)
								planner.new_plan(Goal)
								planner.executePlan(myself)
								room.print()
						if((WithResource)){ kotlincode.coapSupport.updateResource(myself ,"robot/status", "status(active)" )
						 }
					}
					 transition( edgeName="goto",targetState="waitPlanCompletion", cond=doswitch() )
				}	 
				state("waitPlanCompletion") { //this:State
					action { //it:State
						println("detector | waitPlanCompletion")
					}
					 transition(edgeName="twait16",targetState="checkGoal",cond=whenEvent("stepdone"))
					transition(edgeName="twait17",targetState="askObstacle",cond=whenEvent("stepfail"))
					transition(edgeName="twait18",targetState="ssuspend",cond=whenDispatch("suspend"))
					transition(edgeName="twait19",targetState="goHome",cond=whenDispatch("terminate"))
				}	 
				state("checkGoal") { //this:State
					action { //it:State
						println("detector | checkGoal")
						
								val cur_x = myai.RobotState.x
								val cur_y = myai.RobotState.y
								dfs.movedOn(Pair(cur_x, cur_y))
								room.print()
								if (WithResource) room.coapPublish(myself)
					}
					 transition( edgeName="goto",targetState="goalAchieved", cond=doswitchGuarded({(Pair(myai.RobotState.x, myai.RobotState.y) == Goal)}) )
					transition( edgeName="goto",targetState="waitPlanCompletion", cond=doswitchGuarded({! (Pair(myai.RobotState.x, myai.RobotState.y) == Goal)}) )
				}	 
				state("goalAchieved") { //this:State
					action { //it:State
						println("detector | goalAchieved")
						if((Goal == Pair(0, 0))){ forward("unload", "unload($CurrentTrash)" ,"plasticbox" ) 
						CurrentTrash = 0
						if(( WithResource )){ kotlincode.coapSupport.updateResource(myself ,"robot/box", "box($CurrentTrash)" )
						 }
						 }
					}
					 transition( edgeName="goto",targetState="explore", cond=doswitchGuarded({(Suspended == false)}) )
					transition( edgeName="goto",targetState="sleep", cond=doswitchGuarded({! (Suspended == false)}) )
				}	 
				state("askObstacle") { //this:State
					action { //it:State
						println("detector | askObstalce")
					}
					 transition(edgeName="task20",targetState="plasticFound",cond=whenEvent("itsPlastic"))
					transition(edgeName="task21",targetState="obstacleFound",cond=whenEvent("itsObstacle"))
					transition(edgeName="task22",targetState="ssuspend",cond=whenDispatch("suspend"))
					transition(edgeName="task23",targetState="goHome",cond=whenDispatch("terminate"))
				}	 
				state("plasticFound") { //this:State
					action { //it:State
						println("detector | plasticFound")
						
								CurrentTrash += 1
								val (gx, gy) = Goal
								room.put(gx, gy, myai.Type.FREE)
						if(( WithResource )){ kotlincode.coapSupport.updateResource(myself ,"robot/box", "box($CurrentTrash)" )
						 }
					}
					 transition( edgeName="goto",targetState="discharge", cond=doswitchGuarded({(MaxTrash == CurrentTrash)}) )
					transition( edgeName="goto",targetState="explore", cond=doswitchGuarded({! (MaxTrash == CurrentTrash)}) )
				}	 
				state("obstacleFound") { //this:State
					action { //it:State
						println("detector | obstacleFound")
						
								val (gx, gy) = Goal
								room.put(gx, gy, myai.Type.OBSTACLE)
					}
					 transition( edgeName="goto",targetState="explore", cond=doswitch() )
				}	 
			}
		}
}
