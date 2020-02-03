/*
* =====================================
* TcpClientToVirtual.js
* =====================================
*/
const net = require('net');

exports.sendMsg = function ( msg ){
 	var client = new net.Socket();
 	console.log(client);
 	client.connect(8999, '127.0.0.1', function() {
		client.write(msg);
 	})
}
