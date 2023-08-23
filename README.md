# multi-tenancy-kubernetes

## Para criar o cluster virtual

```
vcluster create teste-carga --distro k3s
```

## Recursos/Ferramentas necessárias

### K3S

``` cmd
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644
```

### HELM

```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null

sudo apt-get install apt-transport-https --yes

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list

sudo apt-get update

sudo apt-get install helm
```

### RABBITMQ

#### cria o gerenciador

kubectl apply -f rabbitmq-cluster-deployment.yaml -n vcluster-teste-carga
#### Para descobrir o usuário e senha
```
echo "$(tput setaf 2)Usuario:$(tput sgr0) $(kubectl get -n vcluster-teste-carga secret rabbitmq-default-user  -o jsonpath="{.data.username}" | base64 -d)" && \
echo "$(tput setaf 2)Senha:$(tput sgr0) $(  kubectl get -n vcluster-teste-carga secret rabbitmq-default-user  -o jsonpath="{.data.password}" | base64 -d)"
```

#### Exponhe a porta do serviço

```
kubectl port-forward \
rabbitmq-server-0 15672:15672 \
-n vcluster-teste-carga
```
#### Acessa o cluster

http://localhost:15672