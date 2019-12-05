%====================================================================================
% test description   
%====================================================================================
context(ctxtest, "localhost",  "TCP", "8020").
context(ctxpython, "192.168.43.229",  "TCP", "8030").
 qactor( robot, ctxpython, "external").
  qactor( source, ctxtest, "it.unibo.source.Source").
