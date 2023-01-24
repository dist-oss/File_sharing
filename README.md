# 上手指南

## 下载

```shell
git https://github.com/dist-oss/File_sharing.git
```

```
pip install flask
```

## 配置

编辑 `configure.json`:

```json
{
    "host":"127.0.0.1",
    "port":999,
    "template_folder":"static",
    "static_folder":"static",
    "error":"log/error.log"
}
```

### 运行

```shell
python app.py
```

