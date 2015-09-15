# restframe_learning
rest framework learning note.
It's going to be a API framework server.

doc:
http://www.django-rest-framework.org/

mysql.cnf is a file get my shared DB.


2015-09-15 11:06:31   --south--   http://www.cnblogs.com/BeginMan/archive/2013/09/16/3324774.html

    1、安装完South之后，要在django项目中使用South，先要将South作为一个App导入项目，所以设置INSTALL_APP添加south 第一次使用South。

    2、manage.py syncdb 用来创建south_migrationhistory表。

    3、manage.py convert_to_south youappname #在youappname目录下面创建migrations目录以及第一次迁移需要的0001_initial.py文件

    4、如果改变了model里的内容，./manage.py schemamigration youappname --auto #检测对models的更改

    manage.py migrate youappnam #将更改反应到数据库（如果出现表已存在的错误，后面加 --fake）

    如果第一次使用：
    1、./manage.py schemamigration youappname --initial # youappname目录下面创建一个migrations的子目录（注意！！就算有多个app，也只要initial一个就可以）
    2、./manage.py syncdb #初始化数据表等

    #以后每次对models更改后，可以运行以下两条命令同步到数据库
    3、./manage.py schemamigration youappname --auto #检测对models的更改
    4、./manage.py migrate youappnam #将更改反应到数据库（如果出现表已存在的错误，后面加 --fake）

2015-09-15 11:15:41
    router API and MIXINS api usage.