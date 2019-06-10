#!/bin/bash
#
# NOTE: This script should be executed INSIDE of the container

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

source ${dir_bin}/lbd/lambda-env.sh

print_colored_line $color_cyan "[DOING] list all lambda functions in this project:"
list_functions
