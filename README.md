# sms-dad-jokes

## TODO
- Remove go install from ansible, deploying a built binary so don't need to install go
- Add terraform code to this project for linode
- Setup a github action or circle ci to build and deploy the go code on commit, or maybe Travis CI

## ansible-playbook -u root -i ./inventory.yml -l gp_servers playbook.yml`

## Note, if building on Arch Linux and deploying the binary file to Debian, build like this:
```CGO_ENABLED=0 go build main.go```