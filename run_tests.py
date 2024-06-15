import os
import subprocess
aa
def run_tests():
    test_dir = 'tests'
    report_dir = 'reports'

    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Iterate over each test file in the tests directory
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                test_file = os.path.join(root, file)
                report_file = os.path.join(report_dir, f"report_{file.replace('.py', '')}.html")
                print(f"Running {test_file}...")

                result = subprocess.run(
                    ["pytest", test_file, f"--html={report_file}", "--self-contained-html"],
                    capture_output=True, text=True
                )

                if result.returncode != 0:
                    print(f"Tests failed for {test_file}")
                    print(result.stdout)
                    print(result.stderr)
                else:
                    print(f"Report generated: {report_file}")


if __name__ == "__main__":
    run_tests()
