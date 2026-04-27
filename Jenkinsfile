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
                echo 'Starting Test Container and Running UI Tests...'
                sh '''
                    # 1. Clean up any leftover containers from previous failed runs
                    docker rm -f devops4_test || true
                    
                    # 2. Run your newly built app in the background (-d) on port 5000
                    docker run -d -p 5000:5000 --name devops4_test sushilchavan02/devops_4:latest
                    
                    # 3. Give Flask a few seconds to fully boot up
                    sleep 5
                    
                    # 4. Create venv and run the tests
                    python3 -m venv test_env
                    . test_env/bin/activate
                    pip install selenium
                    touch tests/__init__.py
                    python3 -m unittest discover tests
                '''
            }
            post {
                always {
                    // 5. Destroy the temporary test container (runs whether tests pass or fail)
                    echo 'Tearing down test container...'
                    sh 'docker rm -f devops4_test || true'
                }
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
