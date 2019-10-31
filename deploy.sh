PROJECT=$1
HOST=$2

scp -r $PROJECT/build/distributions/deploy/$PROJECT-1.0/ pi@$HOST:/home/pi/dev/opt/