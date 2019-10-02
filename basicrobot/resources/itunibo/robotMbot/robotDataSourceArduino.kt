package itunibo.robotMbot

import it.unibo.kactor.ActorBasicFsm
import kotlinx.coroutines.launch
import java.io.BufferedReader
import it.unibo.kactor.ActorBasic
import it.unibo.kactor.MsgUtil
import it.unibo.kactor.ApplMessage
import alice.tuprolog.Term
import alice.tuprolog.Struct

class  robotDataSourceArduino( name : String, val owner : ActorBasicFsm , val conn : SerialPortConnSupport  
		  ) : ActorBasic(name, owner.scope){
		
	init{
		//scope.launch{  autoMsg("start","start(1)") }		 
	}

	override suspend fun actorBody(msg: ApplMessage) {
 		val vStr  = (Term.createTerm( msg.msgContent()) as Struct).getArg(0).toString()
        //println("   $name |  handles msg= $msg  vStr=$vStr")
		elabData( vStr )
	}

	suspend fun elabData(data : String ){
                while (true) {
 						try {
							var curDataFromArduino = conn.receiveALine()
							//globalTimer.startTimer()  //TIMER ....
 	 						//println("getDataFromArduino received: $curDataFromArduino"    )
 							var v = curDataFromArduino.toDouble() 
							//handle too fast change ?? NOT HERE
  							var dataSonar = v.toInt();							
							//println("mbotSupport sonar: ${ dataSonar }"   );								
						    //JUNE 2019 (streaming)
							val event = MsgUtil.buildEvent( name,"sonarRobot","sonar( $dataSonar )")								
							//owner.scope.launch{ owner.emitLocalStreamEvent(event) }
 							emit(  event )
						} catch ( e : Exception) {
 							println("getDataFromArduino | ERROR $e   ")
                    }
				}
	}
	
 
}