#for bolt_no in 10 17 18 31 33 35 36 37 40
for ioc in 0 1
do for bolt_no in 10 17 18 31 33 35 36 37 40
#do for bolt_no in 10
do cat .ssh/id_rsa.pub | ssh root@bolt${bolt_no}-ioc${ioc} 'cat >> .ssh/authorized_keys'
done
done
