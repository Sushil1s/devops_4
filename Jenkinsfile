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
                sh 'docker build -t sushilchavan02/devops_4:latest .'
            }
        }
        
       stage('Test') {
            steps {
                echo 'Setting up Virtual Environment and running UI Tests...'
                sh '''
                    # 1. Create a virtual environment named 'test_env'
                    python3 -m venv test_env
                    
                    # 2. Activate the environment
                    . test_env/bin/activate
                    
                    # 3. Install Selenium safely inside the bubble (no system warnings)
                    pip install selenium
                    
                    # 4. Prepare and run the tests
                    touch tests/__init__.py
                    python3 -m unittest discover tests
                '''
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
