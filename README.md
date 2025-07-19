# mlops-artifact-pipeline

# Clone locally:

     git clone https://github.com/maste21/mlops-artifact-pipeline.git

     cd mlops-artifact-pipeline

     Download anocoda from this website - https://www.anaconda.com/download and install it

# Create Conda Environment & Install Dependencies
   Create environment:
   
      conda create -n mlops python=3.8 -y
      conda init
      conda activate mlops
      
    requirements.txt:

      scikit-learn
      joblib
      pytest
      
   Install requirements:
   
      pip install -r requirements.txt
      
# Project Structure

.<img width="220" height="238" alt="image" src="https://github.com/user-attachments/assets/35e17fe2-1a30-4139-83f3-79b547ad5951" />

      

# Branching Strategy

      main: Initial branch with only README.
      classification: For training code/workflows.
      test: For unit tests and testing workflow.
      inference: For inference script and full pipeline workflow.
