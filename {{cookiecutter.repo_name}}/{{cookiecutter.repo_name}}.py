import fire

def {{cookiecutter.repo_name}}(foo: bool = False):
    if foo:
        return "foo"
    return "bar"

# main method for homebrew entrypoint
def main():
    fire.Fire({{cookiecutter.repo_name}})

if __name__ == "__main__":
    main()
    