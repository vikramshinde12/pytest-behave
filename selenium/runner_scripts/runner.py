import argparse
import subprocess
import pdb
import os
import pathlib
import platform

from datetime import datetime

def printing():
    print(f'current platform : {platform.system()}')
    print(f'current path {pathlib.Path(__file__).parent.absolute()}')

def get_unique_run_id():
    printing()

    if os.environ.get("BUILD_NUMBER"):
        unique_run_id = os.environ.get("BUILD_NUMBER")
    elif os.environ.get("CUSTOM_BUILD_NUMBER"):
        unique_run_id = os.environ.get("CUSTOM_BUILD_NUMBER")
    else:
        unique_run_id = datetime.now().strftime('%Y%m%d%H%M%s')

    os.environ['UNIQUE_RUN_ID'] = unique_run_id
    return unique_run_id


def create_output_directory(prefix='result_'):
    global run_id
    if not run_id:
        raise Exception("variable run_id  is not set")

    curr_file_path = pathlib.Path(__file__).parent.absolute()
    dir_to_create = os.path.join(curr_file_path, prefix + str(run_id))
    os.mkdir(dir_to_create)
    print(f'created output directory {dir_to_create}')

    return dir_to_create


if __name__ == '__main__':

    run_id = get_unique_run_id()
    # pdb.set_trace()

    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', required=False, help="Location of test file")
    parser.add_argument('--behave_options', required=False, help="-t <tags>")

    args = parser.parse_args()
    test_dir = args.test_dir or ''
    behave_options = args.behave_options or ''

    print(f'running with behave {behave_options}')
    # pdb.set_trace()

    output_dir = create_output_directory()
    json_output_dir = os.path.join(output_dir, 'json_report_out.json')
    junit_output_dir = os.path.join(output_dir, 'junit_report_out')

    response = subprocess.run(f'behave '
                              f' -f json.pretty'
                              f' -o {json_output_dir}'
                              f' --junit --junit-directory {junit_output_dir}'
                              f' --no-capture '
                              f'{behave_options} '
                              f'{test_dir}', shell=True)
    if response.returncode != 0:
        raise Exception("error !")
