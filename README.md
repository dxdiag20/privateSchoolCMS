# PrivateSchoolCMS
"PrivateSchoolCMS" can be used at small private school as management system. Usage is simple.         
Just download this site and then run it on your Windows Desktop right away!         
It run on web browser, so anybody can execute  and use this program. And plus this is synchronized with ms office excel.    
You can use style sheet as timetable or learning table.         
## Overview
### [Watch Demo Video](https://youtu.be/yk7QZ5b2Udo)
[![Watch the video](main.PNG)](https://youtu.be/yk7QZ5b2Udo)

## User's Guide
[To User's Guide](https://github.com/dxdiag20/privateSchoolCMS/wiki)
## Bootcamp  
You can download and use this program on your windows desktop 
### Operating Environment
```
Windows over 10,    
Windows Office Excel over 2013,     
python over 3.5 64bit,    
chrome recommended       
```
### Installation
Please install [python 3.5](https://www.python.org/downloads/)     
1. Python packages
```
 - Project download
 $ git clone
 - Open CMD WINDOWS as administor.   
 - move to download location.     
 $ cd download location    
 - install libraries    
 $ pip install -r requirment.txt
 - 위 방법이 아닌 한번에 하는 방법
   다운 받은 폴더로 이동 하여 "pip_install.bat"을 클릭하여 실행
 - 마지막으로 설치 된 장고의 버전 확인 
 $ pip list
 - Django must be 1.9 version. So if it is NOT please re install django.      
   Use this option when you install "pip install django==1.9      
  ```      
2. Run 
```
  $ python manage.py runserver:8000
  Or
  Click runserver.bat    
  ``` 
3. Access "Private CMS" on browser   
```
  Open your browser    
  put "localhost:8000" on browser    
  sign up and register your time sechdule file    
  finally click login    
  ```
4. Admin Site
```
  You can access admin site below address   
  localhost:8000/admin
  ID: admin Password: privatecms
  ```     
## Caution!
 [To Caution Guide](https://github.com/dxdiag20/privateSchoolCMS/wiki/4.-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0%EA%B0%80%EC%9D%B4%EB%93%9C)
```
  When error is occured     
  You can deal with error above site        
  ``` 
## Excel files
1. student_excel folder
```
Writing student's lesson tables    
```
2. tutor_excel/timetable_master.xlsx
```
This is time scheudle of teacher and built in program.     
Make this file as teacher and register this file to teacher's account.     
```
3. tutor_excel/sales.xlsx
```
Daily sales note    
```
## Issue   
Please make issue when problem exist.     
If you have further solution, please pull-request       

## Tech
reference following sources
- [Django](https://www.djangoproject.com/) - Django Web framework
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Excel editing library
- [pywin32](https://pypi.org/project/pywin32/) - Excel editing library
- [sb-admin2](https://startbootstrap.com/template-overviews/sb-admin-2/) - Bootstrap dashboard
- [bootstrap](http://getbootstrap.com/) - Bootstrap
- [Loading jquery](https://www.jqueryscript.net/loading/jQuery-Plugin-To-Handle-CSS3-Powered-Spinners-Loaders-Loading-js.html) - Loading jquery plugin
- [Lobibox](http://lobianijs.com/site/lobibox) - Boostrap alert jquery plugin  

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
