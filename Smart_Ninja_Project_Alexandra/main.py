#!/usr/bin/env python
import os
import jinja2
import webapp2
import datetime
import model


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("homeis.html")

class AboutMeHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class BlogHandler(BaseHandler):
    def get(self):
        messages = model.Message.query().fetch()
        return self.render_template("blog.html",
                                    params={"messages": messages})

    def post(self):
        name = self.request.get("name")
        message_text = self.request.get("message_text")
        message = model.Message(message_text=message_text, name=name)
        message.put()
        return self.redirect_to("blog")

class MyProjectsHandler(BaseHandler):
    def get(self):
        return self.render_template("myprojects.html")

class ContactHandler(BaseHandler):
    def get(self):
        return self.render_template("contact.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/hello', AboutMeHandler),
    webapp2.Route('/blog', BlogHandler, name="blog"),
    webapp2.Route('/myprojects', MyProjectsHandler),
    webapp2.Route('/contact', ContactHandler),
], debug=True)
