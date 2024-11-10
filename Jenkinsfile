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
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Додаємо кореневий шлях проєкту до PYTHONPATH
                sh 'export PYTHONPATH=$PYTHONPATH:$(pwd)'

                // Перевіряємо наявність файлів у папці tests
                sh 'ls tests'
                
                // Запускаємо тести
                sh '. venv/bin/activate && pytest --disable-warnings tests/'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/test-results/*.xml', allowEmptyArchive: true
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}
