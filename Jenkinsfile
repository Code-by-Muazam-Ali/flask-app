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
                // Create a virtual environment and install requirements
                // Note: For Windows, use: bat 'python -m venv venv && venv\\Scripts\\pip install -r requirements.txt'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        // Stage 3: Run Unit Test
        stage('Run Unit Test') {
            steps {
                echo 'Running tests...'
                // Run pytest inside the virtual environment
                // Note: For Windows, use: bat 'venv\\Scripts\\pytest'
                sh '. venv/bin/activate && pytest'
            }
        }

        // Stage 4: Build Application
        stage('Build') {
            steps {
                echo 'Building application package...'
                // Build a distribution package
                sh '. venv/bin/activate && pip install build && python -m build'
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
                sh 'echo "Deployment successful!"'
            }
        }
    }
}
