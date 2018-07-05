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


### How to use ([demo](https://youtu.be/AUJwK9-V4J0))
```bash
$ git clone https://github.com/qqwaszx/blackowl.git
$ python main.py

: blackowl > help
```


### Modules /core/modules/
+ CMS Gathering : `CMS Detection`
+ Email to Domain : `Get domain with email`
+ Hackedmail : `Check if email as been hacked`
+ IP Geolocation : `Obtain IP geolocation information`
+ Namech_k : `Get info on a specific person with his username`
+ Subdomain Search : `Search for subdomain`
+ Whois Domain : `Whois information for domain`

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
