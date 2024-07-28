# ShareSafely

## Project Workflow
![Project Workflow Design](https://github.com/user-attachments/assets/07e33b0b-68c4-43b4-bebe-444434ebd257)


## Project Overview
Welcome to the documentation for **ShareSafely**, a web application I've developed to securely manage file uploads using Azure Blob Storage. The application not only allows users to upload files but also generates unique, time-limited links for secure sharing. Additionally, it includes a mechanism for automated cleanup of expired files using Azure Functions.

## Features
- **Secure File Uploads:** Users can securely upload files to Azure Blob Storage.
- **Time-Limited Sharing:** The app generates unique URLs with a limited duration, ensuring that files can only be accessed by authorized users.
- **Automated Cleanup:** Periodic cleanup of expired files is handled using Azure Functions.
- **Monitoring and Alerts:** Set up with Azure Monitor to keep track of the app's performance and health.
- **Secure Credential Management:** Azure Key Vault is used to securely store and manage sensitive credentials.

## Technologies Used
- **Azure Blob Storage**: For secure file storage.
- **Azure Web Apps**: Hosting the web application.
- **Azure Key Vault**: Secure management of secrets.
- **Azure Monitor**: Monitoring and alerting on app performance.
- **Azure Functions**: For automation tasks like cleanup.
- **Python (Flask)**: The backend framework used for development.

## Setup and Configuration

### Prerequisites
To get started with the ShareSafely project, you’ll need the following:
- An Azure account
- A Python environment
- Visual Studio Code or another code editor

### Steps

#### 1. Azure Blob Storage Setup
I began by setting up an Azure Blob Storage account named "sharesafelystrg" and a container named "uploads" to store the uploaded files. Key security configurations include:
- Enabling "Secure transfer required"
- Disabling "Allow Blob Anonymous access"
- Enabling soft delete for blobs and containers

#### 2. Web Application Development
The application was developed using Flask in Python. Below is the structure of the project:

ShareSafelyApp/
├── app.py
├── templates/
│ ├── upload.html
│ └── link.html
└── static/
└── styles.css


- **app.py**: Handles the main application logic, including file uploads and generating SAS tokens.
- **upload.html** and **link.html**: HTML templates for the user interface.
- **styles.css**: Styling for the application.

#### 3. Secure Credentials with Azure Key Vault
To secure sensitive data, I used Azure Key Vault to store the Storage Account key. The application retrieves these credentials securely at runtime, ensuring that sensitive data is not exposed in the source code.

#### 4. Deploying to Azure Web Apps
The web application was deployed to Azure Web Apps using Visual Studio Code. During this process, I configured environment variables such as `KEY_VAULT_URI` and `SECRET_NAME` and enabled a system-assigned managed identity to access the Azure Key Vault.

#### 5. Monitoring and Maintenance
Azure Monitor was used to set up metrics for monitoring the application's performance, including CPU usage and response times. I also set up alerts to notify me of any critical issues, such as server errors.

#### 6. Periodic Cleanup with Azure Functions

![Azure Functions (iii)](https://github.com/user-attachments/assets/198a3bd6-4cc3-40ae-a618-caccd123676d)

![Azure Functions (Testing) (i)](https://github.com/user-attachments/assets/29ea4f85-3230-4be2-83f3-1ef3ebb3af1a)

![Azure Functions (Testing) (ii)](https://github.com/user-attachments/assets/534e0a83-a511-4c7c-bd98-c7c22ce265cd)

![Azure Functions (Testing) (iv)](https://github.com/user-attachments/assets/091e0899-1a34-4bfd-be9e-f7a1492bae60)




To manage storage and ensure security, I implemented an Azure Function named `BlobCleanupFunction` that automatically deletes files after a certain period. This function runs on a schedule, ensuring that expired files are removed promptly.

## Testing

![Testing (ii)](https://github.com/user-attachments/assets/a89b2fcd-770d-43ec-aa97-2ed9d3b2cf04)

![Testing (iv)](https://github.com/user-attachments/assets/d696ee1d-d456-445d-8895-34a5ce5a00fb)

![Testing (vi)](https://github.com/user-attachments/assets/3e4a6af3-7973-4ad0-ac5b-65c5d1e5a880)


To ensure that everything was working correctly, I conducted a final test of the ShareSafely application.

I accessed the ShareSafelyApp through the Azure Portal, navigating to the overview page of the Web App. I then opened the application in my browser using the Web App URL.

Once on the app interface, I tested the file upload functionality by uploading a file named **"Project Workflow Design"**, which was not previously present in the **"uploads"** container. Upon clicking the upload button, the application displayed a new browser tab with a unique, time-limited link to the uploaded file.

As per the design of the application, this link is intended to expire after 15 seconds to ensure security and controlled access. I confirmed the expiration feature by attempting to access the link after the specified duration; as expected, the link was no longer accessible, validating that the application's security mechanisms were functioning as intended.

### Testing Video :

https://github.com/user-attachments/assets/382b65d5-55a2-4623-b648-eb4e3fc07085

## Conclusion

The ShareSafely project successfully implemented a secure and efficient file-sharing web application using Azure services. The project demonstrated comprehensive skills in Azure Blob Storage, Azure Web Apps, Azure Key Vault, Azure Functions, and Azure Monitor. Through rigorous testing, including the final testing phase, all functionalities—secure uploads, time-limited link generation, and automated cleanup—were validated. 

## Skills Demonstrated
- **Secure File Management**: Implemented secure file storage using Azure Blob Storage with controlled access through SAS tokens.
- **Web Application Development**: Developed a web application using Python and Flask, with front-end and back-end integration.
- **Credential Management**: Utilized Azure Key Vault for secure storage and retrieval of sensitive information, enhancing security practices.
- **Automated Maintenance**: Created Azure Functions for automated cleanup of expired files, demonstrating skills in serverless computing.
- **Monitoring and Alerting**: Configured Azure Monitor and Alerts to track application performance and handle potential issues proactively.
- **Deployment and DevOps**: Deployed the web application on Azure Web Apps, including environment configuration and managing deployment processes.

## Repository Contents
- **Manual**: A detailed manual documenting each step of the project, including configurations, testing procedures, and troubleshooting tips.
- **Screenshots**: Visual documentation of key stages and configurations throughout the project, providing a visual guide and reference.
- **Source Code**: All the source code used in this project, including the Flask application, Azure Functions, and any associated scripts, organized in the `source_code` folder.
 
## Contact
For any questions or further information, feel free to reach out to me on LinkedIn: https://www.linkedin.com/in/vivek-vashisht04/
