# sms-reports

## TODOS
- Add terraform code to this project for linode
- Add YNAB report for deltas on transactions
- Add ETrade report for estimated dividend yearly income
- Consider E-mail reports with some python charts and graphs
- Consider repo rename from sms-reports to reports

## INFRA
## Add Terraform Command here
- ```cd terraform```
- ```terraform init```
- ```terraform plan -var-file="secret.tfvars"```
- ```terraform apply -var-file="secret.tfvars"```

## Software Installs & Code Deploys
## ansible-playbook -u root -i "<IP_ADDR>," ansible/playbook.yml