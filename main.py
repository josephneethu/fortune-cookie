#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import random

def getRandomFortune():
    #list of fortunes
    fortunes = [
    "All things are difficult before they are easy",
    "The fortune you seek ,is in another cookie",
    "I cannot help you much ,I'm just a cookie",
    "The early bird get the worm, but second mouse gets the cheese",
    "Meh 404 Fortune not found ,try another"
    ]
    #randomly select one fortune to display
    index = random.randint(0,4)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        fortune = "<strong>" +getRandomFortune()+ "</strong>"
        fortune_sentence= "Your Fortune: "+ fortune
        fortune_paragraph = "<p>" +fortune_sentence+ "</p>"

        refresh_button = "<a href ='.'><button> Another Cookie Please !! </button></a>"

        lucky_number = "<strong>" + str(random.randint(1,100))+ "</strong>"
        num_sentence = "Your Lucky number is: "+str(lucky_number)
        num_paragraph = "<p>" +num_sentence+ "</p>"
        content = header +num_paragraph +fortune_paragraph+refresh_button
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
