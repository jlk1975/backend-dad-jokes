# sms-reports

## TODOS
- Add YNAB report for deltas on transactions (start here: https://api.youneedabudget.com/#deltas)
- Add ETrade report for estimated dividend yearly income
- Consider E-mail reports with some python charts and graphs
- Consider repo rename from sms-reports to reports
- Use some variables in your ansible

## INFRA Setup
- ```cd terraform```
- ```terraform init```
- ```terraform plan -var-file="secret.tfvars"```
- ```terraform apply -var-file="secret.tfvars"```

## Software Installs & Code Deploys
- ```ansible-playbook -u root -i "root@<IP_ADDR>," ansible/playbook.yml```