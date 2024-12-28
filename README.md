# Enhanced Real-Time Face and Eye Detection Using Custom Haar Cascades in OpenCV

## Overview
This repository features a custom-trained model for real-time face and eye detection utilizing OpenCV in Python. Developed by [SampathiNaman](https://github.com/SampathiNaman), this project integrates machine learning with classical computer vision techniques to deliver robust and efficient detection.

## Components
- A custom-trained Haar Cascade models for detecting faces and eyes.
- `main.py` script for face and eye detection.

## Methodology
- **Data Collection:** Gather a diverse dataset of images featuring faces and eyes in various environments, poses, and lighting conditions.  
- **Preprocessing:** Apply techniques such as resizing, normalization, and data augmentation to enhance dataset quality and diversity.  
- **Model Training:** Train custom Haar Cascade classifiers using annotated datasets for precise face and eye detection.  
- **Optimization:** Fine-tune models to improve detection accuracy and minimize false positives.  
- **Integration:** Embed trained Haar Cascade models into the OpenCV framework for seamless real-time detection.  
- **Evaluation:** Test performance on benchmark datasets and real-world scenarios to assess accuracy, speed, and robustness.  
- **Deployment:** Optimize for real-time applications, ensuring compatibility with various hardware environments. 

## Key Features
- **Custom-Trained Haar Cascade Model:** Specifically trained for detecting faces and eyes with improved accuracy on custom datasets.
- **Versatile Detection:** Supports detection in static images, video files, and real-time through webcam.
- **Easy Deployment:** Simple Python script to demonstrate the model's usage across different media types.

## Technology
- **Programming Language**: Python 
- **Libraries**: OpenCV, NumPy 
- **Machine Learning Framework**: scikit-learn 
- **Tools**: Haarcascade XML files, Anaconda, Jupyter Notebooks 
- **Hardware**: Compatible with CPUs and GPUs for deployment on various platforms

## Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV library

You can install OpenCV using pip:
```bash
pip install opencv-python
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/SampathiNaman/Face-and-eye-detection.git
```
2. Navigate to the project directory:
```bash
cd Face-and-eye-detection
```

### Usage
Run the `main.py` script to use the model:
```bash
python main.py [options]
```
#### Options
- `--image IMAGE_PATH`: Specify the path to an image file for face and eye detection.
- `--video VIDEO_PATH`: Specify the path to a video file for face and eye detection.
- If no options are provided, the script will default to using the webcam for real-time detection.

#### Example Usage:
To detect faces and eyes in an image:
```bash
python main.py --image ./path-to-image/image.jpg
```
To detect faces and eyes in a video:
```
python main.py --video ./path-to-video/video.mp4
```
To run real-time detection via webcam:
```
python main.py
```


## Datasets Documentation
For a comprehensive overview of the datasets used in this project, and their applications within the project, please refer to our [detailed dataset documentation](Dataset.md). This documentation includes information on both the positive and negative datasets used in training and testing of the models.


## Contributing
We welcome contributions! If you have suggestions for improving the model or extending its functionalities,
please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Acknowledgments
- We extend our gratitude to the developers of the Cascade Training GUI application for simplifying the custom Haar Cascade training process.
- Special thanks to Innovate for their invaluable support and guidance during this internship project.
