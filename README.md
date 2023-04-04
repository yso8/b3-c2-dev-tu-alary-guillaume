## Calculate - by yso8 & louisalr

[![Pipeline Status](https://gitlab.com/ys8o/b3-c2-dev-tu-alary-guillaume/badges/main/pipeline.svg)](https://gitlab.com/ys8o/b3-c2-dev-tu-alary-guillaume/-/pipelines)

This calculator includes unit tests & an allocated Jenkins pipeline.

Python powered by Coverage/UnitTest

#### <ins>Main menu</ins> : 
![image](https://user-images.githubusercontent.com/73800791/224673065-a254a99b-e37f-4dd4-89ae-3668f286e577.png)

#### 1. <ins>Calculation functionality</ins> :
![image](https://user-images.githubusercontent.com/73800791/224673821-fa03d434-d274-49b2-a2e8-42907405c347.png)

#### 2. <ins>Display of credits</ins> : 
![image](https://user-images.githubusercontent.com/73800791/224674003-f5efc150-017c-4265-b5ce-0c1925e2e792.png)

## Documentation
## Features

- Calculate an arithmetic expression including {+, -, *, /, ^, %, √}
- Launching the test pipeline made with Jenkins
- Display programme credits
- Leaving it

## Tech

- Python
- UnitTest - Tests
- Coverage - Test coverage
- Jenkins - Pipeline 

## Installation

Once the repository is cloned 

To start the program : 
```sh
py main.py 
```

To run the tests :
```sh
py test_calculator.py
```

To use coverage :
```sh
py coverage run test_calculator.py
py coverage html test_calculator.py
```

## GitLab

The gitlab repository : https://gitlab.com/ys8o/b3-c2-dev-tu-alary-guillaume

Test pipeline on gitlab : .gitlab-ci.yml
```yml
stages:
  - test

test-job: 
  stage: test
  image: python:alpine3.16
  script:
    - python test_calculator.py

```

## Jenkins

to see the Jenkins pipeline, look at the pdf available ('integration-continu.pdf') in the repository


**Free Software, Hell Yeah!**
