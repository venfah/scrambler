#!/usr/bin/python

import argparse
from subprocess import check_output, CalledProcessError
from re import compile, search
from time import time, mktime, strptime, ctime

parser = argparse.ArgumentParser(description='Create snapshot for a volume and delete snapshots older than 7 days')
parser.add_argument('--volume', type=str, help='Volume to use')
args = parser.parse_args()

def run(cmd):
    print("{}: {}".format(ctime(), cmd))
    try:
        out = check_output(cmd, shell=True)
    except CalledProcessError as e:
        out = ""
    return out

def check_master():
    vxmemout = run("vxmeminfo --role")
    comp = compile('^\s*role\s*:\s*(master|owner)')
    for line in vxmemout.splitlines():
        m = comp.search(line)
        if (m):
            print("{}: Running on {}".format(ctime(), m.groups()[0]))
            return True
    return False 
        
def snap_create(volname):
    err_str = ''
    vol_found = False
    sc_status = False
    snapname = "{}_snap_{}".format(volname, int(time()))

    print ("\n{}: Creating snapshot...".format(ctime()))
    vsout = run("vxcli volume show {}".format(args.volume))

    comp = compile("^\s*UUID:.*")
    for line in vsout.splitlines():
        s = comp.search(line)
        if (s):
             vol_found = True
             break 
    if (vol_found == False):
        err_str = 'Volume not found'
        return err_str

    scout = run("vxcli volume snapcreate {} {}".format(args.volume, snapname))

    for line in scout.splitlines():
        s = search(r"\s*Snap create successful.*", line)
        if (s):
            sc_status = True
            break
    if (sc_status == False):
        err_str = "Snapshot {} creation failed for the volume {}".format(snapname, volname)
        return err_str
    else:
        print("{}: Snapshot {} created for the volume {}".format(ctime(), snapname, volname))
        return "SUCCESS\n"

def snap_delete(volname, days_older=7):
    err_str = ''
    vol_found = False
    sc_status = False
    snap_start = False
    vol_snaps = []
    vol_snap_dict = dict()
    current_time = int(time())
    days_in_seconds = days_older*24*60*60

    print ("{}: Delete snapshots older than {} days".format(ctime(), days_older))
    vsout = run("vxcli volume show {}".format(args.volume))

    comp = compile("^\s*UUID:.*")
    for line in vsout.splitlines():
        s = comp.search(line)
        if (s):
             vol_found = True
             break 
    if (vol_found == False):
        err_str = 'Volume not found'
        return err_str

    scout = run("vxcli volume snaplist {}".format(args.volume))
    for line in scout.splitlines():
        if (line.startswith("ID")):
             snap_start = True
        if (snap_start == True):
             m = search(r"^\s*(\d+)\s+(\S+)\s+", line)
             if (m):
                 vol_snaps.append(m.groups()[1])

    for snap in vol_snaps:
        vsout = run("vxcli volume snapshow {}".format(snap))
        comp = compile(r'^\s*Creation Time:\s+(.*)$')
        for line in vsout.splitlines():
           m = comp.search(line)
           if m:
               vol_snap_dict[snap] = [m.groups()[0], int(mktime(strptime(m.groups()[0], '%Y-%m-%d %H:%M:%S')))]

    no_of_snaps_deleted = 0
    for snap, epoch in vol_snap_dict.items():
        if epoch[1] + days_in_seconds <= current_time:
            no_of_snaps_deleted += 1
            print ("{}: snap {} its creation time is {} was created more than {} days back. So deleting it.".format(ctime(), snap, epoch[0], days_older))
            sdout = run("vxcli volume snapdelete {}".format(snap))
            for line in sdout.splitlines():
                print("---> {}".format(line))
    
    if (no_of_snaps_deleted == 0):
        print ("{}: No snaps are older than {} days. None deleted".format(ctime(), days_older))
    else:
        print ("{}: {} snapshots older than {} days. All deleted".format(ctime(), no_of_snaps_deleted, days_older))

    return "SUCCESS\n"

if check_master():

    # Create periodic snaps on the volume args.volume
    print(snap_create(args.volume))

    # Delete snapshots periodically on the volume which are older than given days input
    print(snap_delete(args.volume, 7))

else:
    # IOC is standby or un-init anything other than master|owner 
    print("{}: Wait for the IOC to become master or owner and re-run this script for snapshot scheduling".format(ctime()))
