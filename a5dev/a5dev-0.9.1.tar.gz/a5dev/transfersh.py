
import os
import sys
import zipfile
import requests
import datetime
import wget


def get_date_in_two_weeks():
    """
    get maximum date of storage for file
    :return: date in two weeks
    """
    today = datetime.datetime.today()
    date_in_two_weeks = today + datetime.timedelta(days=14)
    return date_in_two_weeks.date()


def get_size(file):
    """
    get file size, in megabytes
    :param file:
    :return: size of file
    """
    size_in_bytes = os.path.getsize(file)
    size_in_megabytes = size_in_bytes / 1000000
    return size_in_megabytes



def check_absolute_path(path):
    """
    check if entered directory is absolute, if not, format it to absolute
    :param path: path that was entered by user
    :return: absolute path
    """
    current_dir = os.getcwd()
    if os.path.isabs(path) is False:
        if str(path).startswith("./"):
            return current_dir + path[1:]
        else:
            return current_dir + "/" + path
    else:
        return path




def create_zip(file_dir):
    """
    create zipfile from files in entered directory
    :param file_dir: absolute path to directory
    :return: absolute path to created zipfile
    """
    curr_path = os.getcwd()
    os.chdir(file_dir)
    zip_name = 'files_archive_{}.zip'.format(
        str(datetime.datetime.now())[5:16].replace(' ', "_"))
    files = os.listdir()
    print("Creating zipfile from files in...", file_dir)
    with zipfile.ZipFile(zip_name, 'w') as zip:
        for f in files:
            zip.write(f)
            print("Added file: ", f)

    zip_path = file_dir + "/" + zip_name
    os.chdir(curr_path)
    # double check if path is absolute
    if os.path.isabs(zip_path):
        return zip_path
    else:
        return os.getcwd() + "/" + zip_name


def remove_file(file):
    print("Removing file...", file)
    os.remove(file)
    print("Removed.")


def confirm_removal(confirm, filename):
    """
    function used in interactive mode, asks weather to remove file, or not
    :param confirm:
    :param filename: absolute path to file
    :return: None
    """
    if confirm == 'y' or confirm == 'yes':
        remove_file(filename)
    elif confirm == 'n' or confirm == 'no':
        print("File will stay there")
    else:
        print("Please etner a valid answer (y/n, yes/no)")
        confirm_removal()


def send_to_transfersh(file,to_clipboard=False):
    """
    send file to transfersh, retrieve download link, and copy it to clipboard
    :param file: absolute path to file
    :return: None
    """
    size_of_file = get_size(file)
    final_date = get_date_in_two_weeks()
    file_name = os.path.basename(file)

    print("\nSending file: {} (size of the file: {} MB)".format(
        file_name, size_of_file))
    url = 'https://transfer.sh/'
    file = {'{}'.format(file): open(file, 'rb')}
    response = requests.post(url, files=file)
    download_link = response.content.decode('utf-8')
    print("Link to download file(will be saved till {}):\n{}".format(
        final_date, download_link))
    if to_clipboard:
        copy_to_clipboard(download_link)
    return download_link


def download_from_transfersh(download_link, path='.'):
    """
    download file from transfersh
    :param download_link: link to uploaded file
    :param path:  directory or file path for file to be downloaded
    :return: path where the file is downloaded
    """
    return wget.download(download_link, out=path)


