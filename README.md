# Image Analysis Platform

## Overview
This Django application serves as an image analysis and commenting platform. Users can upload images for analysis, view analyzed images with descriptions, and add/view comments. The application integrates with AWS Rekognition for image analysis.

## Table of Contents
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Environment](#setting-up-the-environment)
- [Configuration](#configuration)
  - [AWS Rekognition Integration](#aws-rekognition-integration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
Before setting up the application, ensure you have the following installed:
- Python (>=3.x)
- pip (Python package installer)
- virtualenv (optional but recommended)

### Setting Up the Environment
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-analysis-platform.git
   cd image-analysis-platform


Create a virtual environment (optional but recommended):
'python -m venv venv'
'source venv/bin/activate'  # On Windows: venv\Scripts\activate


Install dependencies:
'pip install -r requirements.txt'


Configuration
AWS Rekognition Integration
To enable image analysis, set up AWS Rekognition and configure the application with your AWS credentials.

Create an AWS account.
Create AWS access keys.

Set the following environment variables:
'export AWS_ACCESS_KEY_ID=your-access-key-id'
'export AWS_SECRET_ACCESS_KEY=your-secret-access-key'

or Can be set by using awscli:
Install awscli by using 'pip install awscli'
'aws configure' for configure access key and secret access key


Running the Application
Run the Django development server:
'python manage.py runserver'


Access the application at http://localhost:8000.

API Endpoints
POST /analyze-image: Upload and analyze images.
GET /images: Retrieve a list of analyzed images.
GET /image/<id>: Retrieve details of a specific analyzed image.
POST /image/<id>/comment: Add a comment to a specific image.

1. POST /analyze-image:
Purpose: Accepts image uploads and sends them to AWS Rekognition for analysis.
Implementation:
Users can make a POST request to /analyze-image with an image file in the request.
The application handles image uploads securely and efficiently.
It integrates with AWS Rekognition to analyze images, extracting labels from the API response.
The analysis result is saved in the database along with the image.

2. GET /images:
Purpose: Retrieves a list of analyzed images with descriptions, suitable for infinite scrolling.
Implementation:
Users can make a GET request to /images to retrieve a paginated list of analyzed images.
The API supports infinite scrolling, fetching a limited number of images per request.
Each response includes image details like ID, description, and comments.

3. GET /image/<id>:
Purpose: Retrieves a specific analyzed image, its description, and comments.
Implementation:
Users can make a GET request to /image/<id> to get details of a specific analyzed image.
The response includes the image's ID, description, and a list of comments associated with the image.

4. POST /image/<id>/comment:
Purpose: Allows users to add a comment to a specific image.
Implementation:
Users can make a POST request to /image/<id>/comment with the text of the comment.
The application associates the comment with the specified image and saves it in the database.
Comments provide a way for users to interact with and discuss the analyzed images.


Documentation
For more details on API usage and functionality, refer to the official API documentation.