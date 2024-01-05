import subprocess
import os

def build_and_run_api(api_folder, port):
    # Change directory to the API folder
    os.chdir(api_folder)

    # Build Docker image
    subprocess.run(['docker', 'build', '-t', f'{api_folder.lower()}-api', '.'])

    # Run Docker container
    subprocess.run(['docker', 'run', '-d', '-p', f'{port}:{port}', f'{api_folder.lower()}-api'])

    # Change back to the original directory
    os.chdir('..')

if __name__ == "__main__":
    # List of API folders
    api_folders = [('MM-BD-API', 5000), ('NIST-tests-api', 5001), ('WELL_API', 5003), ('XoshiroAPI', 80)]

    for api_folder in api_folders:
        build_and_run_api(api_folder[0], api_folder[1])