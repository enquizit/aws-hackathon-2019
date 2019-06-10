#!/bin/bash
# -*- coding: utf-8 -*-
#
# Build lambda deployment package in container locally

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] remove all functions defined in serverless.yml ..."
cd ${dir_project_root}
sls remove --aws-profile $aws_profile_for_lambda
