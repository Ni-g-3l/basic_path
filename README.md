# Basic Path

<p align="center">
 <img src="icon.png" height="">
</p>

<center>

[![GitHub license](https://img.shields.io/github/license/Ni-g-3l/basic_path.svg)](https://github.com/Ni-g-3l/basic_path/blob/main/LICENSE)

</center>

This lib provide a convenient way to access basic paths of the system and the application.

## Basic uses 

### Get basic paths

```python
import basic_path

basic_path.init_from_poetry_toml('pyproject.toml')

print(f"User home : {basic_path.user_home()}")
>> /home/nig3l

print(f"App home : {basic_path.app_home()}")
>> /home/nig3l/.basic_path
```

### Register app's paths

```python
from pathlib import *
import basic_path

basic_path.init_from_poetry_toml('pyproject.toml')

log_folder_key = "LOG_FOLDER"
basic_path.register_path(log_folder_key, Path.home() / '.log')

print(f"Log folder : {basic_path.resolve_path(log_folder_key)}")
>> /home/nig3l/.log
```

### Get tmp folder
```python
import basic_path

print(f"Tmp folder : {basic_path.create_tmp_folder()}")
>> /tmp/c6ab7dff-7f88-4874-91d7-f6e5f8f30661
```



## 🐛 Issues / Bugs / FAQs / Feature Requests

If you encounter any issues or have any ideas, please file them in our [Issue Tracker](https://github.com/Ni-g-3l/basic_path/issues).

## ✋ Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING) for details on our code of conduct, and the process for submitting pull requests to us.

## 🔢 Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Ni-g-3l/basic_path/tags).

## 🤹 Authors / Contributers / Attributions

* **Nig3l** - *Main Developer* - [Github](https://github.com/Ni-g-3l/)

See also the list of [contributors](https://github.com/Ni-g-3l/basic_path/contributors) who participated in this project.

## 📃 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

Individiual licensing arrangements can be made if this is an issue for your project - Contact Me at [LinkedIn](https://www.linkedin.com/in/maxime-cots) to discuss.

## 👏 Acknowledgments

* **File Icon** - *Created by justicon* - [Flaticon](https://www.flaticon.com/free-icons/file)
* **Billie Thompson** - *README & Contribution Templates* - [PurpleBooth](https://github.com/PurpleBooth)
