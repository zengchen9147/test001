from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def jinja2_environment(**options):
    # 创建环境对象
    env = Environment(**options)
    # env.globals是存放默认命名空间的字典
    # update方法向字典中更新数据
    env.globals.update({
        'url': reverse,
        'static': staticfiles_storage.url,
    })
