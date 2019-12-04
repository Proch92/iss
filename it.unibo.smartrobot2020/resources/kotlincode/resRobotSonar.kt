package kotlincode

import org.eclipse.californium.core.CoapResource
import org.eclipse.californium.core.server.resources.CoapExchange
import org.eclipse.californium.core.coap.CoAP.ResponseCode.CHANGED;
import org.eclipse.californium.core.coap.CoAP.ResponseCode.CREATED;
import org.eclipse.californium.core.coap.CoAP.ResponseCode.DELETED;
import org.eclipse.californium.core.CoapServer
import it.unibo.kactor.ActorBasic

class resRobotSonar( val owner: ActorBasic, name : String) : CoapResource( name ){
	var distance = "0";
	
	init{
		setObservable(true)
		println("resource $name  | created  " );		
	}
	override fun handleGET( exchange : CoapExchange ) {
		println("resource $name  | GET: ${exchange.getRequestText()} distance=$distance")
		exchange.respond( distance );
	}
//	override fun handlePOST( exchange : CoapExchange ) {
//	}
	override fun handlePUT( exchange : CoapExchange) {
		distance = exchange.getRequestText()
		changed()	// notify all CoAp observers
		exchange.respond(CHANGED)
	}
//	override fun handleDELETE( exchange : CoapExchange) {
//		delete();
//		exchange.respond(DELETED);
//	}
	
}