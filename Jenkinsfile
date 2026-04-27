pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t yourusername/devops_4:latest .'
            }
        }
    stage('Test') {
        steps {
            echo 'Installing dependencies and running tests...'
            // Fix: Changed 'pip' to 'pip3'
            sh 'pip3 install selenium --break-system-packages' 
            sh 'touch tests/__init__.py'
            sh 'python3 -m unittest discover tests'
        }
}
}
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s.yaml'
            }
        }
    }
}
