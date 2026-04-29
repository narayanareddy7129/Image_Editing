#### **Git Bash user name, email setup**





veera@Shannu MINGW64 \~

$ git config --global user.name "narayanareddy999 **--> Toa add username to git bash (global)**

"



veera@Shannu MINGW64 \~

$ git config --global user.email "narayanareddy7129@gmail.com

" **--> To add email to git bash (global)** 



laksh@Narayana MINGW64 \~

$ git config --global user.name

narayanareddy999



laksh@Narayana MINGW64 \~

$ git config --global user.email

narayanareddy7129@gmail.com



laksh@Narayana MINGW64 \~ 









#### **Streamlit**





C:\\Users\\laksh\\ML\\streamlit>**python --version**

Python 3.11.3

&#x09;

C:\\Users\\laksh\\ML\\streamlit>**^Z  (crt+z)	--> To get out from python**



###### **To Create Virtual Environment(venv)**

1. C:\\Users\\laksh\\ML\\streamlit>**python -m venv myenv(name)**



###### **To activate environment**

C:\\Users\\laksh\\ML\\streamlit>**myenv\\Scripts\\activate**



###### **to exit from (myenv)**

(myenv) C:\\Users\\laksh\\ML\\streamlit>**deactivate**   



###### **To run the python file**

(myenv) C:\\Users\\laksh\\ML\\streamlit>**streamlit run file\_name.py**



**--> To stop the application after running the file click (ctr+c)**



================================================================ 



##### **commands in git(versions)**



###### **creates git repository in the myenv**

**--> git init** 



**From now the git will tracks changes in the file.**



**U - file/folder under tracking**

**A - file about to track and need to commit that file**

**M - Modification**



###### **Gives information related file and folder**

**--> git status**



###### **To track changes**

**--> git add file\_name.py**



###### **Commit/saving the changes permanently**

**--> git commit -m 'version\_name'** 



###### **To check all the commits**

**--> git log --online**



###### **changes the code corresponding to the version**

**--> git checkout <commit id>** (changes the code corresponding to the version)





&#x20;

##### **TO PUSH ALL FILES INTO GITHUB** 



###### **To change to another file**

**--> git checkout  master or (commit id)**



**git remote add origin https://github.com/narayanareddy7129/Image\_Editing.git (new repository url)** 





**git remote -v (to check in which repository you are in)**



(myenv) C:\\Users\\laksh\\ML\\streamlit>git remote -v



**output:**



origin  https://github.com/narayanareddy7129/Image\_Editing.git (fetch)

origin  https://github.com/narayanareddy7129/Image\_Editing.git (push)





###### **TO PUSH ALL FILES INTO REPOSITORY**

&#x20;

**step-1: (Goes to main branch)**

**git checkout master**  



**Step-2: (to name the main branch as main**)

**git branch -M main** 



**Step-3: (Push)**

**git push -u origin main**





**========================================================** 





