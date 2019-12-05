package kotlincode

import org.eclipse.californium.core.CoapResource
import org.eclipse.californium.core.server.resources.CoapExchange
import org.eclipse.californium.core.coap.CoAP.ResponseCode.CHANGED;
import org.eclipse.californium.core.coap.CoAP.ResponseCode.CREATED;
import org.eclipse.californium.core.coap.CoAP.ResponseCode.DELETED;
import org.eclipse.californium.core.CoapServer
import it.unibo.kactor.ActorBasic
import it.unibo.kactor.MsgUtil
import kotlinx.coroutines.launch

enum class Direction( ){
	SUD, EAST, NORTH, WEST
}

class resRobotPosition( val owner: ActorBasic, name : String) : CoapResource( name ){
 	var pos        = Pair<Int,Int>(0,0)
	var direction  = Direction.SUD
	var moving     = false
	
	init{
		setObservable(true)
		println("resource $name  | created  " );		
	}
	override fun handleGET( exchange : CoapExchange ) {
		//println("resource $name  | GET: ${exchange.getRequestText()} pos=$pos moving=$moving" )
//		if( moving ) exchange.respond( "pos unknown / $direction / moving=$moving" )
//		else
			exchange.respond( "$pos / $direction"  )  // moving=$moving" 
	}
//	override fun handlePOST( exchange : CoapExchange ) {
//	}
	override fun handlePUT( exchange : CoapExchange) {
		val msg = exchange.getRequestText()
		println("resource $name  | PUT: $msg")
		when( msg ){
			"p" ->  { moving = true;   stepTheOwner( )  }
			"a" ->  { moving = false;  rotateLeft( )    }
			"d" ->  { moving = false;  rotateRight()    }
			"h" ->  { moving = false;  cmdToOwner("h")  }
			"w" ->  { moving = true;   cmdToOwner("w")  }
			"s" ->  { moving = true;   cmdToOwner("s")  }
			"up" -> { updatePos()                       }
			"ua" -> { rotateLeft( )                     }
			"ud" -> { rotateRight()                     }
 			//else -> println("")
		}
		changed()	// notify all CoAp observers
 		exchange.respond(CHANGED)
	}
	
	fun cmdToOwner(msg: String){
		owner.scope.launch{ MsgUtil.sendMsg("cmd","cmd($msg)",owner) }
	}
	fun stepTheOwner( ){
		val msg = MsgUtil.buildDispatch(owner.name,"step","step(370)",owner.name )
		owner.scope.launch{ MsgUtil.sendMsg(msg,owner) }
		//The result of the move is given by the position of the robot
	}
	
	fun updatePos( ){
		val X = pos.first.toInt()
		val Y = pos.second.toInt()
		when( direction ){
			Direction.SUD   -> pos = Pair(X,Y+1)
			Direction.EAST  -> pos = Pair(X+1,Y)
			Direction.NORTH -> pos = Pair(X,Y-1)
			Direction.WEST  -> pos = Pair(X-1,Y)
		}
	}
	
	fun rotateLeft( ){
 		when( direction ){
			Direction.SUD    -> direction  = Direction.EAST
			Direction.EAST   -> direction =  Direction.NORTH
			Direction.NORTH  -> direction =  Direction.WEST
			Direction.WEST   -> direction =  Direction.SUD 
		}
	}
	
	fun rotateRight( ){
 		when( direction ){
			Direction.SUD    -> direction  = Direction.WEST
			Direction.EAST   -> direction =  Direction.SUD
			Direction.NORTH  -> direction =  Direction.EAST
			Direction.WEST   -> direction =  Direction.NORTH 
		}
	}
	
//	override fun handleDELETE( exchange : CoapExchange) {
//		delete();
//		exchange.respond(DELETED);
//	}
	
}