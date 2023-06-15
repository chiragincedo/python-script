pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        echo "This is jenkins file"
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python automate_top.py'
      }
    }
  }
}
