/* Generated by AN DISI Unibo */ 
package it.unibo.plasticbox

import it.unibo.kactor.*
import alice.tuprolog.*
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
	
class Plasticbox ( name: String, scope: CoroutineScope ) : ActorBasicFsm( name, scope){
 	
	override fun getInitialState() : String{
		return "init"
	}
		
	override fun getBody() : (ActorBasicFsm.() -> Unit){
		
			val NPB=10
			var bottles=0
			var acceptDump = true
			val WithResource = true
		return { //this:ActionBasciFsm
				state("init") { //this:State
					action { //it:State
						if(( WithResource )){ kotlincode.coapSupport.updateResource(myself ,"plasticBox/content", "plasticBox($bottles)" )
						 }
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("idle") { //this:State
					action { //it:State
					}
					 transition(edgeName="t020",targetState="dump",cond=whenDispatch("unload"))
					transition(edgeName="t021",targetState="handleReq",cond=whenRequest("canDump"))
				}	 
				state("dump") { //this:State
					action { //it:State
						println("plasticBox | dump")
						if( checkMsgContent( Term.createTerm("unload(NBOTTLES)"), Term.createTerm("unload(X)"), 
						                        currentMsg.msgContent()) ) { //set msgArgList
								
											val nb_dump = payloadArg(0).toInt()
											bottles += nb_dump
								if(( WithResource )){ kotlincode.coapSupport.updateResource(myself ,"plasticBox/content", "plasticBox($bottles)" )
								 }
						}
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
				state("handleReq") { //this:State
					action { //it:State
						println("plasticBox | handleReq")
						if( checkMsgContent( Term.createTerm("canDump(NBOTTLES)"), Term.createTerm("canDump(X)"), 
						                        currentMsg.msgContent()) ) { //set msgArgList
								
											val nb_dump = payloadArg(0).toInt()
											acceptDump = (nb_dump <= (NPB - bottles))
						}
						if((acceptDump)){ answer("canDump", "dumpAccept", "dumpAccept(X)"   )  
						 }
						else
						 { answer("canDump", "dumpFull", "dumpFull(X)"   )  
						  }
					}
					 transition( edgeName="goto",targetState="idle", cond=doswitch() )
				}	 
			}
		}
}
