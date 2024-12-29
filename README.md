# Simple Django Blog
This is a simple Django blog and I am using `Function-based views`, later I will create advanced blog using `Class-base views` and upload it to my GitHub.
In this project, the user can create, read, update and delete a blog there is pagination too where a user will be fecthing 5 blogss per page.

![Django Blog](https://github.com/user-attachments/assets/0358ba83-04ab-4e0e-b6e7-47f74ce8b6e1)

![Blogs](https://github.com/user-attachments/assets/6cbd468b-4e38-4d8f-8b2d-04eb4b76b586)



## How to Install and Run the Project
To get this repository, run the following command inside your git enabled terminal.
```
$ git clone https://github.com/bj1111/diyblog.git
```

Before installing the required packages, it is recommended to create a `virtual environment`.

If you don't have the `virtual environment` installed:
```
$ python -m pip install virtualenv
```

Create the Virtual Environment: Run the following command, replacing `env` with the name you want for your environment:

```
$ python -m venv env
```

Activate the Virtual Environment: To activate the environment, use:

  + Windows:
    ```
    env\scripts\activate
    ```
  
  + Mac:
    ```
    source env/bin/activate
    ```
Deactivate the Virtual Environment: When you're done working, you can deactivate the environment with:
```
deactivate
```


After installing and activating the `virtual environment`, run the following command to install all required packages.
```
$ pip install -r requirements.txt
```
## How to Use the Project
In the same directory where `manage.py` is located, run this command to start the server.
```
$ py manage.py runserver
```
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and click `Sign up` or `Login` in the navigation bar.

The default superuser is:
+ username = _admin_
+ password = _Brij##125_

Once you're logged in, go to `My Blogs` in the navigation bar, where you can manage your blog.

![My Blogs](https://github.com/user-attachments/assets/7b3e2d20-8117-4f03-8d14-f99f24615a96)

You can see user's details in `Profile` in navigation bar, there you can change the password.

![Profile](https://github.com/user-attachments/assets/f25e4b02-0b97-48a8-b476-d25af7b86cc6)


You can run the test by running the command given below.

```
python manage.py test blog
```
here is the image of the test cases been ran.
![testcases](https://github.com/user-attachments/assets/c0f8995a-6709-43e7-802a-9d8d196be242)






# Goodbye!
Thank you for taking the time to explore this simple Django blog project. I hope you find it helpful and informative as you learn more about Django and web development. If you have any questions, feel free to reach out. Happy coding, and goodbye!


  
