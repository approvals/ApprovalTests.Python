## Set-up dev env

### Install requirements
```bash
pip install -r requirements.dev.txt
```

### Code formatting
To format code, run `./format_code.sh`

There is a CI that will automatically format whenever you push but if you would like to do it locally, you can use one of the following methods:

#### Command-line
```bash
./format_code.sh
```

#### Pycharm Black configuration

If you have the professional version of Pycharm you can configure black with the file watcher.

![image](./images/black_config.png)

You can import these settings using [this XML file](./how_to/watchers.xml)
