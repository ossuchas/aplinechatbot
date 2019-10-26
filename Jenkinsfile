pipeline {
  environment {
    registry = "ossuchas/aplinechatbot"
    registryCredential = 'docker_ossuchas'
    dockerImage = ''
    image_tag_number = 'v1.0.2'
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
    stage('Remove Dangling docker image') {
      steps{
        sh 'docker rmi $(docker images -f dangling=true -q)'
      }
    }
  }
}
