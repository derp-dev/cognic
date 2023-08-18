```
username= Ubuntu
password= swed24sw
```

**Dockerfile**

```
FROM ubuntu:16.04
ARG SMB_PASS
ARG SMB_USER
# Creates a new User
RUN useradd -ms /bin/bash $SMB_USER
# Enters the password twice.
RUN echo "$SMB_PASS\n$SMB_PASS" | smbpasswd -a $SMB_USER
```

**Terminal Command**

`docker build --build-arg SMB_PASS=swed24sw --build-arg SMB_USER=Ubuntu . -t IMAGE_TAG`
____
Use `--build-arg` with each argument.

If you are passing two argument then add `--build-arg` with each argument like:

```
docker build \
-t essearch/ess-elasticsearch:1.7.6 \
--build-arg number_of_shards=5 \
--build-arg number_of_replicas=2 \
--no-cache .
```
____
The above answer by pl_rock is correct, the only thing I would add is to expect the ARG inside the Dockerfile if not you won't have access to it. So if you are doing

```
docker build -t essearch/ess-elasticsearch:1.7.6 --build-arg number_of_shards=5 --build-arg number_of_replicas=2 --no-cache .
```

Then inside the Dockerfile you should add

```
ARG number_of_replicas
ARG number_of_shards
```
____
### ENTRYPOINT (default command to execute at runtime)[](https://docs.docker.com/engine/reference/run/#entrypoint-default-command-to-execute-at-runtime)

The `ENTRYPOINT` of an image is similar to a `COMMAND` because it specifies what executable to run when the container starts, but it is (purposely) more difficult to override. The `ENTRYPOINT` gives a container its default nature or behavior, so that when you set an `ENTRYPOINT` you can run the container _as if it were that binary_, complete with default options, and you can pass in more options via the `COMMAND`. But, sometimes an operator may want to run something else inside the container, so you can override the default `ENTRYPOINT` at runtime by using a string to specify the new `ENTRYPOINT`. Here is an example of how to run a shell in a container that has been set up to automatically run something else (like `/usr/bin/redis-server`):

```
 docker run -it --entrypoint /bin/bash example/redis
```

or two examples of how to pass more parameters to that ENTRYPOINT:

```
 docker run -it --entrypoint /bin/bash example/redis -c ls -l
```

```
 docker run -it --entrypoint /usr/bin/redis-cli example/redis --help
```

You can reset a containers entrypoint by passing an empty string, for example:

```
 docker run -it --entrypoint="" mysql bash
```

> **Note**
> 
> Passing `--entrypoint` will clear out any default command set on the image (i.e. any `CMD` instruction in the Dockerfile used to build it).
_____