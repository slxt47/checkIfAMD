import pyamdgpuinfo


if pyamdgpuinfo.detect_gpus() != 0:
    first_gpu = pyamdgpuinfo.get_gpu(0) 
    vram_usage = first_gpu.query_vram_usage()
    print(f"VRAM Usage: {vram_usage} MB")
else:
    print("No AMD GPUs detected.")
    exit(1)
    
