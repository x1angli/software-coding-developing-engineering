This article is specially created, because the instruction given in https://packaging.python.org/tutorials/packaging-projects/ is not accuate.

To pack your python project into a .whl file or .tar file, and upload it onto PyPI. You should do the following steps:

1. Register accounts with PyPI, 

    1.1 Go to https://test.pypi.org/account/register/ and complete the steps on that page. 

    1.1 Register another account on https://pypi.org

    1.1 Verify your email address. Note: the websites above use separate account system.

1. create a `~/.pypirc` (\*nix) or `%USERPROFILE%\.pypirc` (Windows) file, such as
    ```
    [distutils]
    index-servers=
        pypi
        pypitest

    [pypi]
    username = ...
    password = ...

    [pypitest]
    repository = https://test.pypi.org/legacy/
    username = ...
    password = ...
    ```
    
1. Install [twine](https://pypi.org/project/twine/)

   `pip install --upgrade twine`


1. Make sure your python's script folder is in your PATH system variable. For example, on my machine, I have `%APPDATA%\Python\Python37\Scripts` included in the `%PATH%`, SO THAT

1. Do the following steps
    ```
    cd /your/project/base/
    python setup.py sdist bdist_wheel
    pip install --upgrade twine
    cd dist
    del /remaining/unnecessary/files/under/dist/
    cd ..
    REM twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    twine upload -r pypitest dist/*
    ```

1. You will be prompted for the username and password you registered with Test PyPI.

1. Test-install and test-run the package:
`python -m pip install --index-url https://test.pypi.org/simple/ your_pkg`

1. Upload to the main PyPI site: 
`twine upload -r pypi dist/*`
