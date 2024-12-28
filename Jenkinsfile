pipeline {
    agent any
    environment {
        VIRTUAL_ENV = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git branch: 'main', url: 'https://github.com/Anant-1209/coverage-jenkens.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // Setup virtual environment
                    echo 'Setting up Python virtual environment...'
                    sh 'python -m venv ${VIRTUAL_ENV}'  // Create virtual environment
                    
                    // Activate the virtual environment depending on the OS
                    if (isUnix()) {
                        sh 'source ${VIRTUAL_ENV}/bin/activate'  // For Linux/Mac
                    } else {
                        sh '. ${VIRTUAL_ENV}/Scripts/activate'  // For Windows
                    }
                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run Tests and Coverage') {
            steps {
                script {
                    // Activate the virtual environment before running tests
                    if (isUnix()) {
                        sh 'source ${VIRTUAL_ENV}/bin/activate'  // For Linux/Mac
                    } else {
                        sh '. ${VIRTUAL_ENV}/Scripts/activate'  // For Windows
                    }
                    
                    // Run the tests and generate the coverage report
                    echo 'Running tests with coverage...'
                    sh 'coverage run -m unittest discover'  // Run the tests
                    sh 'coverage html'  // Generate HTML coverage report
                }
            }
        }
        stage('Publish Coverage') {
            steps {
                // Publish the coverage report as an artifact or display it
                echo 'Publishing the coverage report...'
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
                    // Run SonarQube analysis
                    echo 'Running SonarQube analysis...'
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
            // Clean up workspace after the pipeline execution
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
