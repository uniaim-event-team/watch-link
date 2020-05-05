# watch-link

watch something and report to somewhere

# License

MIT

# Example

- watch slack, copy to google chat.

# Usage (Installation)

## install python3

Install python3 for the whole instances.
note: if you use amazon linux2,

```bash
$ sudo yum install python3
```

## run or install some MySQL like database

Run or install some MySQL like database.

## install requirements

Install the requirements.

## run get_basic_token.py

Controller instance has basic authentication. You should create the token(hash) of password, and save it to app.ini.

## create app.ini file

Create app.ini file. The sample is app.ini.default.

## edit crontab

Add following line to crontab.

```
* * * * * cd /home/ec2-user/watch-link; python3 watch.py
```

## run init.py

Execute following command.

```bash
$ cd ~/watch-link
$ python3 init.py
```

## run watch-link application(for setup data)

Execute following command.

```bash
$ cd ~/watch-link
$ nohup python3 app.py &
```

## setup data

(under construction)
- watch_links
- input of watch_links
