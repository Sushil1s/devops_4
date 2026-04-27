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
        // This ensures selenium is present every time the build runs
        sh 'pip install selenium' 
        sh 'touch tests/__init__.py'
        sh 'python3 -m unittest discover tests'
    }
}
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s.yaml'
            }
        }
    }
}
