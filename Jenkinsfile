pipeline {
    agent any

    environment {
        IMAGE = 'adl6002/devops-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log --oneline -n 3'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                    pytest -v
                '''
            }
        }

        stage('Build & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'DH_USER',
                                                  passwordVariable: 'DH_PASS')]) {
                    sh '''
                        docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .
                        echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin
                        docker push $IMAGE:$BUILD_NUMBER
                        docker push $IMAGE:latest
                        docker logout
                    '''
                }
            }
        }
    }
}
