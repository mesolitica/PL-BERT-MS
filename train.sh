while true; do
  HF_HOME="/workspace/cache" torchrun --nproc_per_node 4 -m train || echo "Command failed. Restarting..."
done