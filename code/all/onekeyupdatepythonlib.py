import pip
from pip._internal.utils.misc import get_installed_distributions
from subprocess import call
call('python -m pip install -U pip')
for dist in get_installed_distributions():
	call("pip install --upgrade -i https://pypi.douban.com/simple "+dist.project_name,shell=True)
