pipeline {
  environment {
    registry = "ossuchas/aplinechatbot"
    registryCredential = 'docker_ossuchas'
    dockerImage = ''
    image_tag_number = 'v1.3.4'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/ossuchas/aplinechatbot.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":" + image_tag_number
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
  }
}
