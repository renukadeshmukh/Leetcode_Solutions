apiVersion: batch/v1
kind: Job
metadata:
  name: package-cleanup-patch
spec:
  backoffLimit: 5
  template:
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: compute
                operator: In
                values:
                - allowed
              - key: appstack.maglev-system
                operator: In
                values:
                - enabled
            - matchExpressions:
              - key: compute
                operator: In
                values:
                - allowed
              - key: allAppstacks
                operator: In
                values:
                - enabled
      containers:
      - name: package-cleanup-patch
        image: maglev-registry.maglev-system.svc.cluster.local:5000/maglev-catalogm:1.4.1.32
        command: [ "/opt/maglev/bin/garbage_collect" ]
      restartPolicy: OnFailure
