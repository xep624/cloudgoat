#!/usr/bin/env python

import json
import subprocess

with open('./terraform/terraform.tfstate') as tfstate:
  data = json.load(tfstate)

  with open('./credentials.txt', 'w') as credfile:
    credfile.write("Bob's Access Key:         " + data['resources'][0]['instances'][0]['attributes']['id'] + "\n")
    credfile.write("Bob's Secret Key:         " + data['resources'][0]['instances'][0]['attributes']['secret'] + "\n")

