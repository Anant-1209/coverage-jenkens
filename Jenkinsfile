pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/Anant-1209/coverage-jenkens.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // Setup virtual environment
                    sh 'python -m venv ${VIRTUAL_ENV}'
                    sh '. ${VIRTUAL_ENV}/Scripts/activate'  // For Windows
                    // sh 'source ${VIRTUAL_ENV}/bin/activate'  // For Linux/Mac
                    sh 'pip install -r requirements.txt'  // Install dependencies
                }
            }
        }
        stage('Run Tests and Coverage') {
            steps {
                script {
                    // Run the tests and generate coverage report
                    sh '. ${VIRTUAL_ENV}/Scripts/activate'  // For Windows
                    // sh 'source ${VIRTUAL_ENV}/bin/activate'  // For Linux/Mac
                    sh 'coverage run -m unittest discover'  // Run the tests
                    sh 'coverage html'  // Generate HTML coverage report
                }
            }
        }
        stage('Publish Coverage') {
            steps {
                // Publish the coverage report as an artifact or display it
                publishHTML(target: [
                    reportName: 'Coverage Report',
                    reportDir: 'htmlcov',
                    reportFiles: 'index.html'
                ])
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube analysis (using the correct shell command)
                    sh ''' 
                    sonar-scanner.bat \
                    -D"sonar.projectKey=jenkins-coverage" \
                    -D"sonar.sources=." \
                    -D"sonar.host.url=http://localhost:9000" \
                    -D"sonar.token=sqp_a7afb85079007fecf6fe1e7a7b6014e6349ce01c"
                    '''
                }
            }
        }
    }
    post {
        always {
            // Clean up (optional)
            cleanWs()
        }
    }
}
