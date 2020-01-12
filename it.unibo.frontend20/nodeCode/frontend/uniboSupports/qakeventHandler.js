/*
qakeventHandler.js
*/
var io  ; 	//Upgrade for socketIo;

exports.setIoSocket = function ( iosock ) {	//called by
 	io    = iosock;
	console.log("		qakeventHandler | SETIOSOCKET (to update the page) "  );
}

exports.handeData = function ( response ){
	console.log(response)
	var msgStr = response.payload;
	console.log("		qakeventHandler | handeData: " + msgStr);
	io.sockets.send( msgStr );
}
