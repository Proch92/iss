%====================================================================================
% sprint1 description   
%====================================================================================
context(ctxbasicrobot, "localhost",  "TCP", "8018").
context(ctxrobotappl0, "localhost",  "TCP", "8033").
context(ctxradargui, "localhost",  "TCP", "8038").
 qactor( basicrobot, ctxbasicrobot, "external").
  qactor( radargui, ctxradargui, "external").
  qactor( appl0, ctxrobotappl0, "it.unibo.appl0.Appl0").
