DEPLOY_FOLDERNAME = 'dist'

unzip build/distributions/basicrobot-1.0.zip -d build/distributions/deploy/
cp *.pl build/distributions/deploy/*/bin/
#zip -ur build/distributions/basicrobot-1.0.zip build/distributions/deploy/