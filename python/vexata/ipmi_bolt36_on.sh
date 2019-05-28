#5/12/2016: Kevin  
#This will send IPMI On to the Bolt on each IOC
#Example colovore's power off/on of ports
echo "R3 and newer IOCs"


#***update this***
bolt=bolt36
echo "Powering On $bolt"
i=1
while [[ $i -gt 0 ]]
do

for ioc in 0 1;
do
    ipmitool -H ipmi-${bolt}-ioc${ioc} power status -U ADMIN -P ADMIN|grep "Chassis Power is off"
    ipmitool -H ipmi-${bolt}-ioc${ioc} sdr -U ADMIN -P ADMIN
done
sleep 5
echo "Waiting for Power off before powering on"
i=$?
done

for ioc in 0 1;
do
    ipmitool -H ipmi-${bolt}-ioc${ioc} power on -U ADMIN -P ADMIN
done

for ioc in 0 1;
do
    ipmitool -H ipmi-${bolt}-ioc${ioc} sdr -U ADMIN -P ADMIN
done
