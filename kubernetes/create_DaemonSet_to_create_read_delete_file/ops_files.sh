# This script 
# creates 100, 4k files using dd, sleep 10s
# read all the files, sleep 10s
# delete all the files, sleep 10s
# Continue all the steps in a while true loop

while true
do

    echo "ITERATION: $iteration"
    while [ $timer -gt 0 ]
    do
         sleep 1
         timer=`expr $timer - 1`
    done

    # Create 100 files of size 4k inside directtor $(filedir} with ane ${filename}-no
    echo "    Creating $totalfiles in dir $filedir with file name ${filename}-no of size 4k"
    while [ $totalfiles -gt 0 ]
    do
         dd if=/dev/urandom of=${filedir}/${filename}${filecount} bs=4k count=1 2>/dev/null
         filecount=`expr $filecount + 1`
         totalfiles=`expr $totalfiles - 1`
    done
    totalfiles=$origtotalfiles
    echo "    Creating $totalfiles in dir $filedir with file name ${filename}-no of size 4k - Done"

    filecount=1
    timer=$origtimer
    while [ $timer -gt 0 ]
    do
         sleep 1
         timer=`expr $timer - 1`
    done
    # READ the created files
    echo "    Reading the created files"
    while [ $totalfiles -gt 0 ]
    do
         dd of=/dev/null if=${filedir}/${filename}${filecount} 2>/dev/null
         filecount=`expr $filecount + 1`
         totalfiles=`expr $totalfiles - 1`
    done
    echo "    Reading the created files - Done"

    totalfiles=$origtotalfiles
    filecount=1
    timer=$origtimer
    while [ $timer -gt 0 ]
    do
         sleep 1
         timer=`expr $timer - 1`
    done
    # delete file files created
    echo "    Deleting the files created"
        while [ $totalfiles -gt 0 ]
    do
         rm -f ${filedir}/${filename}${filecount}
         filecount=`expr $filecount + 1`
         totalfiles=`expr $totalfiles - 1`
    done
    echo "    Deleting the files created - Done"

    timer=$origtimer
    filecount=1
    totalfiles=$origtotalfiles
    iteration=`expr $iteration + 1`

done
