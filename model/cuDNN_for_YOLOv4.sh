# CUDA: Let's check that Nvidia CUDA drivers are already pre-installed and which version is it.
/usr/local/cuda/bin/nvcc --version
# We need to install the correct cuDNN according to this output

nvidia-smi

# Change the number depending on what GPU is listed above, under NVIDIA-SMI > Name.
# Tesla K80: 30
# Tesla P100: 60
# Tesla T4: 75
%env compute_capability=60

#Install cuDNN according to the current CUDA version
