Requirement:
+ Your local host: 
	- Terraform
	- Ansible


To run this Terraform please go to terraform/dev/

Run these commands:

export ANSIBLE_HOST_KEY_CHECKING=False
sudo chmod 600 ../ap_southeast_1_key_pair
terraform init
terraform plan -out terraform
terraform apply terraform

Then you access to the public ip of EC2 instance by port 80
Run this command to get the public ip: terraform show | grep public_ip | sed -n 2p | awk '{gsub("\"","");print $3}'
