#!/usr/bin/python
import argparse
import threading
from subprocess import check_output, CalledProcessError
from re import compile, search
from time import time, mktime, strptime, ctime, sleep
from yaml import safe_load;
import os
import random
from collections import OrderedDict


'''
HOW TO RUN:
print ("python {} --helmapp app-1 --namespace default --snapcount 50".format(os.path.basename(__file__)))
'''

def run(cmd):
    print("{}: CMD exec:{}".format(ctime(), cmd))
    try:
        out = check_output(cmd, shell=True)
    except CalledProcessError as e:
        out = ""
    return out

def get_volumes_in_helmapp(appname):
    cmd_output = run("kubectl get pvc -o wide -o json")
    cmd_output_json = safe_load(cmd_output)
    volumetree = dict()
    for eachitem in cmd_output_json['items']:
       if appname == eachitem['metadata']['name']:
            volumetree[eachitem['spec']['volumeName']] = dict()
            volumetree[eachitem['spec']['volumeName']]['snapshots'] = OrderedDict()
            volumetree[eachitem['spec']['volumeName']]['volumeName'] = eachitem['spec']['volumeName']
            volumetree[eachitem['spec']['volumeName']]['storage'] = eachitem['spec']['resources']['requests']['storage']
            volumetree[eachitem['spec']['volumeName']]['volumeMode'] = eachitem['spec']['volumeMode']
            volumetree[eachitem['spec']['volumeName']]['helmappname'] = eachitem['metadata']['name']
    return (volumetree)

def snap_create_on_volume (appname=None, snapno=0, snapstring=None):
    snapfile = snapfile="/tmp/volsnap-{}-{}.yaml".format(appname, snapno)
    
    FILE = open(snapfile, "w")

    if snapstring != None:
        for eachline in snapstring.split("\n"):
            eachline = eachline.replace("name: SNAPNAME", "name: volsnap-{}-{}".format(appname, snapno))
            eachline = eachline.replace("persistentVolumeClaimName: CLAIMNAME", "persistentVolumeClaimName: {}".format(appname))
            #print("{} {}".format(snapfile, eachline))
            FILE.write("{}\n".format(eachline))
        FILE.close()
    print "Create a snapshot volsnap-{}-{} for the app {}".format(appname, snapno, appname)
    cmd_output = run("kubectl create -f {}".format(snapfile))
    cmd_output_json = safe_load(cmd_output)
    print ("Snap create output: {}".format(cmd_output_json))
    return ("volsnap-{}-{}".format(appname, snapno))

def snap_delete_of_volume (snapname=None):
    cmd_output = run("kubectl delete volumesnapshot {}".format(snapname))
    cmd_output_json = safe_load(cmd_output)
    return (snapname)
    pass

if __name__ == "__main__":
    # PARSE THE ARGS
    parser = argparse.ArgumentParser(description='run stress on Helm APP')
    parser.add_argument('--helmapp', type=str, help='Helm App name', required=True, choices=['app-1', 'app-2'])
    parser.add_argument('--namespace', type=str, help='Name space of all the pods', required=True)
    parser.add_argument('--snapcount', type=int, help='Number of snapshots', required=True, choices=range(0,60))
    args = parser.parse_args()

    volumes_in_helm = get_volumes_in_helmapp(args.helmapp)
    print("POST VOL CREATE: {}".format(volumes_in_helm))

    volsnap_string = '''
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: SNAPNAME
  labels:
    app.kubernetes.io/instance: robin
    app.kubernetes.io/managed-by: robin.io
    app.kubernetes.io/name: robin
spec:
  volumeSnapshotClassName: robin-snapshotclass
  source:
    persistentVolumeClaimName: CLAIMNAME
'''

    for snap_number in range (0, args.snapcount):
        for each_pvc in  volumes_in_helm.keys():
            if volumes_in_helm[each_pvc]['helmappname'] == args.helmapp:
                snapcreate_return = snap_create_on_volume( appname=args.helmapp, snapno=snap_number, snapstring=volsnap_string)
                print ("sleep for 30 seconds after snap create")
                sleep (30)
                if snapcreate_return not in volumes_in_helm[each_pvc]['snapshots']:
                    volumes_in_helm[each_pvc]['snapshots'][snapcreate_return] = int(time())
    print("POST SNAP CREATE: {}".format(volumes_in_helm))

    while True:
        snap_number = random.randint(0, args.snapcount)
        snapname = "volsnap-{}-{}".format( args.helmapp, snap_number)
        snapdelete_return = snap_delete_of_volume(snapname=snapname)
        for each_pvc in  volumes_in_helm.keys():
            if snapdelete_return in volumes_in_helm[each_pvc]['snapshots']:
                 print ("snapshot {} deleted from the volume {}".format(snapdelete_return, each_pvc))
                 volumes_in_helm[each_pvc]['snapshots'].pop(snapdelete_return)
        print ("sleep for 30 seconds after snap delete")
        sleep (30)
        print("POST SNAP DELETE: {}".format(volumes_in_helm))

        snapcreate_return = snap_create_on_volume( appname=args.helmapp, snapno=snap_number, snapstring=volsnap_string)
        for each_pvc in  volumes_in_helm.keys():
            if snapcreate_return not in volumes_in_helm[each_pvc]['snapshots']:
                volumes_in_helm[each_pvc]['snapshots'][snapcreate_return] = int(time())
        print ("sleep for 30 seconds after snap create")
        sleep (30)
        print("POST SNAP CREATE: {}".format(volumes_in_helm))
