class BrowserHistory:
    def __init__(self):
        self.history = []

    def visit_page(self, url):
        print(f"Visiting: {url}")
        self.history.append(url)

    def back_button(self):
        if len(self.history) > 1:
            last_page = self.history.pop()
            print(f"Moving back from: {last_page}")
            print(f"Now at: {self.history[-1]}")
        else:
            print("No more pages in history!")


browser = BrowserHistory()
browser.visit_page("google.com")
browser.visit_page("facebook.com")
browser.visit_page("github.com")

browser.back_button() 
browser.back_button() 