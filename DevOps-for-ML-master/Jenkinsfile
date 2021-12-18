pipeline {
   agent any

   stages {
      stage('Clone New Code') {
         steps {
            cleanWs()
            git 'https://github.com/kalikichandu/DevOps-for-ML.git'
                      
         }
      }
      stage('Build and Run Docker Container') {
         steps {
            script {
                
                  sh 'chmod 700 ${WORKSPACE}/Dockerfile'
                  sh 'chmod 700 ${WORKSPACE}/CI_and_CD/src/inference.py'
                  sh 'chmod 700 ${WORKSPACE}/requirements.txt'
                  
                  sh 'sudo docker build --tag ml_api .'
                  
                  sh 'sudo docker tag ml_api kalikichandu/house_price_prediction_image:v0.${BUILD_NUMBER}'
                  sh 'sudo docker push kalikichandu/house_price_prediction_image:v0.${BUILD_NUMBER}'
                  
                  sh 'scp ${WORKSPACE}/Dockerfile azure_prod@104.43.164.138:/home/azure_prod/house_price_prediction_api/'
                  sh 'scp ${WORKSPACE}/requirements.txt azure_prod@104.43.164.138:/home/azure_prod/house_price_prediction_api/'
                  sh 'scp ${WORKSPACE}/CI_and_CD/src/inference.py azure_prod@104.43.164.138:/home/azure_prod/house_price_prediction_api/src/'
                    
                  sh 'ssh azure_prod@104.43.164.138 sudo docker pull kalikichandu/house_price_prediction_image:v0.${BUILD_NUMBER}'
                  sh 'ssh azure_prod@104.43.164.138 sudo docker run -d -p 5000:5000 -v ml_vol:/var/house_price_prediction/ kalikichandu/house_price_prediction_image:v0.${BUILD_NUMBER}'

            }
          
         }
      }

   }
}
