'use strict';

angular.module('userLogin').
    component('userLogin', {
        templateUrl : "login.html",
        controller: function($cookies, $http, $location, $routeParams, $rootScope, $scope, $window){
            var loginUrl = 'api/login/'
            
            $scope.loginMessage = "";
            var tokenExists = $cookies.get("token")
            var usernameExists = $cookies.get("username")
            
            if (tokenExists) {
                $location.path("/homepage/")
                
                
            } 
            $scope.doLogin = function(user){
                
                var reqConfig = {
                    method: "POST",
                    url: loginUrl,
                    data: {
                        username: user.username,
                        password: user.password
                    },
                   
                }

                var loginRequestAction = $http(reqConfig)

                loginRequestAction.success(function(r_data, r_status, r_headers, r_config) {
                    $cookies.put("token", r_data.token)
                    $cookies.put("username", r_data.username)
                    $cookies.put("userid", r_data.id)
                    $window.location.href="http://"+$window.location.host+"/homepage/";
                    console.log(r_data)
                    

                })
                loginRequestAction.error(function(e_data, e_status, e_headers, e_config) {
                    $scope.loginMessage = "Invalid Credentials"
                })

            }
           
        }
    })
    