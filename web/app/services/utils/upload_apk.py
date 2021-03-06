from decimal import Decimal
import dropbox
import os
import re
import shutil
import sys


def get_max_version(apk, max_version):
    match = re.search(r"(\d+(\.\d)*)", apk)
    if match is not None:
        version = match.group(1)
        if Decimal(version) > Decimal(max_version):
            max_version = version
    return max_version


def upload(root_dir, ci_project_dir, oauth2_access_token):
    file = os.path.join(ci_project_dir, "sciq-apk", "app-debug.apk")
    apks_dir = os.path.join(root_dir, "sciq-apk")
    dbx = dropbox.Dropbox(oauth2_access_token=oauth2_access_token)
    max_version = "0.0"
    # Get max version from filesystem
    for apk in os.listdir(apks_dir):
        max_version = get_max_version(apk, max_version)
    # Get max version from Dropbox
    for entry in dbx.files_list_folder("").entries:
        apk = entry.name
        max_version = get_max_version(apk, max_version)
    new_file = "sciq_v." + str(Decimal(max_version) + Decimal("0.1")) + ".apk"
    new_file_full_path = os.path.join(apks_dir, new_file)
    shutil.move(file, new_file_full_path)
    dbx.files_upload(open(new_file_full_path, "rb").read(), "/" + new_file)
    download_url = dbx.sharing_create_shared_link("/" + new_file).url
    # Make url directly downlodable
    download_url = download_url[:-1] + "1"
    with open(
        os.path.join(root_dir, "web", "app", "templates", "index.html"), "r+"
    ) as f:
        index = f.read()
        index = re.sub(
            r"__DROPBOX_DOWNLOAD_URL__|https://www.dropbox.com/s/.*?\?dl=1",
            download_url,
            index,
        )
        f.seek(0)
        f.write(index)
        f.close()

    with open(
        os.path.join(root_dir, "README.md"), "r+"
    ) as f:
        readme = f.read()
        readme = re.sub(
            r"__DROPBOX_DOWNLOAD_URL__|https://www.dropbox.com/s/.*?\?dl=1",
            download_url,
            readme,
        )
        f.seek(0)
        f.write(readme)
        f.close()


if __name__ == "__main__":
    upload(sys.argv[1], sys.argv[2], sys.argv[3])
