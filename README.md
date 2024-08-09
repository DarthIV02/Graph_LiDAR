# Graph_LiDAR
Testing for graph LiDAR segmentation

conda create --name graph_lidar python=3.7
tmux new-session -s jupyter
conda activate graph_lidar

python -m ipykernel install --user --name=graph_lidar
# In another window of the comand prompt
kubectl port-forward <name of the pod> 8888:8888
jupyter notebook --ip='0.0.0.0' --allow-root

