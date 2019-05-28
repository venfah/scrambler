#5/12/2016: Kevin  
#This will send IPMI Off to the Bolt on each IOC
#Example colovore's power off/on of ports
echo "R3 and newer IOCs"

#***update this***
bolt=bolt36
echo "Powering Off $bolt"
read -p "press any key to power off"
for ioc in 0 1;
do
    ipmitool -H ipmi-${bolt}-ioc${ioc} power status -U ADMIN -P ADMIN
done

for ioc in 0 1;
do
    ipmitool -H ipmi-${bolt}-ioc${ioc} power off -U ADMIN -P ADMIN
done
