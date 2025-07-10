# EKS Flask + MySQL Demo

This repo shows how to deploy a simple Flask app with MySQL DB on AWS EKS.

## 📂 Files

- `app.py` — Flask app (Python 3.12)
- `Dockerfile` — Build image
- `k8s-all.yaml` — All K8s resources (Secret, PVC, StatefulSet, Deployment, Services)
- `eks-cluster.yaml` — EKS cluster config for eksctl

## 🚀 Steps

### 1️⃣ Create the EKS Cluster

```bash
eksctl create cluster -f eks-cluster.yaml
aws eks update-kubeconfig --region us-east-2 --name flask-mysql-demo
```

### 2️⃣ Build & Push the Image

```bash
docker build -t flask-mysql-demo .
docker tag flask-mysql-demo:latest <YOUR_ECR_URI>:latest
docker push <YOUR_ECR_URI>:latest
```

### 3️⃣ Deploy

Update `k8s-all.yaml` with your ECR image, then:

```bash
kubectl apply -f k8s-all.yaml
```

### 4️⃣ Access

Get the LoadBalancer:

```bash
kubectl get svc flask-service
```

Visit the `EXTERNAL-IP` in your browser.

## ✅ Done!
