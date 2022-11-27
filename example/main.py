import basic_path as bp
import utils

# Initialisation State
bp.init_from_poetry_toml("pyproject.toml")

# Get variables
print(f"User home -> {bp.user_home()}")
print(f"App home -> {bp.app_home()}")
print(f"Temp folder -> {bp.create_tmp_folder()}")

# Reuse from other file
utils.print_app_dir()
