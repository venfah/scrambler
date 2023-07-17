#!/bin/bash

ss=${1:-anthos-2}
SSH='ssh -l root'

#Setup IPs: 10.9.72.47 10.9.72.48 10.9.72.49 10.9.72.50 10.9.72.51
declare -a hosts=("hypervvm-72-47" "hypervvm-72-48" "hypervvm-72-49" "hypervvm-72-50" "hypervvm-72-51")
hostcount=${#hosts[@]}; i=0

tmux source-file ~/.tmux.conf
tmux has-session -t $ss >/dev/null 2>&1
[[ $? == 0 ]] && { echo "Session already exist....quitting" ; exit ; } 


echo "Configure Window-1"
tmux new-session -n baselinux -s $ss -d
tmux split-window -t "$ss:1"
tmux select-layout -t "$ss:1" "even-horizontal"

echo "Configure Window-2"
tmux new-window -t "$ss:2" -n setup-home -c ~
tmux split-window -t "$ss:2"
tmux split-window -t "$ss:2"
tmux split-window -t "$ss:2"
tmux split-window -t "$ss:2"
tmux select-layout -t "$ss:2" "even-vertical"
while [ $i -lt $hostcount ];
do
    tmux send-keys -t "$ss:2" -t ${i} "${SSH} ${hosts[$i]}" C-m
    let i++
done
i=0
echo "Configure Window-3"
tmux new-window -t "$ss:3" -n csi-nodlogin-status -c ~
tmux split-window -t "$ss:3"
tmux split-window -t "$ss:3"
tmux split-window -t "$ss:3"
tmux split-window -t "$ss:3"
tmux select-layout -t "$ss:3" "even-horizontal"
while [ $i -lt $hostcount ];
do
    tmux send-keys -t "$ss:3" -t ${i} "${SSH} ${hosts[$i]}" C-m
    let i++
done
i=0
echo "Configure Window-4"
tmux new-window -t "$ss:4" -n iomgr-status -c ~
tmux split-window -t "$ss:4"
tmux split-window -t "$ss:4"
tmux split-window -t "$ss:4"
tmux split-window -t "$ss:4"
tmux select-layout -t "$ss:4" "even-horizontal"
while [ $i -lt $hostcount ];
do
    tmux send-keys -t "$ss:4" -t ${i} "${SSH} ${hosts[$i]}" C-m
    let i++
done
i=0

echo "Configure Window-5"
tmux new-window -t "$ss:5" -n SERVER-INTERFACE -c ~
tmux split-window -t "$ss:5"
tmux split-window -t "$ss:5"
tmux split-window -t "$ss:5"
tmux split-window -t "$ss:5"
tmux select-layout -t "$ss:5" "even-horizontal"
while [ $i -lt $hostcount ];
do
    tmux send-keys -t "$ss:5" -t ${i} "${SSH} ${hosts[$i]}" C-m
    let i++
done
i=0

echo "Configure Window-6"
tmux new-window -t "$ss:6" -n run-the-mill -c ~
tmux split-window -t "$ss:6"
tmux select-layout -t "$ss:6" "even-vertical"

sleep 2;
# Set the default Window to First Window
tmux select-window -t $ss:2

# Login to all the sessions 
tmux set-window -t "$ss:2" synchronize-panes on
tmux send-keys -t "$ss:2" "robin123" C-m
tmux set-window -t "$ss:3" synchronize-panes on
tmux send-keys -t "$ss:3" "robin123" C-m
tmux set-window -t "$ss:4" synchronize-panes on
tmux send-keys -t "$ss:4" "robin123" C-m
tmux set-window -t "$ss:5" synchronize-panes on
tmux send-keys -t "$ss:5" "robin123" C-m
