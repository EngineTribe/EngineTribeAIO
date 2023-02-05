#!/usr/bin/env bash

git submodule update --init
python3 -m venv venv
source venv/bin/activate
for module in "enginetribe" "enginebot_discord"; do
  pushd ${module}
  git pull
  pip3 install -r requirements.txt
  popd
done