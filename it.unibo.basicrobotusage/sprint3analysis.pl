%====================================================================================
% sprint3analysis description   
%====================================================================================
mqttBroker("localhost", "1883").
context(ctxrobotappl0, "localhost",  "MQTT", "8033").
 qactor( robotappl0, ctxrobotappl0, "it.unibo.robotappl0.Robotappl0").
  qactor( consolesimulator, ctxrobotappl0, "it.unibo.consolesimulator.Consolesimulator").
