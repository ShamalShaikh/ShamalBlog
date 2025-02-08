---
title: "Production-Grade Kubernetes Deployment Patterns for AI Applications"
date: 2025-02-10 12:00:00 +/-TTTT
categories: [Tutorials, DevOps]
tags: [kubernetes, devops, deployment, cloud-native]
image:
  src: "/ShamalBlog/images/tutorials/k8s-patterns.jpg"
  alt: "Kubernetes Deployment Patterns"
---

## Advanced Kubernetes Deployment Patterns for AI Workloads

This guide covers production-tested deployment patterns for AI applications on Kubernetes, focusing on scalability and reliability.

### 1. Sidecar Pattern for Model Serving

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model-server
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: model-server
        image: model-server:latest
        resources:
          limits:
            nvidia.com/gpu: 1
      - name: model-loader
        image: model-loader:latest
        volumeMounts:
        - name: model-storage
          mountPath: /models
```

### 2. Horizontal Pod Autoscaling for ML Workloads

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: model-server-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model-server
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Pods
    pods:
      metric:
        name: inference_requests_per_second
      target:
        type: AverageValue
        averageValue: 1000
```

### 3. StatefulSet for Distributed Training

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: distributed-training
spec:
  serviceName: training-cluster
  replicas: 4
  template:
    spec:
      containers:
      - name: trainer
        image: training-job:latest
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: WORLD_SIZE
          value: "4"
```

### 4. Job Pattern for Batch Inference

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: batch-inference
spec:
  parallelism: 3
  completions: 10
  template:
    spec:
      containers:
      - name: inference
        image: batch-inference:latest
        resources:
          limits:
            nvidia.com/gpu: 1
```

### 5. Custom Resource Definitions for ML Workflows

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: mlworkflows.ai.example.com
spec:
  group: ai.example.com
  names:
    kind: MLWorkflow
    plural: mlworkflows
  scope: Namespaced
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              modelName:
                type: string
              trainingData:
                type: string
              hyperparameters:
                type: object
```

## Best Practices

### Resource Management

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: ml-quota
spec:
  hard:
    requests.nvidia.com/gpu: 8
    limits.nvidia.com/gpu: 8
    requests.memory: 64Gi
    limits.memory: 128Gi
```

### Network Policies

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: ml-network-policy
spec:
  podSelector:
    matchLabels:
      app: model-server
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: api-gateway
```

### Monitoring Setup

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: model-metrics
spec:
  selector:
    matchLabels:
      app: model-server
  endpoints:
  - port: metrics
```

## Implementation Tips

1. **GPU Resource Management**
   - Use node labels for GPU types
   - Implement GPU sharing when possible
   - Monitor GPU utilization

2. **Scaling Strategies**
   - Use KEDA for custom metrics
   - Implement graceful scaling
   - Consider cost optimization

3. **Security Considerations**
   - Implement RBAC
   - Use network policies
   - Secure sensitive data

## Testing Deployment

```bash
# Apply configurations
kubectl apply -f k8s/

# Verify deployments
kubectl get deployments,statefulsets,jobs

# Check pod status
kubectl get pods -w

# View logs
kubectl logs -l app=model-server
```

[View complete configurations on GitHub →](https://github.com/yourusername/k8s-ml-patterns) 