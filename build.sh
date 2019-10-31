PROJECT=$1

cd $PROJECT
sh build.sh
unzip build/distributions/$PROJECT-1.0.zip -d build/distributions/deploy/
cp *.pl build/distributions/deploy/$PROJECT-1.0/bin/
rm build/distributions/$PROJECT-1.0.zip