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
- ### 2.1 User stories
    - Site Admin
        - As a **Site Admin** I can **approve comments** so that **I can moderate the content in the comments section**
        - As a **Site Admin** I can **delete posts and comments** so that **I can remove potentially fraudulent or harmful content**
        - As a **Site Admin** I can **create a draft post** so that **I can finish writing later**
    - Site User    
        - As a **Site User** I can **view blog posts as a list** so that **I can select one to read**
        - As a **Site User** I can **open specific blog posts** so that **I can read the whole post**
        - As a **Site User** I can **comment on a post** so that **I can engage in the conversation**
        - As a **Site User** I can **like or unlike a post** so that **I can interact with the content**
        - As a **Site User** I can **dislike or undislike a post** so that **I can interact with the content**
        - As a **Site User** I can **register an account** so that **I can log in and comment/like posts**
        - As a **Site User** I can **search for content based on name or location** so that **I can easily find what I'm looking for**
        - As a **Site User** I can **see all posts I've made** so that **I can easily modify or remove posts if needed**
        - As a **Site User** I can **delete my posts** so that **wrong, old or irrelevant information doesn't stay visible**
        - As a **Site User** I can **rate the courts by my experience** so that **other users can be inspired or informed**
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
    - Head Pro S Padel ball - #e2f754
- ### 2.3 Structure of Data
- I used [smartdraw](https://www.smartdraw.com/) for creating the structure of the models. I have included screenshots of it below:

## 3. Features
- Navigation Bar
    - Navigation bar has different links dependant on wether the user is logged in or not
        -  Home, Sign up/Log in if you are logged out
        - Home, Log out if you are logged in
- Blog section
    - This section lists blog posts by the latest created_on date, also displaying likes/dislikes and number of comments
    - It lists them as cards and when you click on the header of the cards it will open that blog post in full width page and where you can commment on the post/like or dislike the court
    - They are paginated by 9 posts per page, three cards per row.
- Footer
    - This section displays copyright information and links to social media accounts.
- Admin section
    - This is only for the site admin but it will be the standard django admin page where the admin can approve posts and comments.


## 4. Future features
- Navigation Bar
    - I'd like to add more links on the site, like a site to donate, and an About section.
    - I'd also like to add the searchbar in the navigation bar as it is a good modern way to structure you site.
- Blog section
    - I'd like to incorporate Google Maps API for allowing user to start typing the adress and then getting suggestions by Google Maps.
    - Each blog post would also have a small window of the map locating the court with an arrow.
- Footer
    - The footer will have a FAQ link added in the future.

## 5. Wireframes

=== Post planning ===

## 6. Technology
- HTML/CSS
- JavaScript
- Python/Django
- Heroku
- PostgreSQL
- Cloudinary

## 7. Testing
- ### 7.1 code validation
- ### 7.2 test cases (user story based with screenshots)
- ### 7.3 fixed bugs
- ### 7.4 supported screens and browsers

## 8. Deployment
- ### 8.1 via Heroku
- ### 8.2 via Github
- ### 8.3 via Gitpod

## 9. Credits
 - Default image - [Tomasz Krawczyk](https://unsplash.com/photos/M2x3A8Q4JbY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
 - Color schema thanks to [Colormind](http://colormind.io/bootstrap/)
 - ERDiagram via [smartdraw](https://www.smartdraw.com/)