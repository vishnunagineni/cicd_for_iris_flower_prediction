1.create virtual environment

```cmd
virtualenv name
```
2.Activate environment

```cmd
Scripts\activate
```

3.create requirements.txt and install dependencies using that

```cmd
pip install -r requirements.txt
```
4.download the dataset and put that in data_given


5.git clone or git init empty repository

```cmd
  git init
  dvc init
  dvc add dataset
  git add .
  git commit -m "first commit"
  git branch -M main
  git push
```
6. add stages to the dvc.yaml file for automating the execution of stages in pipeline using dvc repro command

```cmd
  dvc repro
```
7. tox command for automation testing

```cmd
  tox
```
pytest command
```cmd
  pytest -v
```
8. setup command

```cmd
  pip install -e .
```

9. building own packages using wheel and setup

```cmd
  python setup.py sdist bdist_wheel 
```