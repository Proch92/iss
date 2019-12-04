%====================================================================================
% basicrobot description   
%====================================================================================
mqttBroker("localhost", "1884").
context(ctxbasicrobot, "localhost",  "TCP", "8018").
 qactor( robotadapter, ctxbasicrobot, "itunibo.robot.robotAdapterQaStream").
  qactor( basicrobot, ctxbasicrobot, "it.unibo.basicrobot.Basicrobot").
  qactor( sentinel, ctxbasicrobot, "it.unibo.sentinel.Sentinel").
