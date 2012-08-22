#!/usr/bin/env python
#
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""A simple application that demonstrates sharding counters
   to achieve higher throughput.

Demonstrates:
   * Sharding - Sharding a counter into N random pieces
   * Memcache - Using memcache to cache the total counter value in generalcounter.
"""

import webapp2
import jinja2
import os
import generalcounter

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class CounterHandler(webapp2.RequestHandler):
    """Handles displaying the values of the counters
    and requests to increment either counter.
    """

    def get(self):
        template_values = {
          'generaltotal': generalcounter.get_count('FOO')
        }
        template = jinja_environment.get_template('counter.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        generalcounter.increment('FOO')
        self.redirect("/")

  
app = webapp2.WSGIApplication([('/', CounterHandler),
                               ],
                              debug=True)

