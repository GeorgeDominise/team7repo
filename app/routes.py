from app import myapp_obj

@myapp_obj.route("/")
@myapp_obj.route("/home")
def home():
	return "<html><p>Hello, World!</p></html>"
