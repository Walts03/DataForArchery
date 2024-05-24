#include <stdio.h>

// Kernel function to add the elements of two arrays
__global__
void Add(int n, float *x, float *y) {
  int index = blockIdx.x * blockDim.x + threadIdx.x;
  int stride = blockDim.x * gridDim.x;
  for (int i = index; i < n; i += stride) {
    y[i] = x[i] + y[i];
  }
}

int main(void) {
  int n = 1 << 20;  // 1M elements

  float *x, *y;

  // Allocate Unified Memory – accessible from CPU or GPU
  cudaMallocManaged(&x, n * sizeof(float));
  cudaMallocManaged(&y, n * sizeof(float));

  // Initialize x and y arrays on the host
  for (int i = 0; i < n; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  // Run kernel on 1M elements on the GPU
  int block_size = 256;
  int num_blocks = (n + block_size - 1) / block_size;
  Add<<<num_blocks, block_size>>>(n, x, y);

  // Wait for GPU to finish before accessing on host
  cudaDeviceSynchronize();

  // Check for errors (all values should be 3.0f)
  float max_error = 0.0f;
  for (int i = 0; i < n; i++) {
    max_error = fmax(max_error, fabs(y[i] - 3.0f));
  }
  printf("Max error: %f\n", max_error);

  // Free memory
  cudaFree(x);
  cudaFree(y);

  return 0;
}

