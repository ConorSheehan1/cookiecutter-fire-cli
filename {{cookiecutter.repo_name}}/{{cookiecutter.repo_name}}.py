# Third party
import fire

__version__ = "0.1.0"


def {{cookiecutter.repo_name}}(foo: bool = False, version: bool = False) -> str:
    if version:
        return __version__
    if foo:
        return "foo"
    return "bar"


# main method for homebrew entrypoint
def main():
    fire.Fire({{cookiecutter.repo_name}})


if __name__ == "__main__":
    main()
