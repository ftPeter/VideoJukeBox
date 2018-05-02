#!/bin/sh
#
# status-update.sh
# update the robot status csv and push it to git hub for web serving
#
# for automatic updating every five minutes,
# add this file to the crontab as shown
# crontab -e
# */5 * * * * /home/mhc/multi-robotics/robots/Romi-All/status-update/send_ip_to_github.sh
#
# Peter F. Klemperer
# April 29, 2018

ROBOT_NAME="videojukebox"
ROBOT_IP=`ip route get 1 | awk '{print $NF;exit}'`
ROBOT_TIMESTAMP=`date +%Y-%m-%d_%H-%M-%S`

echo "$ROBOT_TIMESTAMP sending robot NAME $ROBOT_NAME with IP $ROBOT_IP"
echo "FILE $UPDATE_FILENAME"

echo "robot: $ROBOT_NAME\ntime: $ROBOT_TIMESTAMP\nip: $ROBOT_IP" | ssh multirobotics@multirobotics.peterklemperer.com "cat > ~/multirobotics.peterklemperer.com/multi-robotics-status/_data/$ROBOT_NAME.yml"
ssh multirobotics@multirobotics.peterklemperer.com "cd ~/multirobotics.peterklemperer.com/multi-robotics-status ; jekyll build -d ../public"

