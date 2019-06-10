#!/bin/bash
# deploy the lambda in circle ci

dir_here="$( cd "$(dirname "$0")" ; pwd -P )"
dir_bin="$(dirname "${dir_here}")"
dir_project_root=$(dirname "${dir_bin}")

cd ${dir_project_root}

# copy specified config-<stage>.json file to ${dir_project_root}/config.json
config_json_file_relpath=$1

specified_config_json_file="${dir_project_root}/${config_json_file_relpath}"
config_json_file="${dir_project_root}/config.json"
cp ${specified_config_json_file} ${config_json_file}

source ${dir_bin}/lbd/lambda-env.sh

# generate ${dir_project_root}/config-final.json based on ${dir_project_root}/config.json
python_create_final_config_script="${dir_project_root}/skymap_mpl/devops/create_final_config.py"
${bin_python} ${python_create_final_config_script}

if [ $? -ne 0 ]
then
  exit $?
fi

# update vars from config-final.json
python_get_python_config_value_script="${dir_project_root}/skymap_mpl/devops/get_final_config_value.py"

s3_bucket_lambda_deploy="$(${bin_python} ${python_get_python_config_value_script} "DEPLOYMENT_S3_BUCKET_NAME")"
aws_region="$(${bin_python} ${python_get_python_config_value_script} "AWS_REGION")"

if [ -n "$CIRCLECI" ]; then # if in CircleCI
    aws_profile_for_lambda="default"
    sls deploy --aws-profile $aws_profile_for_lambda
    aws configure set aws_access_key_id "${AWS_ACCESS_KEY_ID}"
    aws configure set aws_secret_access_key "${AWS_SECRET_ACCESS_KEY}"
    aws configure set default.region "${aws_region}"
    aws configure set default.output json
    sls deploy --aws-profile "default"
else # if in local dev, use pyenv
    aws_profile_for_lambda="$(${bin_python} ${python_get_python_config_value_script} "AWS_PROFILE")"
    sls deploy --aws-profile $aws_profile_for_lambda
fi

bash ./bin/lbd/apply-vpc-sg-layer.sh
