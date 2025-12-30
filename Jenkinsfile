pipeline {
    agent any

    // Build parameters for user-controlled options
    parameters {
        booleanParam(name: 'executeTests', defaultValue: true, description: 'Run tests?')
        string(name: 'ENV', defaultValue: 'dev', description: 'Deployment environment')
    }

    // Environment variables accessible throughout the pipeline
    environment {
        APP_ENV = "${params.ENV}" // Use parameter for environment
        BUILD_INFO = "Build-${env.BUILD_NUMBER}"
        MAVEN_HOME = "C:/Program Files/Apache/Maven/bin" // Update to your Maven installation path
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building in environment: ${env.APP_ENV}"
                echo "Build info: ${env.BUILD_INFO}"
                bat "\"${env.MAVEN_HOME}/mvn\" -B -DskipTests package"
            }
        }

        stage('Test') {
            // Run tests only if executeTests parameter is true
            when {
                expression { return params.executeTests }
            }
            steps {
                echo "Running tests in environment: ${env.APP_ENV}"
                echo "Build info: ${env.BUILD_INFO}"
                bat "\"${env.MAVEN_HOME}/mvn\" test"
            }
        }

        stage('Deploy') {
            // Deploy only if Build succeeded (and Test ran successfully if enabled)
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo "Deploying in environment: ${env.APP_ENV}"
                echo "Build info: ${env.BUILD_INFO}"
                bat "bash deploy.sh"
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed. Environment: ${env.APP_ENV}, ${env.BUILD_INFO}"
        }
        success {
            echo "Build succeeded. ${env.BUILD_INFO}"
        }
        failure {
            echo "Build failed. ${env.BUILD_INFO}"
        }
    }
}
