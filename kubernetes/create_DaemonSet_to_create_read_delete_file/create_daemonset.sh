kubectl create configmap obfsim --from-file=ops_files.sh
sleep 10s
kubectl create -f test1.yaml

# How to check
kubectl get pods -n default -o wide
