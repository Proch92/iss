gradle -b build_ctxBasicRobot.gradle distZip
unzip build/distributions/basicrobot-1.0.zip -d build/distributions/distZip/
cp *.pl build/distributions/distZip/basicrobot-1/bin/
zip -ur build/distributions/basicrobot-1.0.zip build/distributions/distZip/