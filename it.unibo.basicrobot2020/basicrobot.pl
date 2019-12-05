%====================================================================================
% basicrobot description   
%====================================================================================
mqttBroker("localhost", "1884").
context(ctxbasicrobot, "localhost",  "TCP", "8018").
context(ctxpython, "192.168.43.229",  "TCP", "8030").
 qactor( robotadapter, ctxpython, "external").
  qactor( basicrobot, ctxbasicrobot, "it.unibo.basicrobot.Basicrobot").
  qactor( sentinel, ctxbasicrobot, "it.unibo.sentinel.Sentinel").
