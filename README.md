# user-agent-evergreen
The user-agent strings of the major browsers, updated daily, as a python package.

## Failure-as-a-service 🎉

The resulting user-agent strings are kinda userless:
* **Chrome** Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) **Headless**Chrome/121.0.6167.139 Safari/537.36
* **Edge** Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) **Headless**Chrome/121.0.2277.98 Safari/537.36 **Headless**Edg/121.0.2277.98
* **Firefox** - (The selenium webdriver failed to match the version of Firefox.)

The point of the exercise was to get the current user-agent strings of the latest major browser. But since we're running them in headless mode, for the GitHub action, we're getting user-agent strings that say we're in headless mode. So it's a failure. Back to the drawring board.

## So, where's the python package? 🧐

Not much point now, innit?
