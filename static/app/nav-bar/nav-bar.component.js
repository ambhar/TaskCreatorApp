'use strict';

angular.module('navBar').
    component('navBar', {
        templateUrl : "nav-bar.html",
        controller: function($cookies, $http, $location, $routeParams, $scope, $filter, $window){

            var tokenExists = $cookies.get("token")
            if (tokenExists) {
                
                $scope.loggedin = true

            
           }
           $scope.signout = function(){
                $cookies.remove("username");
                $cookies.remove("token");
                $cookies.remove("userid");
                $window.location.href="http://"+$window.location.host+"/login/";
            }

           $scope.signin = function(){
                $window.location.href="http://"+$window.location.host+"/login/";
            }
            
           $scope.signup = function(){
                $window.location.href="http://"+$window.location.host+"/signup/";
            }
        }
    })
    