package kotlincode

import org.eclipse.californium.core.CoapResource
import org.eclipse.californium.core.server.resources.CoapExchange
import org.eclipse.californium.core.coap.CoAP.ResponseCode.CHANGED;
import org.eclipse.californium.core.coap.CoAP.ResponseCode.CREATED;
import org.eclipse.californium.core.coap.CoAP.ResponseCode.DELETED;
import org.eclipse.californium.core.CoapServer
import it.unibo.kactor.ActorBasic

class resRobotMap( val owner: ActorBasic, name : String) : CoapResource( name ){
	var map = "";
	
	init{
		setObservable(true)
		println("resource $name  | created  " );		
	}
	override fun handleGET( exchange : CoapExchange ) {
		println("resource $name  | GET: ${exchange.getRequestText()} map=$map")
		exchange.respond( map );
	}
//	override fun handlePOST( exchange : CoapExchange ) {
//	}
	override fun handlePUT( exchange : CoapExchange) {
		map = exchange.getRequestText()
		changed()	// notify all CoAp observers
		exchange.respond(CHANGED)
	}
//	override fun handleDELETE( exchange : CoapExchange) {
//		delete();
//		exchange.respond(DELETED);
//	}
	
}
