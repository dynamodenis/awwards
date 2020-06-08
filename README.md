# AwwardMe

Developer: Dynamo Denis Mbugua

Email: dmbugua66@gmail.com

To run this site click [here](https://awwardme.herokuapp.com/)

Location: Nairobi, Kenya

---
## Description

This an application where developers can be a able to post their projects and other developers can be able to vote and gauge their views on the application.

---
## Technologies used

- Python(Django)
- Pipenv
- Bootstrap4
- Heroku

---

## Installation
- Clone the repository directly to your pc using this command
```
https://github.com/dynamodenis/awwards.git
```
- To be able to run this project on your PC you need to have python already installed Python version 3.6 and above. Incase you dont have it use this commands to install

```
$ sudo add-apt-repository ppa:jonathonf/python-3.6
$ sudo apt-get update
$ sudo apt-get install python3.6
```
- Install Python command tool called PIP Where we going to use pipenv to install 3rd party extentions and virtual environment which comes preinstalled in linux and mac.
For linux use this to install pip
```
$ sudo apt-get install python3-pip 
```
- For mac 0S use this command to install pip
```
sudo easy_install pip
```
- Open your editor and run the cloned repository and install the modules below to run effectivey.

- To install all requirements and extentions needed to run the app install pipfile using
```
pipenv lock -r 
```

- To run the class test use the following commands in the terminal
```
python3.6 manage.py test project
```

- Now your ready to run the modules type the fillowing commands to run the app locally.
```
python3.6 manage.py runserver
```
---
## How to use the api

For our api which is supposed to help other developers to user our data you will need to be authorized bu a token. We recomend to use ***PostMan*** which helps makes http requests to fetch data and get your token.

```
On Post Man choose the url choose POST request www.awwardme.heroku.com/api-auth-token/
on the body where u pass in username and your password to register for auth token.

```

#### Getting users using api endpoint

To be able to get and use our users data who have signed up in our application use then following end point
```
www.awwardme.heroku.com/api/users/
```

To get a specific user, your pass in the user id on the url to get user example
```
www.awwardme.heroku.com/api/users/5/

5 in the above url represents the id of the user of type int
```
#### Getting project using api endpoint

To be able to get and use our project data who have signed up in our application use then following end point

```
www.awwardme.heroku.com/api/project/
```

To get a specific project, your pass in the project id on the url to get project example
```
www.awwardme.heroku.com/api/users/5/

5 in the above url represents the id of the project of type int
```





---


## Contribution

Fell free to contribute or help to make the **awwardme** module better. Follow the above instructiom.

- Fork the project repository/clone
- Creat this new Branch (git checkout -b feature/improve-awwardme(name of module))
- Make intended changes and Add the changes made
- Make the commit(git commit -m "improve-awwardme(name of module)")
- Create an upstream if u dont have one(git remote add origin https://github.com/dynamodenis/awwards.git)
- Push the changes to my repo(git push origin improve-insta-poster(name of module)
- Create a pull request.

---
## Bugs Requests

Just by any chance you get caught up or the site is not responding to certain results, feel to post your issue [here](https://github.com/dynamodenis/awwards/issues/new)

## License

This Project is licensed by [MIT](License)



