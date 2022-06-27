# PadelCourtR
![Logo for the website]()

## Table of Contents
<hr>

### 1. [ Purpose of the project](#1-purpose-of-the-project)

### 2. [ UX](#2-ux)

- ### 2.1[ User Stories](#21-user-stories-1)
- ### 2.2[ Typography and color schema](#22-typography-and-color-schema-1)
- ### 2.3[ Structure](#23-structure-1)

### 3. [ Features](#3-features)

### 4. [ Future features](#4-future-features)

### 5. [ Wireframes](#5-wireframes)

### 6. [ Technology](#6-technology)

### 7. [ Testing](#7-testing)
- ### 7.1[ code validation](#71-code-validation-1)
- ### 7.2[ test cases (user story based with screenshots)](#72-test-cases-user-story-based-with-screenshots-1)
- ### 7.3[ fixed bugs](#73-fixed-bugs-1)
- ### 7.4[ supported screens and browsers](#74-supported-screens-and-browsers-1)

### 8. [ Deployment](#8-deployment)
- ### 8.1[ via Heroku](#81-via-heroku-1)
- ### 8.2[ via GitHub](#82-via-github-1)
- ### 8.3[ via GitPod](#83-via-gitpod-1)

### 9. [ Credits](#9-credits)

## 1. Purpose of the project

I wanted to create a website for something that I love. A sport called Padel. It is one of the fastest growing sports in Sweden and there are opening about 50 to 100 new courts around the country each year. So this website aims to allow users to add padel courts with ratings to either inspire, inform or possibly even warn other users. The community can then search for courts and leave comments wether they agree with the author or not as well as write other helpful information that the author might have missed. Users will then also be able to upvote/downvote the courts.

## 2. UX

- ### 2.1 User stories [(Kanban board can be found here)](https://github.com/pakkONE/Portfolio-Project-4/projects/1) Each user story is a link that takes you to the GitHub issue I have created for each user story
    - Anonymous User
        - [As an **Anonymous User** I can **view blog posts as a list** so that **I can select one to read**](https://github.com/pakkONE/Portfolio-Project-4/issues/1)
        - [As an **Anonymous User** I can **search posts by court name** so that **find posts about courts I'm interested in**](https://github.com/pakkONE/Portfolio-Project-4/issues/9)
        - [As an **Anonymous User** I can **read comments and view likes/dislikes** so that **I can be informed by the content**](https://github.com/pakkONE/Portfolio-Project-4/issues/2)
        - [As an **Anonymous User** I can **read blog posts and see amount of likes/dislieks** so that **I can see which posts are viral**](https://github.com/pakkONE/Portfolio-Project-4/issues/14)
        - [As an **Anonymous User** I can **register an account** so that **I can log in, add posts and comment/like posts**](https://github.com/pakkONE/Portfolio-Project-4/issues/6)
    - Registered User
        - [As a **Registered User** I can **comment on a post** so that **I can engage in the conversation**](https://github.com/pakkONE/Portfolio-Project-4/issues/3)
        - [As a **Registered User** I can **like or unlike a post** so that **I can interact with the content**](https://github.com/pakkONE/Portfolio-Project-4/issues/4)
        - [As a **Registered User** I can **dislike or undislike a post** so that **I can interact with the content**](https://github.com/pakkONE/Portfolio-Project-4/issues/5)
        - [As a **Registered User** I can **see all posts and comments I've made** so that **I can easily modify or remove them if needed**](https://github.com/pakkONE/Portfolio-Project-4/issues/10)
        - [As a **Registered User** I can **delete my posts** so that **wrong, old or irrelevant information doesn't stay visible**](https://github.com/pakkONE/Portfolio-Project-4/issues/11)
        - [As a **Registered User** I can **rate the courts by my experience** so that **other users can be inspired or informed**](https://github.com/pakkONE/Portfolio-Project-4/issues/12)
    - Site Admin
        - [As a **Site Admin** I can **create a draft post** so that **I can finish writing it later**](https://github.com/pakkONE/Portfolio-Project-4/issues/13)
        - [As a **Site Admin** I can **delete posts and comments** so that **I can remove potentially fraudulent or harmful content**](https://github.com/pakkONE/Portfolio-Project-4/issues/8)
        - [As a **Site Admin** I can **approve comments** so that **I can moderate the content in the comments section**](https://github.com/pakkONE/Portfolio-Project-4/issues/7)

- ### 2.2 Typography and color schema

I used [Colormind](http://colormind.io/bootstrap/) to generate a color schema. I decided on two colors to incorporate on my site based on the color on the grass on the best artificial grass for a padel court, called Mondo as well as the color of the padel ball Head Pro S. The details are here beneath. 

- Typography
    - Logo - Anton, Regular, weight: 400
    - The rest - Roboto Condensed, Regular, weight: 300, 400, 700
    - HTML Code:
        - ``` <link rel="preconnect" href="https://fonts.googleapis.com"> ```
        - ``` <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> ```
        - ``` <link href="https://fonts.googleapis.com/css2?family=Anton&family=Roboto+Condensed:wght@300;400;700&display=swap" rel="stylesheet"> ```
    - CSS Code:
        - ``` font-family: 'Anton', sans-serif; ```
        - ``` font-family: 'Roboto Condensed', sans-serif; ```
- Color Schema
    - Blue Aritifical Grass color of padel courts called Mondo - #005387
        - Used as background color for navbar, hover effects over some buttons
    - Head Pro S Padel ball - #e2f754
        - Used as font color on logo and hamburger menu icon on mobile devices

- ### 2.3 Structure of Data

- I used [smartdraw](https://www.smartdraw.com/) for creating the structure of the models. I have included screenshots of it below:

## 3. Features
- Navigation Bar
    - Navigation bar has different links dependant on wether the user is logged in or not
        - Home, Sign up/Log in if you are logged out
        - Home, Add Post, My Activity, Log out if you are logged in
        - Search bar with a function to search posts based on court name. Is not case-sensitive.
- Home/Blog view section
    - Hero image is displayed at the top of this page, with a call-to-action button for users who are not logged in.
    - This section lists blog posts by the latest created_on date, also displaying likes/dislikes and number of comments
    - It lists them as cards and when you click on the header of the cards it will open that blog post in full width page and where you can commment on the post/like or dislike the court
    - They are paginated by 9 posts per page, three cards per row.
- Blog post view
    - Here is a page for each post that display relevant information about the court as well as the content written by the user.
    - There is also a comment section for registered users to comment on the post.
    - Registered users can also upvote/downvote posts.
    - The author of the post will also have two buttons at the bottom of the blog post, one for editing the post and another for deleting the post
- Add Post section (only for regiestered users)
    - Here is a django form with the ability to add a new post for users who are signed in.
    - The image file is optional and if uploaded will be stored on cloudinary. If user does not provide one a placeholder photo will be used.
- Edit Post
    - Users who have added posts has the ability to edit their posts.
- My Activity (only for regiestered users)
    - Here the users comments and posts will be ordered with a link to each post for editing or deleting, as well as for each comment a link to delete the comment
- Confirm delete page
    - Whenever a user clicks on a 'delete post'-button they will be directed to a page asking for their confirmation if they really want to delete the post, with an additional option of going back to the post if they changed their mind.
- Footer
    - This section displays copyright information and links to social media accounts.
- Sign up page
    - Anonymous users has the ability to sing up for an account so that they can add posts, comment on posts and like/dislike posts.
- Sign in page
    - Users who has an account has the ability to sign in to their account.
- Admin section
    - This is only for the site admin but it will be the standard django admin page where the admin can approve posts and comments and handle registered users.

## 4. Future features

- Navigation Bar
    - I'd like to add more links on the site, like a site to donate, and an About section.
- Blog section
    - I'd like to incorporate Google Maps API for allowing user to start typing the adress and then getting suggestions by Google Maps.
    - Each blog post would also have a small window of the map locating the court with an arrow.
- Footer
    - The footer will have a FAQ link added in the future.
- Sign in / Sign up page
    - In the future I will style the forms more to go with the same look as the rest of the page.

## 5. Wireframes

=== Post planning ===

## 6. Technology

- HTML/CSS
    - I used semantic HTML language for the templates
    - Some custom CSS was also done eventhough I used Bootstrap
- JavaScript
    - Some JavaScript was necessary, for Bootstrap as well as eventlistener
- Bootstrap 5.1.3
    - I used Bootstrap for the styling of the webpage and took some inspiration from [this bootstrap blog theme](https://startbootstrap.com/theme/clean-blog)
- Python
    - All additional libraries can be viewed on the [requirements.txt-file](requirements.txt)
- Django
    - Django was the framework used for this project
- Heroku
    - The live project is deployed to [Heroku](https://www.heroku.com/)
- Heroku PostgreSQL
    - To handle the database I used PostgreSQL on Heroku
- Cloudinary
    - As done in the walkthrough project, I also used Cloudinary for storing my static files so that I would not have to rely on Herokus Dynos
- Crispy Forms
    - I also used Crispy forms for the comment form
- FontAwesome
    - My website would not be as cool without the use of FontAwesome and their icons

## 7. Testing

- ### 7.1 code validation
    - HTML
        - HTML code was validated without issues on [W3C HTML Validator](https://validator.w3.org/)
    - CSS
        - CSS code validated without issues on [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator)
    - PEP8
        - All Python code was checked with this [PEP8 validator](http://pep8online.com/)
    - Lighthouse
        - All fields were green on Lighthouse

- ### 7.2 test cases (user story based with screenshots)

- ### 7.3 fixed bugs
    - I encountered a bug saying ``` NoReverseMatch at /admin/blog/post/add/ ```<br>
    ``` Reverse for 'django_summernote-upload_attachment' not found. 'django_summernote-upload_attachment' is not a valid view function or pattern name. ```
        - I solved this by adding ``` path('summernote/', include('django_summernote.urls')), ``` to padelcourtr/urls.py instead of blog/urls.py
    - When I am trying to dislike a post and clicking the thumbs down icon, it adds a number to the liked count.
        - This was solved by changing the name of the button from ``` name="bloglike_id" ``` to ``` name="blogdislike_id" ```
    - While logged in and viewing the 'my acitivity' template, there are two separate submit buttons, one for submitting a comment and the other for wanting to delete your comment. The form on the right hand side wouldn't allow me to delete my comment before I filled in the submit comment form as it can't be left blank.
        - To solve this I had to create an eventlistener via JavaScript to prevent default on the delete comment button
    - 
- ### 7.4 supported screens and browsers
    - I have tested this on Safari, Chrome and Brave as well as Safari on iOS.
    - The site works well with responsive design and looks incredible also on smaller screen devices.

## 8. Deployment

- ### 8.1 via Heroku
- ### 8.2 via Github
- ### 8.3 via Gitpod

## 9. Credits

 - Default image - [Tomasz Krawczyk](https://unsplash.com/photos/M2x3A8Q4JbY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
 - Color schema thanks to [Colormind](http://colormind.io/bootstrap/)
 - ERDiagram via [smartdraw](https://www.smartdraw.com/)
 - As one of the walkthrough projects also used, I used a [blog theme](https://startbootstrap.com/theme/clean-blog) from startbootstrap.com
 - I'd like to thank my mentor, Rohit, for providing me with helpful ideas and great support throughout the course of this project.
 - The walkthrough projects of this program has also provided me with tips, helpful tools and inspiration to take my projects to the next level.
 - The Tutor Support Team at Code Institute has been very helpful in solving some issues and providing me with knowledge as well as resources for further reading.
 - I have also gained some great tips and ideas from my fellow students at Code Institute. The community is truly amazing and has both inspired and challenged me.