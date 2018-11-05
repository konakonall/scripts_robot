from git import Repo, RemoteProgress
from urlparse import urlparse
import os

repos = [
    'https://github.com/tencentyun/qcloud-sdk-android.git',
    'https://github.com/tencentyun/qcloud-sdk-ios.git',
    'https://github.com/tencentyun/cos-php-sdk-v5.git',
    'https://github.com/tencentyun/cos-python-sdk-v5.git',
    'https://github.com/tencentyun/cos-js-sdk-v5.git',
    'https://github.com/tencentyun/cos-nodejs-sdk-v5.git',
    'https://github.com/tencentyun/cos-java-sdk-v5.git',
    'https://github.com/tencentyun/cos-cpp-sdk-v5.git',
    'https://github.com/tencentyun/cos-c-sdk-v5.git'
]


def sync_all_repos():
    location = os.getcwd()
    for repo in repos:
        url = urlparse(repo)
        repo_name = url.path.replace('/tencentyun/', '').replace('.git', '')
        path = os.path.join(location, repo_name)
        if not os.path.exists(path):
            os.mkdir(path)
            Repo.clone_from(repo, path, progress=Progress())
        else:
            my_local_repo = Repo(path)
            my_local_repo.remote().pull()

        print 'pull done : ' + repo

class Progress(RemoteProgress):
    def line_dropped(self, line):
        print line
    def update(self, *args):
        print self._cur_line

if __name__ == '__main__':
    sync_all_repos()