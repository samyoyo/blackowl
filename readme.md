## Black Owl

This is a simple tool to gather information, based on [Operative-Framework](https://github.com/graniet/operative-framework) (Thanks [@graniet75](https://twitter.com/graniet75))


### Requirements
+ requests
+ pythonwhois
+ beautifulsoup4

##### Install requirements
```bash
$ pip install -r requirements.txt
```


### How to use
```bash
$ git clone https://github.com/qqwaszx/blackowl.git
$ python main.py

: blackowl > help
```


### Modules /core/modules/
+ CMS Gathering
+ Email to Domain
+ Hackedmail
+ IP Geolocation
+ Namech_k
+ Subdomain Search
+ Whois Domain

#### Write module
+ Create new module:
```
: blackowl > new_module
: blackowl(New module name ?) > my_module
: blackowl(New module description ?) > This is a module
```
+ Write your code in 'def main(self):':
```
$ vim core/modules/my_module.py
```
