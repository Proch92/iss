package kotlincode

import org.eclipse.californium.core.CoapClient
import org.eclipse.californium.core.coap.MediaTypeRegistry
import org.eclipse.californium.core.CoapResponse
import it.unibo.kactor.ActorBasic

object coapSupport{
lateinit var client : CoapClient
lateinit var host   : String
	
	fun init( address : String ){
		host = address
 	}
	
	private fun setClientForPath( path : String ){
		val url = host + "/" + path
		client = CoapClient( url )
		client.setTimeout( 1000L )
	}
	
	fun updateResource( owner : ActorBasic, path: String, msg : String ){
		setClientForPath( path )
		//println("coapSupport | updateResource $msg")
		val resp : CoapResponse = client.put(msg, MediaTypeRegistry.TEXT_PLAIN)
		//println("coapSupport | updateResource respCode=${resp.getCode()}")
	}
	
	fun readResource(  owner : ActorBasic, path : String ){
		setClientForPath( path )
		val respGet : CoapResponse = client.get( )
		val v = respGet.getResponseText()
		println("coapSupport | readResource v=$v")
	}
}
