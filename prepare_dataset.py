
import os
import sys
import wandb

# Downloading the dataset
url = "https://activeeon-public.s3.eu-west-2.amazonaws.com/datasets/MNIST.new.tar.gz"
print("download:", url, file=sys.stderr)

os.system("mkdir dataset")
os.system("wget -O dataset/MNIST.tar.gz {}".format(url))
os.system("tar -zxvf dataset/MNIST.tar.gz -C dataset/")

#Uploading the dataset to wandb

run = wandb.init(entity='gigl', project='mnist_wandb', job_type='prepare_dataset')
artifact = wandb.Artifact(name='mnist', type='dataset')
artifact.add_dir("./dataset")
run.log_artifact(artifact)



