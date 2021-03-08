# A basic authentication system for django rest API
Before you go, please please an `.env` file in project directory and the content should be same as what your `settings.py` requires. please `settings.py` file, also make sure you have datbase ready what django allows

### Step 01
Install all dependency with `pip install -r requirements.txt`

### step 02
run the server

## Final Step (Play with API on Live)
Hit these follwoing URL to know more details after you run the server
http://127.0.0.1:8000/doc/ `swagger documentation`
http://127.0.0.1:8000/api/docs/ `django rest api doc`


# Error in sending email?
If your `is_active` is `False` by default, then django will not send password reset to your mail.

More about customized email templates: https://github.com/iMerica/dj-rest-auth/issues/9#issuecomment-705426124 \

about email template issue: https://github.com/iMerica/dj-rest-auth/issues/9#issuecomment-757507600 \

Read documents to learn more about configuration the `allauth` or `rest_auth` https://django-allauth.readthedocs.io/en/latest/configuration.html
