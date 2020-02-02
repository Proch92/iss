/*
* =====================================
* TcpClientToVirtual.js
* =====================================
*/
var   net    = require('net');

var socket = null;


function sendMsg( msg ){
 		if( socket == null ){
 	  		console.log('TcpClientToVirtual ATTEMPTS CONNECTION ...'  );
			socket = net.connect({ port: 8999, host: "localhost" });
   			socket.setEncoding('utf8');
			
			// when receive data back, print to console
			socket.on('data',function(data) {
				console.log(data);
			});
			
			// when server closed
			socket.on('close',function() {
				console.log('connection is closed');
			});
			socket.on('end',function() {
				console.log('connection is ended');
			});
			socket.on('error',function() {
				console.log('	TcpClientToVirtual WARNING connection with virtual not possible');
			});
		
		}else
		socket.write(msg+"\n");
 }

//===============================================================

process.on('exit', function(code){
	console.log("Exiting code= " + code );
});

//See https://coderwall.com/p/4yis4w/node-js-uncaught-exceptions
process.on('uncaughtException', function (err) {
//cursor.reset().fg.red();
	console.error('TcpClientToVirtual got uncaught exception:', err.message);
//cursor.reset();
//	process.exit(1);		//MANDATORY!!!
});

//===============================================================



module.exports = sendMsg; 
