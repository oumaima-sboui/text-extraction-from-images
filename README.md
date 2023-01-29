# text-extraction-from-images


## Table of contents
* [About the project](#About-the-project)
* [Technologies and installation](#Technologies-and-installation)
* [Result](#Result)



## About the project

The goal of this project is to detect text from images and extract them, we use images of different cards (passport, residence permit, identity card,..) that are taken from the internet. . 


## Technologies and installation

### Technologies
Project is created with:
* An IDE, text editor or notebook environment
* Python 3.7 - Python 3.10

### installation
apart the basic libraries you have to install 
* [Mongodb](https://www.mongodb.com/) : is a document-oriented database management system
* [paddleocr](https://pypi.org/project/paddleocr/) :aims to create multilingual, awesome, leading, and practical OCR tools that help users train better models and apply them into practice 
* [pymongo](https://pymongo.readthedocs.io/en/stable/):is a Python distribution containing tools for working with MongoDB from Python.

  
  
**paddleocr**
```
pip install "paddleocr>=2.0.1"
```
**pymongo**
```
pip install pymongo==3.5.1
```
**Mongodb**  

Download from [here](https://www.mongodb.com/try/download/compass)


## Result

the result is presented in two different ways :  
*  [csv file](https://github.com/oumaima-sboui/text-extraction-from-images/blob/master/result.csv)
*  database saved in Mongodb


![image](https://user-images.githubusercontent.com/70036966/215360142-62a8a4aa-8ec7-473c-9ec8-931882254ba9.png)



