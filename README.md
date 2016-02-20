# pysoup
*package managment in a bowl*

### what

Python is a great language: it is flexible, readable and convenient. It also has a wide variety of tools which allow the distribution and setup of projects.

Unlike other environments (such as nodejs) python projects are not natively encapsulated; in order to create self-contained projects, one has to create a virtualenv environment for them, and install the dependencies from within it, or install the dependencies globally.

pysoup comes to solve exactly that. It easily manages your project's dependendencies by creating a private virtualenv environment for it and managing the dependencies within it.

That allows you to easily migrate your project to other environments without having to take care of creating and preparing their dependencies.

### how

pysoup makes use of a configuration file named `soup.yaml` which should be found within your project's root directory. The configuration file defines your project and dictates pysoup what should be prepared.

```yaml
name: 'pysoup'
author: 'Roy Sommer'
version: '0.1.0'
repository: 'https://www.github.com/illberoy/pysoup'
dependencies:
  Twisted: '15.5.0'
  blessings: '1.6.0'
  PyYAML: '3.11'
  argcomplete: '1.0.0'
```

pysoup will then set up a virtualenv directory under `venv` in your project's root, and will install the specified dependencies under it using pip.

### dependency version notation

Each dependency should have one of the following versioning notation as its value:

`1.0.0` - will install precisly version 1.0.0 or nothing at all

`+1.0.0` - will install any version newer or equal to 1.0.0

`-1.0.0` - will install version 1.0.0 at most

`*` - will install any version

### usage

`$ soup install` - read the configuration in the current working directory, create a virtualenv at that directory and install the dependencies specified.

### disclaimer

The project is still in its (very) early development, so unexpected behavior might occure (if your cat eats your mouse all of a sudden, that might, or might not have happened because you've used pysoup). Proceed with caution!

```

       X  X  X
      X  X  X

+------------------+
 +----------------+
   +------------+
   
```
