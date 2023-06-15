pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        echo "This is jenkins file"
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python automate_top.py'
      }
    }
  }
}
