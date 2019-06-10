#!/bin/bash
# -*- coding: utf-8 -*-
#
# Build lambda deployment package in container locally

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] apply VPC Security Group and Layer to functions ..."

cd ${dir_project_root}
the_python_script="${dir_project_root}/manual_scripts/apply_vpc_sg_and_layer.py"
$bin_python ${the_python_script}
