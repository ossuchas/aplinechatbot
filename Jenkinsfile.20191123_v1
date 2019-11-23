pipeline {
  environment {
    registry = "apthailand/suchat_s"
    registryCredential = 'docker_ossuchas'
    dockerImage = ''
    image_tag_number = 'chatbot_api_v1.0.3'
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
    stage('Deploy 2 OKD') {
      steps{
          sh "oc login --insecure-skip-tls-verify https://devops01-master.apthai.com:8443 -usuchat_s -pP@ssw0rd"
          sh "oc project testrepo"
          sh "oc patch dc linechatbot --patch='{\"spec\":{\"template\":{\"spec\":{\"containers\":[{\"name\": \"linechatbot\", \"image\":\"docker.io/apthailand/suchat_s:chatbot_api_v1.0.3\"}]}}}}'"
      }
    }
  }
}
