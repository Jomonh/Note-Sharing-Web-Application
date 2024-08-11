## *django notes app*
   Notes Sharing App using django(python framework)
   
###  *Prerequisites:*
  ``` Python Version >> 3.7.8```

  ```Virtualenv setup```

###  *Features*
   - A registerd user can access all the notes shared/added by the admin
   - Can download the pdfs
   - can request specific notes
   - Admin can handle all the feattures like adding/updating/deleting the notes/users and can have overall control.
   - sqlite3 database

## Getting Started

To get started with this project, you have two options:

### 1. *Clone the Repository*
   - Use the following link to clone the repository to your local machine:
    
     ```bash
     git clone https://github.com/Jomonh/Note-Sharing-Web-Application.git

     
   - Once cloned, navigate to the project directory:
     
     ```bash
     cd Note-Sharing-Web-Application


### 2. *Fork the Repository*
   - If you prefer, you can directly *fork* this repository.
   - Click the *Fork* button at the top-right of this page.
   - After forking, clone the repository from your account:

     ```bash
     git clone https://github.com/your-username/your-forked-repository.git


###  *Virtualenv Setup*
1.    <code>python -m install virtualenv</code> or <code>pip install virtualenv</code> 
&nbsp;
3.    <code>virtualenv (environment_name)</code>
&nbsp;
5.    <code>environment_name\Scripts\activate</code>
&nbsp;

###  *Run Project*
1.  <code>First Locate to project folder in cmd with virtual environment running</code>
&nbsp;
2.  <code>pip install -r requirements.txt</code>
&nbsp;
3.  <code>python manage.py makemigrations</code>
&nbsp;
4.  <code>python manage.py migrate</code>
&nbsp;
5.  <code>python manage.py createsuperuser</code>
&nbsp;
6.  <code>python manage.py runserver</code>


Paste this <code>127.0.0.1:8000</code> IP Address on any browser and it will start.

<code>127.0.0.1:8000/admin</code> and enter your superuser's username/pass for django admin panel access
     

### 🌟 *Don’t Forget to Star!*
   - If you find this project useful, please consider giving it a star ⭐. It helps others discover it too!

###  *License*
   - This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/MIT) file for details.
