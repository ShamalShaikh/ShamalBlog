#!/usr/bin/python2.7
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Configuration options for the application.

  OAuth 2.0 Client Settings:
    Visit the APIs Console (https://code.google.com/apis/console/) to create or
    obtain client details for a project.
    Authorized Redirect URIs for your client should include the hostname of your
    app with /admin/auth appended to the end.
    e.g. http://example.appspot.com/admin/auth

  XSRF Settings:
    This is used to generate a unique key for each user of the app.
    Replace this with a unique phrase or random set of characters.
    Keep this a secret.
"""

__author__ = 'shamalshaikh@gmail.com (Shamal Shaikh)'

# OAuth 2.0 Client Settings
AUTH_CONFIG = {
    'OAUTH_CLIENT_ID': '720805358899-0q2id4fe5aam31p3h2moc5fdv3bid6e2.apps.googleusercontent.com',
    'OAUTH_CLIENT_SECRET': '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',

    # E.g. Local Dev Env on port 8080: http://localhost:8080
    # E.g. Hosted on App Engine: https://your-application-id.appspot.com
    'OAUTH_REDIRECT_URI': '%s%s' % (
        'https://shamalblogs.el.r.appspot.com',
        '/admin/auth')
}

# XSRF Settings
XSRF_KEY = 'SAY HE IS ALLAH! THE ONE! THE ETERNAL REFUGE! HE NEITHER BEGETS NOR BORN! AND THERE IS NOTHING LIKE HIM!'
