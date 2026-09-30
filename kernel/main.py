import tomllib
from pathlib import Path

curr_file_path = Path(__file__).resolve()
pyproject_file_path = (curr_file_path.parent / "pyproject.toml").resolve()

# read dependencies
def get_dependencies():
    if not pyproject_file_path.exists():
        raise FileNotFoundError("Unable to find pyproject.toml file")

    # read file
    with open(pyproject_file_path, "rb") as file:
        config = tomllib.load(file)

    project_table = config.get("project", {})
    deps = project_table.get("dependencies", [])
    dep_groups = config.get("dependency-groups", {})

    return {
        "dependencies": deps,
        "dependency-groups": dep_groups
    }

def main():
    try:
        print("--- kernel ---")
        print("A centralized directory to manage dependencies for everyday workflow.")

        # current dependencies
        all_deps = get_dependencies()

        # core dependencies
        print("--- Core Dependencies ---")
        for dep in all_deps["dependencies"]:
            print(f"- {dep}")

        # dev dependencies
        print("--- Dev Dependencies ---")
        for group_name, group_deps in all_deps["dependency-groups"].items():
            print(f"[{group_name}]")
            for dep in group_deps:
                print(f"   - {dep}")

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()