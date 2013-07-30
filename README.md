Android GCM
-----------

**Caution:** Project is very hacky at the moment.

This is just a sample Android application having push notifications. It shows a toast message and notification when it receives the push notification.

The file gcm_server.py can be used to send messages to the application. 


HOWTO
=====

 1. Configure the application in your editor (preferably Eclipse), add libs/gcm.jar to your buildpath
 2. Change the SENDER_ID attribute in src/com/dhruvb/myapplication/CommonUtilities.java to your Google OAuth project id. Its usually in the URL `https://code.google.com/apis/console/?pli=1#project:<your_project_id_is_this>:access`
 3. Start the application in debug mode, the logcat output will print a device registration id, this id is used by the gcm server to send messages.
 4. Do a `pip install python-gcm`
 5. Change the API_KEY attribute in gcm-server.py.
 6. Run the script as `python gcm-server.py -r <registration-id> -m '<message here>'`

Refer: https://developer.android.com/google/gcm/gs.html for more clear instructions to get SENDER_ID and API_KEY

