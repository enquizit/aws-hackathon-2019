#!/bin/bash
# -*- coding: utf-8 -*-
#
# display lambda function deployment relative path, url

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line ${color_cyan} "[DOING] print lambda relative information:"
print_colored_ref_line ${color_light_blue} "lambda build dir" $(colored_path ${path_build_lambda_dir})
print_colored_ref_line ${color_light_blue} "serverless config file" $(colored_path ${path_serverless_yml})
print_colored_ref_line ${color_light_blue} "lambda package source code" ${s3_uri_lambda_source_file}
print_colored_ref_line ${color_light_blue} "lambda package dependencies layer" ${s3_uri_lambda_source_file}
print_colored_ref_line ${color_light_blue} "lambda package deployment package" ${s3_uri_lambda_deploy_pkg_file}
print_colored_ref_line ${color_light_blue} "link, lambda deploy" ${aws_console_url_s3_lambda_deploy}

print_colored_ref_line ${color_light_blue} "lambda exec role" $(get_lambda_exec_role)
print_colored_ref_line ${color_light_blue} "latest layer arn" $(get_latest_layer_arn)
