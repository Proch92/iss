/* Generated by AN DISI Unibo */ 
package it.unibo.ctxMind
import it.unibo.kactor.QakContext
import it.unibo.kactor.sysUtil
import kotlinx.coroutines.runBlocking

fun main() = runBlocking {
	QakContext.createContexts(
	        "192.168.1.92", this, "robotmind.pl", "sysRules.pl"
	)
}

