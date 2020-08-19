# Docker

## 容器

```sh
docker run -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -v /host/mysql/data:/var/lib/mysql -v /host/mysql/file:/var/lib/mysql-files -v /host/mysql/config:/etc/mysql -d --restart=always --name mysql mysql
```

/host/mysql/config 目录需要预先在宿主机上生成。
实例 config 目录里，确保有 my.cnf 文件。


```sh
# 这个文件如果可写太高会被忽略，所以改掉。
chmod 644 -R /etc/mysql
```


为了更稳妥，高版本的 mysql 会只加载 /etc/my.cnf 所以多个挂在的配置文件。该文件可写太高也会被忽略权限最好改成 644。

```sh
docker run -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -v /host/mysql/data:/var/lib/mysql -v /host/mysql/file:/var/lib/mysql-files -v /host/mysql/config:/etc/mysql -v /host/mysql/my.cnf:/etc/my.cnf -d --restart=always --name mysql mysql
```
