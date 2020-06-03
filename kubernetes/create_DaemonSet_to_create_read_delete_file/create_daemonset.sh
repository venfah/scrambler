kubectl create configmap obfsim --from-file=ops_files.sh
sleep 10s
kubectl create -f test1.yaml

# How to check
kubectl get pods -n default -o wide


# below is the watch output when we run 3 daemonset test1.yaml test2.yaml and test3.yaml with name centos1, centos2 and centos3
#Every 2.0s: kubectl get pods -n default -o wide                                                                                                                               Wed Jun  3 08:13:36 2020

#NAME            READY   STATUS    RESTARTS   AGE   IP              NODE                      NOMINATED NODE   READINESS GATES
#centos1-2r8sv   1/1     Running   5          31h   172.21.4.183    qct-17.robinsystems.com   <none>           <none>
#centos1-mcb7c   1/1     Running   1          31h   172.21.14.195   qct-19.robinsystems.com   <none>           <none>
#centos1-mrjf9   1/1     Running   2          31h   172.21.5.232    qct-18.robinsystems.com   <none>           <none>
#centos2-98dft   1/1     Running   5          31h   172.21.0.64     qct-17.robinsystems.com   <none>           <none>
#centos2-mlc4x   1/1     Running   2          31h   172.21.12.137   qct-18.robinsystems.com   <none>           <none>
#centos2-n7wj7   1/1     Running   1          31h   172.21.4.159    qct-19.robinsystems.com   <none>           <none>
#centos3-9cns9   1/1     Running   2          31h   172.21.7.60     qct-18.robinsystems.com   <none>           <none>
#centos3-9x7s2   1/1     Running   5          31h   172.21.9.89     qct-17.robinsystems.com   <none>           <none>
#centos3-qghlx   1/1     Running   1          31h   172.21.0.138    qct-19.robinsystems.com   <none>           <none>
