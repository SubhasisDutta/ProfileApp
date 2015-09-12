# NoteBook
Google App Engine Java 
Notebook
========

A profile Web Application based on Google App Engine developed using Python.


To Deploy
appcfg.py -A <appID> update <Root Folder>/ --noauth_local_webserver

Using the command get the URL then after geting he code paste it in the Code box.
This will deploy the app.

    https://accounts.google.com/o/oauth2/auth?scope=https%3A%2F%2Fwww.googleapis
.com%2Fauth%2Fappengine.admin+https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcloud-pl
atform&redirect_uri=urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob&response_type=code&clien
t_id=550516889912.apps.googleusercontent.com&access_type=offline

Enter verification code:

## Setup Instructions
1. Update the value of `application` in `app.yaml` to the app ID you
   have registered in the App Engine admin console and would like to use to host
   your instance of this sample.
   
   
   
Reference
http://brizzled.clapper.org/blog/2008/08/07/writing-blogging-software-for-google-app-engine/