## Set-up dev env

### Install requirements
```bash
pip install -r requirements.dev.txt
```

### Code formatting
We use [black](https://black.readthedocs.io/en/stable/) for formatting.
There is a CI that will automatically format your code to black but if you would like to do it, you can use one of the following methods:

#### Command-line
```bash
python -m black .
```

#### Pycharm

If you have the professional version you can configure black with the file watcher.

![image](./images/black_config.png)

You can import these settings using [this XML file](./how_to/watchers.xml)
