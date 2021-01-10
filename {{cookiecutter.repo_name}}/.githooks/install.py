# Standard Library
import os
from glob import glob

# Third party
import fire

src_dir = os.path.dirname(os.path.realpath(__file__))


def install_hooks(force=False):
    """
    symlink every file from .githooks to .git/hooks and make them executable

    Args:
        force (bool): force the symlink to overwrite existing files in .git/hooks
    """

    dest_dir = os.path.join(src_dir, "..", ".git", "hooks")
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)  # mkdir -p

    for filepath in glob(f"{src_dir}/*"):
        if filepath.endswith("install.py"):
            continue

        filename = os.path.basename(filepath)
        new_path = os.path.join(dest_dir, filename)

        if force and os.path.exists(new_path):
            os.unlink(new_path)  # remove old git hook

        os.symlink(filepath, new_path)
        os.system(f"sudo chmod +x {new_path}")


if __name__ == "__main__":
    fire.Fire(install_hooks)
