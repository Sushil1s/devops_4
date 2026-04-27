pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
                // IMPORTANT: Replace 'yourusername' with your actual Docker Hub username
                sh 'docker build -t yourusername/devops_4:latest .'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Installing dependencies and running Selenium UI Tests...'
                // Install Selenium for the isolated Jenkins user environment
                sh 'pip3 install selenium --break-system-packages'
                
                // Ensure Python recognizes the tests folder
                sh 'touch tests/__init__.py'
                
                // Discover and execute all tests
                sh 'python3 -m unittest discover tests'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying to Kubernetes...'
                sh 'kubectl apply -f k8s.yaml'
            }
        }
    }
}
