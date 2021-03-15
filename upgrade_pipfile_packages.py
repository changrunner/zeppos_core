from subprocess import Popen, PIPE


def run_command(command_list):
    print(f"run_command: {command_list}")
    p = Popen(command_list, stdout=PIPE)
    out, err = p.communicate()
    print(f"run_command out: {out}")
    print(f"run_command err: {err}")
    return out.decode("utf-8").split('\r\n')


def get_dict_of_packages():
    print("get_dict_of_packages")
    # package_list = run_command("pipenv run pip list --outdated --extra-index-url=https://test.pypi.org/simple".split(" "))
    package_list = ['Package            Version Latest Type', '------------------ ------- ------ -----', 'idna               2.10    3.1    wheel', 'importlib-metadata 3.7.0   3.7.2  wheel', 'keyring            22.3.0  23.0.0 wheel', 'Pygments           2.8.0   2.8.1  wheel', 'setuptools         52.0.0  54.1.1 wheel', 'tqdm               4.58.0  4.59.0 wheel', 'zeppos-logging     1.0.15  1.0.16 wheel', '\x1b[0m']
    package_dict = {}
    for package in [p for p in package_list if 'zeppos' in p.strip()]:
        package_items = [p for p in package.split(' ') if len(p.strip()) > 0]
        package_dict[package_items[0]] = {"current_version": package_items[1], "available_version": package_items[2]}

    return package_dict


def get_out_of_date_packages_dict(package_dict):
    print("get_out_of_date_packages_dict")
    outdated_packages_dict = {}
    for k, v in package_dict.items():
        if v["current_version"] != v["available_version"]:
            outdated_packages_dict[k] = v
            print(f'Outdate: {k} - Current [{v["current_version"]}]: New [{v["available_version"]}]')
    return outdated_packages_dict


def do_we_have_outdated_packages(outdated_packages):
    return len(outdated_packages) > 0


def update_pipfile(outdated_packages):
    print("update_pipfile")
    with open("Pipfile", "r") as f:
        lines = f.readlines()

    with open("Pipfile", "w") as f:
        for line in lines:
            for k, v in outdated_packages.items():
                if line.startswith(k):

                    available_version = v["available_version"]
                    line = f'{k} = ">={available_version}"\n'
                    print(f"Set new version for [{k}]")
            f.write(line)


def upgrade_pipenv():
    print("upgrade_pipenv")
    run_command("pipenv --rm".split(" "))
    run_command("pipenv install".split(" "))
    run_command("pipenv install --dev".split(" "))

def commit_changes_to_git():
    print("commit_changes_to_git")
    run_command("git add --all".split(" "))
    run_command(["git", "commit", "-m 'update library'"])
    run_command("git push".split(" "))


def upgrade_packages():
    print("upgrade_packages")
    outdated_packages_dict = get_out_of_date_packages_dict(
        get_dict_of_packages()
    )
    if do_we_have_outdated_packages(outdated_packages_dict):
        print(f"We have [{len(outdated_packages_dict)}] outdated packages.")
        print("Let's Upgrade!")
        update_pipfile(outdated_packages_dict)
        # upgrade_pipenv()
        commit_changes_to_git()


        # pipenv run python deploy.py
        # git add --all
        # git commit -m "version 1.0.9"
        # git push
    else:
        print("Nothing to upgrade")


def main():
    print("main")
    upgrade_packages()
    print("Done!")
    # packages_dict = create_packages_dict(get_packages_from_pipfile())
    # get_latest_package_versions(packages_dict)


if __name__ == '__main__':
    main()
