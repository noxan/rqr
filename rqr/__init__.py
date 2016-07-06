from .updater import check_file_for_updates

def main():
    check_file_for_updates('./requirements/base.txt')
