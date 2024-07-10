# Dataset Documentation
This project utilizes several publicly available datasets for training and testing the face and eye detection model. Below are the details and access links for each dataset.

- **Flickr-Faces-HQ Dataset (FFHQ)**
    - **Description**: It is a high-quality image dataset of human faces, originally created as a benchmark for generative adversarial networks (GAN). The dataset consists of 70,000 high-quality PNG images at 1024×1024 resolution and contains considerable variation in terms of age, ethnicity and image background. It also has good coverage of accessories such as eyeglasses, sunglasses, hats, etc.
    - **Source**: [Link to the dataset](https://drive.google.com/drive/folders/1tg-Ur7d4vk1T8Bn0pPpUSQPxlPGBlGfv)
    - **License**: Creative Commons Attribution 4.0 International License (CC BY 4.0). For more details, visit the [FFHQ Dataset GitHub page](https://github.com/NVlabs/ffhq-dataset?tab=readme-ov-file).
    - **Usage in This Project**: A subset of the FFHQ dataset was used to train the face detection model. This subset was carefully selected to provide a diverse range of human faces, aiming for improved accuracy and robustness in face detection capabilities.


- **MRL Eye Dataset**
    - **Description**: The MRL Eye Dataset is a comprehensive collection of eye images collected by the Machine Learning Research Lab at VSB-Technical University of Ostrava. It is designed for use in eye tracking and detection applications, offering a wide variety of eye conditions, including different gaze directions, lighting conditions, and occlusions. This dataset is particularly useful for developing and testing algorithms for eye detection, gaze estimation, and eye tracking.
    - **Source**: [Link to the dataset](http://mrl.cs.vsb.cz/eyedataset)
    - **License**: Users are advised to check the website for specific license terms. Typically, academic datasets may be released under terms that allow for non-commercial research and educational use.
    - **Usage in This Project**: The MRL Eye Dataset was employed to enhance the eye detection capabilities of our model. By incorporating a diverse set of eye images, the model's performance in accurately detecting and tracking eyes under various real-world conditions has been significantly improved.


- **MIT Indoor Scenes CVPR 2019 Dataset**
    - **Description**: This dataset features a comprehensive collection of images depicting various indoor scenes. It was curated for the CVPR 2019 Workshop on Large Scale Holistic Video Understanding. The dataset is instrumental for computer vision tasks requiring background and environmental context understanding.
    - **Source**: [Link to the dataset](https://www.kaggle.com/datasets/itsahmad/indoor-scenes-cvpr-2019)
    - **License**: The dataset is hosted on Kaggle, and users should consult the specific license terms and conditions on the dataset's page. Kaggle datasets are generally subject to the Kaggle Data License, which may differ based on the dataset.
    - **Usage in This Project**: A subset of the MIT Indoor Scenes CVPR 2019 dataset has been utilized as negative images for the face and eye detection models. Prior to use, images containing human faces were manually removed to ensure the dataset exclusively enhances the models' ability to identify the absence of target features in various indoor settings. This meticulous selection process serves to improve the models' accuracy and robustness in detecting faces and eyes under diverse conditions.


- **ADE20K Outdoors Dataset**
    - **Description**: The ADE20K Outdoors dataset is part of the ADE20K dataset, focusing on outdoor scenes. It encompasses a wide range of natural and urban environments, making it a valuable resource for computer vision tasks that require contextual understanding of outdoor settings.
    - **Source**: [Link to the dataset](https://www.kaggle.com/datasets/residentmario/ade20k-outdoors)
    - **License**: Users should review the specific license terms and conditions on the dataset's Kaggle page. Kaggle datasets are typically subject to the Kaggle Data License, which may vary for each dataset.
    - **Usage in This Project**: A subset of the ADE20K Outdoors dataset has been used as negative images for the face and eye detection models. To ensure the dataset's effectiveness in this role, images containing human faces or eyes were manually removed. This process helps to refine the models' ability to accurately detect the absence of faces and eyes in outdoor scenes, thereby enhancing their overall detection capabilities in diverse conditions.


Please ensure you comply with the respective licenses and usage guidelines when utilizing these datasets.


