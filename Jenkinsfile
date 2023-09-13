pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        echo "This is jenkins file"
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 automate_top.py'
      }
    }
  }
}
