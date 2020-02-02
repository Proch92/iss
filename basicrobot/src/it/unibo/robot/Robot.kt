/* Generated by AN DISI Unibo */ 
package it.unibo.robot

import it.unibo.kactor.*
import alice.tuprolog.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
	
class Robot ( name: String, scope: CoroutineScope ) : ActorBasicFsm( name, scope){
 	
	override fun getInitialState() : String{
		return "s0"
	}
		
	override fun getBody() : (ActorBasicFsm.() -> Unit){
		return { //this:ActionBasciFsm
				state("s0") { //this:State
					action { //it:State
						println("init")
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("idle") { //this:State
					action { //it:State
						println("robot waiting")
					}
					 transition(edgeName="t00",targetState="handleCmd",cond=whenDispatch("cmd"))
					transition(edgeName="t01",targetState="handleObstacle",cond=whenEvent("obstacle"))
					transition(edgeName="t02",targetState="handeRemove",cond=whenEvent("remove"))
				}	 
				state("handleCmd") { //this:State
					action { //it:State
						println("$name in ${currentState.stateName} | $currentMsg")
						if( checkMsgContent( Term.createTerm("cmd(X)"), Term.createTerm("cmd(X)"), 
						                        currentMsg.msgContent()) ) { //set msgArgList
								forward("cmd", "cmd(${payloadArg(0)})" ,"robotadapter" ) 
						}
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("handeRemove") { //this:State
					action { //it:State
						println("hande remove")
						if( checkMsgContent( Term.createTerm("remove(NAME)"), Term.createTerm("remove(NAME)"), 
						                        currentMsg.msgContent()) ) { //set msgArgList
								forward("remove", "remove(${payloadArg(0)})" ,"robotadapter" ) 
						}
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("handleObstacle") { //this:State
					action { //it:State
						println("$name in ${currentState.stateName} | $currentMsg")
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
			}
		}
}
