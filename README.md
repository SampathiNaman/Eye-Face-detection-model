# Enhanced Face and Eye Detection in Real-Time Using Haarcascades in OpenCV

## Overview
This repository hosts a custom-trained model for face and eye detection, leveraging the power of OpenCV in Python. Developed by [SampathiNaman](https://github.com/SampathiNaman), this project aims to provide a versatile and more accurate detection system by using a model trained on a unique dataset.

## Components
- A custom-trained Haar Cascade models for detecting faces and eyes.
- `main.py` script for face and eye detection.

## Key Features
- **Custom-Trained Haar Cascade Model:** Specifically trained for detecting faces and eyes with improved accuracy on custom datasets.
- **Versatile Detection:** Supports detection in static images, video files, and real-time through webcam.
- **Easy to Use:** Simple Python script to demonstrate the model's usage across different media types.

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
- A special thanks to the developers of the Cascade Training GUI application, which greatly simplified the process of training our custom Haar Cascade model. Their tool provided an intuitive interface and powerful features that enabled us to efficiently train and fine-tune our detection model.
- Gratitude is also extended to Innovate for providing the internship opportunity that made this project possible. Their support and guidance have been invaluable in completing this project.
