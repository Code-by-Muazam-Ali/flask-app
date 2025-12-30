pipeline {
    agent any

    stages {
        // Stage 1: Clone the Repository
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: Install Dependencies
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                // Create a virtual environment and install requirements for Windows
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        // Stage 3: Run Unit Test
        stage('Run Unit Test') {
            steps {
                echo 'Running tests...'
                // Run pytest inside the virtual environment for Windows
                bat 'venv\\Scripts\\pytest'
            }
        }

        // Stage 4: Build Application
        stage('Build') {
            steps {
                echo 'Building application package...'
                // Build a distribution package for Windows
                bat 'venv\\Scripts\\pip install build'
                bat 'venv\\Scripts\\python -m build'
                // Archive the artifacts (the built files) so you can download them from Jenkins
                archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
            }
        }

        // Stage 5: Deploy (Simulated)
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // In a real scenario, you would copy files to a server here.
                // For this lab, we print a success message.
                bat 'echo Deployment successful!'
            }
        }
    }
}
