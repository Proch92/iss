%====================================================================================
% basicrobot description   
%====================================================================================
mqttBroker("localhost", "1884").
context(ctxbasicrobot, "172.0.0.1",  "MQTT", "8030").
 qactor( robotadapter, ctxbasicrobot, "itunibo.robot.robotAdapterQaStream").
  qactor( robot, ctxbasicrobot, "it.unibo.robot.Robot").
