import subprocess
import sys

def run_command(command):
    try:
        # Run the command and capture its output and error
        result = subprocess.run(
            command,
            shell=True,
            check=True,  # Raises an exception if the command fails
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

def main():
    print("--- Running WordPress Core Installation Check ---")
    
    # Check if WordPress is already installed gracefully
    run_command("wp core install --url=http://localhost:8000 --title='My WordPress Site' --admin_user=admin --admin_password=password --admin_email=admin@example.com --skip-email || true")

    print("WordPress core is installed and configured.")

    print("\n--- Testing Custom Plugin Functionality ---")

    # Activate the custom plugin
    run_command("wp plugin activate custom-plugin")

    # Test the shortcode
    shortcode_output = run_command("wp eval 'echo do_shortcode(\"[my_greeting]\");'")
    expected_output = "Hello from My Custom Plugin!"

    if shortcode_output == expected_output:
        print("✔ Success: Shortcode output is correct.")
    else:
        print("✖ Error: Shortcode test failed.")
        print(f"Expected: '{expected_output}'")
        print(f"Got: '{shortcode_output}'")
        sys.exit(1)

    print("\nAll tests passed successfully!")
    sys.exit(0)

if __name__ == "__main__":
    main()
