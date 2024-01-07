import subprocess
import os

def get_image_id(image_name):
    image_id = subprocess.run(['docker', 'images', image_name, '-q'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

    return image_id

def build_and_run_api(api_folder, port_inside, port_outside):
    os.chdir(api_folder)
    

    subprocess.run(['docker', 'build', '-t', f'{api_folder.lower()}-api', '.'])

    subprocess.run(['docker', 'stop', f'{api_folder.lower()}-container'])
    subprocess.run(['docker', 'rm', f'{api_folder.lower()}-container'])
    subprocess.run(['docker', 'run', '-d', '-p', f'{port_outside}:{port_inside}', '--name', f'{api_folder.lower()}-container', f'{api_folder.lower()}-api'])
        

    os.chdir('..')

if __name__ == "__main__":
    api_folders = [('MM-BD-API', 5002, 5002), ('NIST-tests-api', 5001, 5001), ('WELL_API', 5003, 5003), ('XoshiroAPI', 80, 5004)]

    for api_folder in api_folders:
        build_and_run_api(api_folder[0], api_folder[1])