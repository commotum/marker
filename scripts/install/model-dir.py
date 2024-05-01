import os

def create_models_dir():
    home_dir = os.path.expanduser("~")
    models_dir = os.path.join(home_dir, ".models")
    
    if not os.path.exists(models_dir):
        print("Creating .models directory")
        os.makedirs(models_dir)
    else:
        print(".models directory already exists")
    
    marker_dir = os.path.join(models_dir, "marker")
    
    if not os.path.exists(marker_dir):
        print("Creating marker directory within .models")
        os.makedirs(marker_dir)
    else:
        print("marker directory already exists within .models")

if __name__ == "__main__":
    create_models_dir()