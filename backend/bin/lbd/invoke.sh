#!/bin/bash
# -*- coding: utf-8 -*-
#
# Run lambda function in container locally with custom event data
#
# usage:
#
#   invoke "func_name" "path-to-event-json-file.json"
#
# It uses Linux pre-built dependencies at <dir_project_root>/build/lambda/site-packages
# So make sure you did "make lbd-build-deploy-pkg" first

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh
invoke_lbd $1 $2
