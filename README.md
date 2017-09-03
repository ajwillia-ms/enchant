# Enchant CMS

A cloud based CMS to easily manage a collection of statically generated sites.

## Running

The app contains a wsgi file "application.py" but if you want to run on the
command like you can call "run.py".

## Usage

You can browse with the following useful URLs

* http://127.0.0.1:5000/sites - list sites managed
* http://127.0.0.1:5000/sites/example - see the example site included

And if you're looking to try out the API then why not use this graphql
query which will list all the pages on all sites along with their titles.

```
http://127.0.0.1:5000/api?query={sites{name,title,pages{name,title}}}
```


