# Makefile

# Compiler
NVCC = nvcc

# Flags
CFLAGS = -arch=sm_50

# Target
TARGET = main

# Source files
SRC = main.cu

# Build target
all: $(TARGET)

$(TARGET): $(SRC)
	$(NVCC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)

