import subprocess
import sys
from tests.utils import remove_if_exists

def setup_module(module):
    # Clean up generated output before running
    test_out = 'generated/TestCLISmoke'
    remove_if_exists(test_out)

def test_cli_runs_example_config():
    import pathlib
    project_root = pathlib.Path(__file__).resolve().parent.parent
    cli_path = project_root / 'cli.py'
    config_path = project_root / 'examples' / 'example_config.yaml'
    out_dir = project_root / 'generated' / 'TestCLISmoke'

    remove_if_exists(out_dir)

    result = subprocess.run([
        sys.executable, str(cli_path), str(config_path), '--output-dir', str(out_dir)
    ], capture_output=True, text=True, cwd=str(project_root))
    if result.returncode != 0:
        print('STDOUT:', result.stdout)
        print('STDERR:', result.stderr)
    assert result.returncode == 0
    # Check that main.py and database.py were generated
    app_dir = out_dir / 'MyGeneratedApp'
    assert (app_dir / 'main.py').exists(), f"main.py not found in {app_dir}"
    assert (app_dir / 'database.py').exists(), f"database.py not found in {app_dir}"

    # Clean up generated test files after test
    remove_if_exists(out_dir)
