### Project 70% complete..
# Nuclei image segmentation

## A computer vision segmentation model built on UNET architecture, capable of capturing Nuclei cells in an image.

## Index
1. [About](#about)
2. [Demo](#demo)
3. [Technologies](#tech)
4. [Usage](#usage)
    * [Installation](#installation)
5. [Developer Features](#dev)
6. [Future Improvements](#future)
    * [Efficiency and AI Power](#power)
7. [Credits](#credits) 
8. [License](#license)
 

<a name="about"></a>
## About
Introducing our segmentation model, constructed using the UNET architecture with 5 levels. Designed specifically to capture nuclei in images, this project focuses on the nitty-gritty—building the right layers and fine-tuning parameters. Our aim? Simple—attain the highest accuracy and optimal results.
Explore the core functionalities of our project:

- **Data Management:**
  - Store data effortlessly on Amazon S3 for seamless accessibility.

- **Data Preprocessing:**
  - Ingest and transform data to optimize it for the training pipeline.

- **Custom Dataset Creation:**
  - Tailor your dataset to meet specific project requirements.

- **Model Development:**
  - Construct a UNET-style deep learning model, enriched with dropouts, batch normalization, and hyperparameter tuning.

- **Results Visualization:**
  - Visualize model outcomes effectively using Lightning, enhancing insights.

- **CI/CD Pipeline:**
  - Establish a robust Continuous Integration and Continuous Deployment (CI/CD) pipeline using GitHub Actions for automated development workflows.

- **Application Dockerization:**
  - Enhance flexibility and portability by Dockerizing the application.

- **AWS Deployment:**
  - Deploy your model seamlessly on AWS using EC2 instances and the Elastic Container Registry (ECR). Streamline your model implementation for optimal performance in an AWS environment.


<a name="demo"></a>
## Demo
A GUI of the project will be posted soon at https://sam-deeplearning.vercel.app/human-segmentation. Stay tuned!

<a name="tech"></a>
## Technologies
- Python
- Pytorch
- Google Colab
- Numpy
- Matplotlib
- Transformers
- fastAPI
- Git and Github Actions
- Docker
- AWS S3, ECR, EC2

<a name="usage"></a>
## Usage
A GUI of the project will be posted soon at https://sam-deeplearning.vercel.app/human-segmentation. Stay tuned!

Additionally, you can use the following installation to clone and run the model locally on your computer.

To install this project, make sure you have the correct version of Python and pip.

<a name="installation"></a>
### Installation
- Switch to Python3.
- Follow the code below to create a virtual environment and install the necessary libraries.
(Currently tested on Python 3.8 and Python 3.10)
```
git clone https://github.com/samyarsworld/medical-image-segmentation.git
cd medical-image-segmentation

For Linux users:
python3 -m venv venv
source venv/bin/activate

For Windows users:
virtualenv venv
.\venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

<a name="dev"></a>
## Developer Features
Here are some technical considerations that were used to build and design this project:

**Object-oriented design in Python:** The 



<a name="future"></a>
## Future Improvements
<a name="power"></a>
### Efficiency and AI Power
There are several ways that the trained model could perform. Here are a few suggestions:

- **Implement a more sophisticated AI system:** The


<a name="credits"></a>
## Credits

- SAMYAR FARJAM (https://github.com/samyarsworld)

If you'd like to contribute to our segmentation model, please feel free to submit a pull request or open an issue on our [GitHub repository](https://github.com/samyarsworld/medical-image-segmentation). We welcome all contributions and feedback.

<a name="license"></a>
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
