import os
import shutil

def remove_generated_file(filepath):
    full_path = os.path.join(os.getcwd(), '{{cookiecutter.repo_name}}', filepath)
    if os.path.isfile(full_path):
        os.remove(filepath)

create_pypi_deploy_actions = '{{cookiecutter.create_pypi_deploy_github_action}}' == 'y'

if not create_pypi_deploy_actions:
    remove_generated_file(os.path.join('.github', 'workflows', 'deploy'))
