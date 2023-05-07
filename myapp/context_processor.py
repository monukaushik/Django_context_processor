import datetime
def cur_datetime(request):
   curdate=datetime.datetime.now()
   return { 'current_date':curdate }


# Context processors are a way to provide common context variables to all templates in your project without having to pass them explicitly to each template. They are especially useful for providing variables that are used on many or all pages of your website, such as the current user or site settings.

# When a view function or class-based view returns a rendered template, the context dictionary returned by the view is merged with the context variables provided by the context processors before being passed to the template engine.

# To use a context processor, you need to define a Python function that returns a dictionary of context variables, and then register the function in your Django project's settings.py file. Once registered, the context variables provided by the context processor will be available in all templates.