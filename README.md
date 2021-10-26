### Webgenesis
A simple command line interface for generating hello-world starter apps for 
quick setup


#### Why Webgenesis?
When building web apps, it can become common to be starting from the same or similar set of code and basic project structure. Hence webgenesis comes in to
reduce this burden of writing the same code when starting up a web project



#### Installation
```bash
pip install webgenesis
```


#### Usage
```bash
webgenesis --help

```


#### Create A Project for a web framework
+ Uses the default 'hello-<webframework>' as project folder
+ Supported frameworks include
	- flask
	- streamlit
	- express
	- koajs
	- bottle
	- tornado
	- fastapi

```bash
webgenesis create flask

```

```bash
webgenesis create streamlit

```

#### Create A Project using Custom/Specified Project
```bash
webgenesis create flask -f myflaskapp
```



#### About
+ Maintainer: Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech


#### Contributions
Contributions are welcome. In case you notice a bug let us know.
Happy Coding
