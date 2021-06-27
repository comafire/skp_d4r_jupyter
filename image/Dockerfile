FROM nvidia/cuda:11.0-cudnn8-devel-ubuntu18.04 
# for GeForce GT 750M, capability: 3.0 cuda architecture
# FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04 
LABEL maintainer="comafire@gmail.com"

USER root

# Bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
apt-utils sudo \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

# User
ARG username
ARG userid
ARG userhome=/home/${username}
RUN echo "username=${username}, userid=${userid}"
RUN adduser ${username} --uid ${userid} --gecos '' --disabled-password \
&& echo "${username} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${username} \
&& chmod 0440 /etc/sudoers.d/${username}

# Lang
ARG locale="ko_KR.UTF-8"
ENV LOCALE ${locale}
RUN echo "LOCALE: $LOCALE"
RUN if [[ $LOCALE = *ko* ]] \
; then \
apt-get update && apt-get install -y --no-install-recommends \
locales language-pack-ko fonts-nanum* \
; else \
apt-get update && apt-get install -y --no-install-recommends \
locales language-pack-en \
; fi
RUN echo "$LOCALE UTF-8" > /etc/locale.gen && locale-gen
ENV LC_ALL ${LOCALE}
ENV LANG ${LOCALE}
ENV LANGUAGE ${LOCALE}
ENV LC_MESSAGES POSIX

# Common
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential vim curl wget git git-flow cmake bzip2 sudo unzip net-tools \
libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev sqlite3 libsqlite3-dev llvm \
libfreetype6-dev libxft-dev libcurl4-gnutls-dev libxml2-dev 
RUN apt-get update && apt-get install -y --no-install-recommends \
software-properties-common libjpeg-dev libpng-dev ncurses-dev imagemagick \
libgraphicsmagick1-dev libzmq3-dev gfortran gnuplot gnuplot-x11 libsdl2-dev \
openssh-client htop iputils-ping
RUN apt-get update && apt-get install -y --no-install-recommends \
freetds-bin krb5-user ldap-utils libffi6 libsasl2-2 libsasl2-modules \
libssl1.1 locales  lsb-release sasl2-bin unixodbc

# Python3 (System)
RUN apt-get update && apt-get install -y --no-install-recommends \
python3 python3-dev python3-pip python3-virtualenv python3-software-properties python3-gdbm
RUN pip3 install --upgrade pip
RUN pip3 install --cache-dir /tmp/pip3 --upgrade setuptools wheel

# Java
RUN apt-get update && apt-get install -y --no-install-recommends \
openjdk-8-jdk maven

# Scala
ENV SCALA_VER 2.12.12
ENV SCALA_HOME /usr/local/scala-${SCALA_VER}

ENV PATH $PATH:$SCALA_HOME/bin
RUN curl -sL --retry 3 --insecure \
"https://downloads.lightbend.com/scala/$SCALA_VER/scala-$SCALA_VER.tgz" \
| gunzip | tar x -C /usr/local/ \
&& ln -s $SCALA_HOME /usr/local/scala

# Julia
ENV JULIA_VER 1.6.1
ENV JULIA_HOME /usr/local/julia-${JULIA_VER}

ENV PATH $PATH:$JULIA_HOME/bin
RUN mkdir ${JULIA_HOME} && cd /tmp && \
    wget -q https://julialang-s3.julialang.org/bin/linux/x64/`echo ${JULIA_VER} | cut -d. -f 1,2`/julia-${JULIA_VER}-linux-x86_64.tar.gz && \
    tar xzf julia-${JULIA_VER}-linux-x86_64.tar.gz -C ${JULIA_HOME} --strip-components=1 && \
    rm /tmp/julia-${JULIA_VER}-linux-x86_64.tar.gz
RUN julia -v
RUN julia -e 'using Pkg;Pkg.update()'

# R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/'
RUN apt-get update && apt-get --allow-unauthenticated install -y --no-install-recommends \
r-base r-base-dev

# NodeJS (System)
RUN apt-get update && apt-get install -y --no-install-recommends \
nodejs npm 
RUN npm install -g n

# Jupyter Deps
RUN apt-get update && apt-get install -y --no-install-recommends \
texlive-xetex

# Change USER
USER ${username}
WORKDIR ${userhome}

# Python3 (User)
ARG pyenv_pyver
RUN git clone https://github.com/pyenv/pyenv.git ${userhome}/.pyenv
ENV PYENV_ROOT ${userhome}/.pyenv
ENV PATH $PYENV_ROOT/bin:$PATH
ENV PYENV_VERSION ${pyenv_pyver}
RUN pyenv install ${pyenv_pyver}
RUN pyenv global ${pyenv_pyver}
RUN pyenv rehash
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ${userhome}/.bashrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ${userhome}/.bashrc
RUN echo 'eval "$(pyenv init --path)"' >> ${userhome}/.bashrc
RUN pyenv versions
RUN eval "$(pyenv init --path)" && python3 --version 
RUN eval "$(pyenv init --path)" && pip install --upgrade pip
RUN eval "$(pyenv init --path)" && pip install setuptools invoke wheel pylint

# Jupyter
RUN eval "$(pyenv init --path)" && pip install jupyterlab

# PySpark
ENV SPARK_VER 3.1.2
RUN eval "$(pyenv init --path)" && pip install pyspark[sql]==${SPARK_VER}

# Jupyter Scala
RUN eval "$(pyenv init --path)" && pip install spylon-kernel

# Jupyter R kernel
ENV R_LIBS ${userhome}/Rlib
ENV R_LIBS_USER ${userhome}/Rlib
RUN mkdir -p ${R_LIBS_USER}
RUN R -e "install.packages(c('curl', 'repr', 'httr'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('devtools'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('pbdZMQ', 'IRdisplay', 'evaluate', 'crayon', 'uuid', 'digest'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('SparkR'), repos='http://cran.rstudio.com/')"
RUN R -e "install.packages(c('IRkernel'), repos='http://cran.rstudio.com/')"
RUN eval "$(pyenv init --path)" && R -e "IRkernel::installspec()"

# Jupyter Julia Kernel
RUN julia -e 'using Pkg;Pkg.update()' && \
julia -e 'using Pkg;Pkg.add("IJulia")' && \
# Precompile Julia packages
julia -e 'using IJulia'

# NodeJS (User) 
ENV N_PREFIX="${userhome}/n"
RUN n lts

# Env
VOLUME /home/${username}/jupyter
VOLUME /home/${username}/notebooks
