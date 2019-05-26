#!/usr/bin/env python

import json
import subprocess

with open('./terraform/terraform.tfstate') as tfstate:
  data = json.load(tfstate)

  with open('./credentials.txt', 'w') as credfile:
    credfile.write("Bob's Access Key:         " + data['modules'][0]['resources']['aws_iam_access_key.bob_key']['primary']['id'] + "\n")
    credfile.write("Bob's Secret Key:         " + data['modules'][0]['resources']['aws_iam_access_key.bob_key']['primary']['attributes']['secret'] + "\n" )
    credfile.write("Joe's Access Key:         " + data['modules'][0]['resources']['aws_iam_access_key.joe_key']['primary']['id'] + "\n")
    credfile.write("Joe's Secret Key:         " + data['modules'][0]['resources']['aws_iam_access_key.joe_key']['primary']['attributes']['secret'] + "\n" )

