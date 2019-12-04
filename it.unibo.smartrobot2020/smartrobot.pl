%====================================================================================
% smartrobot description   
%====================================================================================
mqttBroker("localhost", "1884").
context(ctxsmartrobot, "localhost",  "MQTT", "8020").
context(ctxbasicrobot, "192.168.1.5",  "MQTT", "8018").
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( smartrobot, ctxsmartrobot, "it.unibo.smartrobot.Smartrobot").
