#!/bin/bash

gdown https://drive.google.com/uc?id=1bByEqiC6pr2AfjmV8prp8C2XWq5z5AhK
ansible-playbook ansible/download-ds.yml --vault-password-file ./vault-pass.txt
python3  model-train.py
ansible-playbook ansible/upload-model.yml --vault-password-file ./vault-pass.txt
