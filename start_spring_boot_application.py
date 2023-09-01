import os
import subprocess

# os.environ["JAVA_HOME"] = "C:\Program Files\Java\jdk-17"
# os.environ["MAVEN_HOME"] = "C:\maven"

def load_env_variables(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            variables = line.strip().split(';')
            for variable in variables:
                key_value = variable.strip().split('=')
                if len(key_value) == 2:
                    key, value = key_value
                    os.environ[key] = value
                    print(key + '=' + value)


def compile_and_run(project_location):
    try:
        os.chdir(project_location)
        env_file_path = os.path.join(project_location, 'app_env.txt')
        load_env_variables(env_file_path)
        # subprocess.run(['mvn', 'clean', 'install'])
        subprocess.run('mvn clean install', shell=True, check=True)
        subprocess.run(['java', '-jar', 'target/app.jar'])

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    choice = input("Do you want to use the current directory as the project location? (y/n): ").strip().lower()
    if choice == 'y':
        current_directory = os.path.dirname(os.path.abspath(__file__))
        print("Using the current directory:", current_directory)
        compile_and_run(current_directory)
    else:
        project_location = input("Enter the project location: ").strip()
        compile_and_run(project_location)