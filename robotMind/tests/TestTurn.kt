package tests

import org.junit.Assert.assertTrue
import org.junit.Assert.fail
import org.junit.After
import org.junit.Before
import org.junit.Test
import kotlinx.coroutines.launch
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import org.eclipse.californium.core.CoapClient
import org.eclipse.californium.core.coap.MediaTypeRegistry
import org.eclipse.californium.core.CoapResponse

class TestTurn {
	lateinit var client : CoapClient
	
	@Before
	fun systemSetUp() {
		//client = CoapClient("coap://localhost:5683")
  	 	GlobalScope.launch{
 			println("%%%%%%% start context")
			it.unibo.ctxMind.main()
 		}
 		delay(3000)		//give the time to start
 	}
 
	@After
	fun terminate() {
		println("%%%%%%% Test terminated")
	}
 
	@Test
	fun moveTest() {
		client = CoapClient("coap://localhost:5683/robot/pos")
		client.setTimeout(1000L)
		client.put("a", MediaTypeRegistry.TEXT_PLAIN)
		delay(2000)
		val newPos = client.get().getResponseText()
		assertTrue("", newPos == "(0, 0) / EST")
 	}

	fun delay( time : Long ){
		Thread.sleep( time )
	}
}