pipeline {

	agent any

	stages {
		stage('python36') {
			steps {
				sh 'tox -e py36'
			}
		}
		stage('python37') {
			steps {
				sh 'tox -e py37'
			}
		}
		stage('python38') {
			steps {
				sh 'tox -e py38'
			}
		}
		stage('style') {
			steps {
				sh 'tox -e style'
			}
		}
	}

	options  {
		buildDiscarder ( logRotator ( numToKeepStr:  '5' ,  artifactNumToKeepStr:  '5' ))
	}

}
