#!/bin/bash
# -*- coding: utf-8 -*-
#
# Build lambda deployment package in container locally

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] build everything for lambda at ${path_build_lambda_dir} in container ${docker_image_for_build} ..."
mkdir -p ${path_build_lambda_dir}
script_path=${dir_container_workspace}/bin/lbd/build-lbd-everything-in-container.sh
docker run -v ${dir_project_root}:${dir_container_workspace} --rm ${docker_image_for_build} bash ${script_path}
