import storage
from twisted.web import http, resource, static
from django.template import loader, Template, Context
from datetime import datetime, timedelta


class TemplatedResource(resource.Resource):

	def __init__(self, template_filename):
		resource.Resource.__init__(self)
		self.template = loader.get_template(template_filename)

	def render_template(self, context, request):
		request.setHeader("Content-Type", "text/html; charset=utf-8")
		response = self.template.render(context).encode('utf-8')
		request.write(response)
		return ""

class Index(TemplatedResource):

	isLeaf = False

	def render_GET(self, request):
		digest = storage.TREE.get_digest([10, 60, 240, 1440, 2880])
		context = Context(digest)
		return self.render_template(context, request)

class Root(static.File):

	isLeaf = False

	def __init__(self, path, defaultType="text/html", ignoredExts=(), registry=None, allowExt=0):
		static.File.__init__(self, path)
		self.index = Index('index.html')

	def directoryListing(self):
		return self.index

class Digest(TemplatedResource):

	isLeaf = True

	def render_GET(self, request):
		if 'min' in request.args:
			digest = storage.TREE.get_digest([int(request.args['min'][0])])
		else:
			digest = storage.TREE.get_digest([10, 60, 240, 1440, 2880])
		context = Context(digest)
		return self.render_template(context, request)

class Pattern(TemplatedResource):

	isLeaf = True

	def render_GET(self, request):
		minutes = int(request.args['min'][0])
		td = datetime.now() - timedelta(minutes=minutes)
		context = storage.TREE.get_details(int(request.args['hash'][0]), td)
		context.update({'minutes': minutes})
		return self.render_template(Context(context), request)

class Data(TemplatedResource):

	isLeaf = True

	def render_GET(self, request):

		td = datetime.now() - timedelta(minutes=int(request.args['min'][0]))
		inthash = int(request.args['hash'][0])
		host = request.args['host'][0]
		context = Context(storage.TREE.get_host_data(inthash, host, td))
		return self.render_template(context, request)

class Metrics(TemplatedResource):

	isLeaf = True

	def render_GET(self, request):

		context = Context(storage.TREE.metrics)
		return self.render_template(context, request)
