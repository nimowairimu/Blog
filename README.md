# Blog

## Author
> Irene Wairimu Mungai, A student at Moringa School.
  There were no contributors apart from Irene Mungai only.

## Description
This is a web application that allows various users to submit a one minute pitch. Users can also be able to view other pitches from different categories ie Enterpreneurship, Interview and Sales, comment on the pitches posted and vote. 

## User Stories
* As a user, I would like to view the blog posts on the site
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.

## Specifications

| Behaviour  |	Input       |	  Output      |
|------------|--------------|-----------------|
|To Sign up | Click Sign up | Registers a new user into the application |
|To Sign In | Click Sign In | For sers who already have accounts to sign into the app|
|Display Various Blog Categories| Click Blogs 	|Various Blogs already posted will be displayed |
|Add your blog |	Click on add blog |Redirects you to a form with title nad content textarea |
|View Random Quotes |	Click quotes  | View random quotes from a quotes api|
|Back to Homepage  |Click home |Redirects a user/subscriber back to home page of the application |
|Add Comment | Click on Add comments | Adds a comment on a blog post |
| Delete Blog  |Click on delete Blog | Delete  blogs that a user finds insulting |

## Prerequisites
Python3.6
## Setup Instructions
1. ``git clone https://github.com/nimowairimu/Blog.git``
1. `` cd Blog``
1. `` python3.6 -m venv virtual`` (install virtual environment)
1. `` source virtual/bin/activate``To activate the virtual environment
1. ``python3.6 -m pip install -r requirements.txt``  To install all dependencies.
1.  Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
`` ./start.sh`` To run the application on your local server 


## Contacts Informantion
 - You can provide feedback or raise any issues/ bugs through my [Email](nimowairimu@gmail.com)
  - Or you can call me on my [Cell](+254704529132)


## Known Bugs
No known bugs of the Application.

## Technologies Used
* Python3.6
* Flask framework
* Bootstrap
* PostgreSQL
## License
MIT (c) 2021 Wairimu Mungai
