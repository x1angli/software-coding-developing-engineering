Dear friends,

This is a git submodule/subrepo that contains a bunch of Python sub-projects. 

Since Python is almost the full-stack language, we chose it in favor of other languages. Python is cross-platform and almost universally supported. Except for browser front-end, applications written in Python spans all the way from IoT (Internet of Things, such as wearable devices) to backend server applications, to big data solutions.   

All projects under this group are intended to be practical. Some are boilerplate examples to be reused by the general public in the future. Others solve common problems in our daily life or coding. 

Additionally, these projects serve as educational purposes. We use these projects to train new hires or Python beginners. Through our daily development, we found that experienced programmers have their own problems as well -- for example, then tend to use Java-like syntax, which slows the code progress and makes the code base more difficult to maintain. Of course, you are welcome to submit your pull request to improve the code.

## Introduction of Projects

### diff-str

This a single-module project whose purpose is to compare two collections/lists/arrays of strings. Assuming you have a bunch of strings (namely group A),  and another group B. What strings are shared by both groups in common? What only show up in group A, and group B, respectively? This project will solve your problem. 


### bulk-rename

This python script renames all files matching a hard-coded RE under a folder. 

Note: to keep a minimalistic style, I intentionally made this file as hard-coded (rather than flexible and adpative). Therefore, you are supposed to have basic knowledge of Python as well as regular expression. 

### encoding-base

Python ships with an in-house Base64/Base16 encoder and decoder. Still, I provide my own implementation. This code snippet has following purposes: 
* To teach python learners the MIME Base64 spec. Also, to showcase how to manipulate byte-level date in Python
* To provide a flexible and extendable encoding/decoding solution, so that users can write it to encode data in any format (which is specified by passing in a "base alphabet"). Since most data-transfering protocols prohibit using certain characters, the existance of such encoding solution will maximize data density without breaking protocol limitations


### char2img

This tool generates a large image or PDF file for each individual character in a string. 
It supports East Asian languages such as Chinese, Korean and Japanese.
