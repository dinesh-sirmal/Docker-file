pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_PATH = "${WORKSPACE}/docker-compose.yml"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/dinesh-sirmal/Docker-file.git', branch: 'main'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose -f $DOCKER_COMPOSE_PATH build'
            }
        }

        stage('Run Docker Containers') {
            steps {
                sh 'docker-compose -f $DOCKER_COMPOSE_PATH up -d'
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        always {
            echo 'CI/CD pipeline finished.'
        }
    }
}
