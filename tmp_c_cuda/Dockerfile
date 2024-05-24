FROM nvidia/cuda:12.3.2-devel-rockylinux9

RUN yum -y update && \
    yum -y install \
    gcc \
    gcc-c++ \
    make \
    wget && \
    yum clean all

WORKDIR /usr/src/app

COPY . .

RUN make

# Set the entry point to run the compiled binary
# CMD ["./main"]

