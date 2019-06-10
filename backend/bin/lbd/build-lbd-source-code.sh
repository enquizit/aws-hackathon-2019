#!/bin/bash
#
# Build lambda source code only. Only needs to update source code, if using layer.

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] build lambda source code at ${path_lambda_source_file} ..."
mkdir -p ${path_build_lambda_dir}
rm_if_exists ${path_lambda_source_file}
build_lbd_source_code
