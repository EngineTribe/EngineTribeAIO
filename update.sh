#!/usr/bin/env bash

for module in "enginetribe" "enginebot_discord"; do
  pushd ${module}
  git pull
  popd
done