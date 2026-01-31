class Browser:
    def make_http_request(self,url):
        print("Making HTTP request",url)
    def make_http_request(self,url , auth=None):
        print("Making HTTP requests",url, auth)

b = Browser()
b1 = b.make_http_request("http://example.com","auth-token")  # This will work
b2 = b.make_http_request("http://example.com")  # This will also work
print(b1)
print(b2)