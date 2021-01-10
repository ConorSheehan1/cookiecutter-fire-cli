import os
import shutil


def remove_generated_file(filepath):
    # hooks are run from generated dir context, so will be ./example_cli
    full_path = os.path.join(os.getcwd(), '{{cookiecutter.repo_name}}', filepath)
    if os.path.isfile(full_path):
        os.remove(filepath)


create_pypi_deploy_action = '{{cookiecutter.create_pypi_deploy_github_action}}' == 'y'
create_release_action = '{{cookiecutter.create_release_github_action}}' == 'y'

if not create_pypi_deploy_action:
    remove_generated_file(os.path.join('.github', 'workflows', 'deploy.yml'))

if not create_release_action:
    remove_generated_file(os.path.join('.github', 'workflows', 'release.yml'))
