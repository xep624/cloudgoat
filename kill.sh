#!/bin/bash

cd terraform && terraform destroy -auto-approve
rm ../tmp/allow_cidr.txt
rm ../credentials.txt
rm ./terraform.tfstate*
rm ./plan.tfout

