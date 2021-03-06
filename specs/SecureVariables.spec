SecureVariables
===============

Setup of contexts
* Basic Configuration - setup
* Using pipeline "edit-pipeline" - setup
* With "1" live agents - setup
* Capture go state "SecureVariables" - setup

SecureVariables
---------------

tags: secure_variables

* Add environment "uat" to any "1" Idle agents - Using Agents API

* Looking at environment "uat"
* Open Environment edit page for environment "uat"
* Edit environment variables
* For variable at row "1" set name "env_level_variable_made_secure_at_pipeline_level" value "env_insecure_key_value"
* Add new variable
* On Job settings page of pipeline "edit-pipeline" stage "defaultStage" job "defaultJob"
* Open "Environment Variables" tab - On Job settings page
* Add environment variable "secure_variable_made_insecure_by_job" with value "secure_variable_made_insecure_by_job"
* Save Changes
* On Stage settings page of pipeline "edit-pipeline" stage "defaultStage"
* Open "Environment Variables" tab - On Stage settings page
* Add environment variable "secure_variable_made_insecure_by_stage" with value "secure_variable_made_insecure_by_stage"
* Save Changes
* Open Environment edit page for environment "uat"
* Edit pipelines
* Add pipeline "edit-pipeline" and save environment

* On Pipeline settings page of pipeline "edit-pipeline"
* Open "Environment Variables" tab - On Pipeline settings page

* Add environment variable "plain_key" with value "plain_value"
* Add secure environment variable "secure_key" with value "secure_value"
* Add secure environment variable "secure_key_overridden_by_trigger" with value "secure_value_2"
* Add secure environment variable "env_level_variable_made_secure_at_pipeline_level" with value "secure_value_3"
* Add secure environment variable "secure_variable_made_insecure_by_stage" with value "secure_value_4"
* Add secure environment variable "secure_variable_made_insecure_by_job" with value "secure_value_5"
* Save Changes
* Verify the message "Saved successfully." is present

* Verify environment variable with name "plain_key" and value "plain_value1" is present
* Verify secure environment variable with name "secure_key" is present
* Verify secure environment variable with name "secure_key_overridden_by_trigger" is present
* Verify secure environment variable with name "env_level_variable_made_secure_at_pipeline_level" is present
* Verify secure environment variable with name "secure_variable_made_insecure_by_stage" is present
* Verify secure environment variable with name "secure_variable_made_insecure_by_job" is present

* On Job settings page of pipeline "edit-pipeline" stage "defaultStage" job "defaultJob"
* Add task "Rake"
* Set target to "\"string_reverse[secure_key secure_key_overridden_by_trigger env_level_variable_made_secure_at_pipeline_level secure_variable_made_insecure_by_stage secure_variable_made_insecure_by_job]\"" with working directory "git"
* Save Changes

* On Swift Dashboard Page
* Looking at pipeline "edit-pipeline" - On Swift Dashboard page
* Trigger pipeline - On Swift Dashboard page
* Wait till pipeline completed - On Swift Dashboard page
* Verify stage "defaultStage" is "passed" on pipeline with label "1" - On Swift Dashboard page
* On Job details page of pipeline "edit-pipeline" counter "1" stage "defaultStage" counter "1" job "defaultJob"

* Verify console log contains message "setting environment variable 'plain_key' to value 'plain_value'"
* Verify console log contains message "setting environment variable 'secure_key' to value '********'"
* Verify console log contains message "setting environment variable 'secure_key_overridden_by_trigger' to value '********'"
* Verify console log contains message "setting environment variable 'env_level_variable_made_secure_at_pipeline_level' to value 'env_insecure_key_value'"
* Verify console log contains message "overriding environment variable 'env_level_variable_made_secure_at_pipeline_level' with value '********'"
* Verify console log contains message "setting environment variable 'secure_variable_made_insecure_by_stage' to value 'secure_variable_made_insecure_by_stage'"
* Verify console log contains message "setting environment variable 'secure_variable_made_insecure_by_job' to value 'secure_variable_made_insecure_by_job'"
* Verify console log does not contains message "overriding environment variable 'secure_key'"
* Verify console log does not contains message "overriding environment variable 'secure_key_overridden_by_trigger'"
* Verify console log contains message "secure_key=eulav_eruces"
* Verify console log contains message "secure_key_overridden_by_trigger=2_eulav_eruces"
* Verify console log contains message "env_level_variable_made_secure_at_pipeline_level=3_eulav_eruces"
* Verify console log contains message "secure_variable_made_insecure_by_stage=egats_yb_erucesni_edam_elbairav_eruces"
* Verify console log contains message "secure_variable_made_insecure_by_job=boj_yb_erucesni_edam_elbairav_eruces"

* On Swift Dashboard Page
* Open trigger with options - On Swift Dashboard page
* Switch to Secure Environment Variables tab - On Swift Dashboard page
* Override secure variable named "secure_key_overridden_by_trigger" with value "overridden_value_2"
* Trigger pipeline with options - On Swift Dashboard page

* On Swift Dashboard Page
* Looking at pipeline "edit-pipeline" - On Swift Dashboard page
* Wait till pipeline completed - On Swift Dashboard page
* Verify stage "defaultStage" is "passed" on pipeline with label "2" - On Swift Dashboard page
* On Job details page of pipeline "edit-pipeline" counter "2" stage "defaultStage" counter "1" job "defaultJob"

* Verify console log contains message "setting environment variable 'plain_key' to value 'plain_value'"
* Verify console log contains message "setting environment variable 'secure_key' to value '********'"
* Verify console log contains message "setting environment variable 'secure_key_overridden_by_trigger' to value '********'"
* Verify console log contains message "setting environment variable 'env_level_variable_made_secure_at_pipeline_level' to value 'env_insecure_key_value'"
* Verify console log contains message "overriding environment variable 'env_level_variable_made_secure_at_pipeline_level' with value '********'"
* Verify console log contains message "setting environment variable 'secure_variable_made_insecure_by_stage' to value 'secure_variable_made_insecure_by_stage'"
* Verify console log contains message "setting environment variable 'secure_variable_made_insecure_by_job' to value 'secure_variable_made_insecure_by_job'"
* Verify console log does not contains message "overriding environment variable 'secure_key'"
* Verify console log contains message "overriding environment variable 'secure_key_overridden_by_trigger' with value '********'"
* Verify console log contains message "secure_key=eulav_eruces"
* Verify console log contains message "secure_key_overridden_by_trigger=2_eulav_neddirrevo"
* Verify console log contains message "env_level_variable_made_secure_at_pipeline_level=3_eulav_eruces"
* Verify console log contains message "secure_variable_made_insecure_by_stage=egats_yb_erucesni_edam_elbairav_eruces"
* Verify console log contains message "secure_variable_made_insecure_by_job=boj_yb_erucesni_edam_elbairav_eruces"


Teardown of contexts
____________________
* Capture go state "SecureVariables" - teardown
* With "1" live agents - teardown
