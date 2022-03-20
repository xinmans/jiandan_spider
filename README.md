## jiandan_spider
spider which can get pics from http://jiandan.net

## Installation
# run as scripts 
1. Clone this repository:
```shell
git clone https://github.com/xinmans/jiandan_spider.git
cd jiandan_spider
```

2. install requirements

```shell
pip install -r /app/requirements.txt
mkdir -p /data
sudo chmod 777 /data
```
3.  run as python 
```
python jiandan.py
```

4. you can see the pic under /data folder

# run as docker
1. build docker image
```
sudo docker build -t jiandan_spider:v1 .
mkdir -p /data
sudo chmod 777 /data

```

2. run as docker
```
sudo docker run -d --restart=always  --name=jiandan_spider -v /data:/data jiandan_spider:v1
```

you can see the pics under /data

```
$ ls -ltr /data
total 0
drwxr-xr-x 2 root root 0 Mar 20 15:34 top_photos_unduplicate
drwxr-xr-x 2 root root 0 Mar 20 17:53 girl_photos_unduplicate
drwxr-xr-x 2 root root 0 Mar 20 17:54 ooxx_photos_unduplicate
drwxr-xr-x 2 root root 0 Mar 20 17:54 pic_photos_unduplicate
drwxr-xr-x 2 root root 0 Mar 20 18:05 pond_photos_unduplicate
```







