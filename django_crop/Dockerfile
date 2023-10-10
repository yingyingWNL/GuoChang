FROM python:3.7

MAINTAINER Aaron

#设置环境变量
ENV PYTHONUNBUFFERED 1

#设置pip源为国内源
COPY pip.conf /root/.pip/pip.conf

#在容器内/var/www/html/下创建mysite1文件夹
RUN mkdir -p /var/www/html/mysite1

#设置容器内工作目录
WORKDIR /var/www/html/mysite1

#将当前目录文件加入到容器工作目录中(.表示当前宿主机目录)
ADD . /var/www/html/mysite1

#利用pip安装依赖
RUN pip install -r requirements.txt


### docker run -it -d --name mysite1 -p 8000:8000 -v /home/vscode/django_crop/:/var/www/html/mysite1 django_docker_img:v1

### 下面进行再docker中安装fastdfs
### https://blog.csdn.net/weixin_44689630/article/details/101226233
### 使用python setup.py install 后， 进行测试
# from fdfs_client.client import Fdfs_client
# client = Fdfs_client('utils/fastdfs/client.conf')
# client.list_all_groups()