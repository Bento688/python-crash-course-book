import subprocess

try:
    result = subprocess.run(["ls", "-la"], capture_output=True, text=True, check=True)

    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error: " + e.stderr)
