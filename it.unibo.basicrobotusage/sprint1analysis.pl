%====================================================================================
% sprint1analysis description   
%====================================================================================
mqttBroker("192.168.43.229", "1883").
context(ctxbasicrobot, "192.168.43.171",  "MQTT", "0").
context(ctxrobotappl0, "localhost",  "TCP", "8033").
context(ctxradargui, "192.168.43.5",  "MQTT", "0").
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( radargui, ctxradargui, "external").
  qactor( robotappl0, ctxrobotappl0, "it.unibo.robotappl0.Robotappl0").
