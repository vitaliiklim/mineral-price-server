pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'git@github.com:vitaliiklim/mineral-price-server.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Створення віртуального середовища та встановлення залежностей
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Запуск тестів у віртуальному середовищі
                sh '. venv/bin/activate && python -m unittest discover'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            echo 'Some tests failed.'
        }
    }
}
